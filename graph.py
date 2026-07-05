from pydantic import BaseModel
from config import gemini_client
from typing import TypedDict

from langgraph.graph import StateGraph, END

from student_tools import recommend_professors
from professor_tools import lookup_professor
from web_tools import research_trends
from collaboration_tool import suggest_collaboration
from confirmation_tools import confirm_recommendation

class RouteDecision(BaseModel):
    tool: str

# ---------------------------------------
# Graph State
# ---------------------------------------

class FacultyState(TypedDict):

    query: str

    documents: list

    answer: str


# ---------------------------------------
# Router
# ---------------------------------------

def router(state):

    query = state["query"]

    prompt = f"""
You are an intelligent routing agent for a University Faculty Assistant.

Your job is to decide which ONE tool should answer the user's question.

Available tools:

student
- Recommend professors
- Find supervisors
- Suggest faculty based on interests
- Course recommendations

professor
- Questions about ONE specific professor
- Publications
- Research interests
- Office hours
- Biography

research
- Latest research trends
- Emerging technologies
- Recent advancements
- Future directions

collaboration
- Suggest faculty collaborations
- Joint research
- Interdisciplinary projects

Return ONLY the tool name.

User Question:
{query}
"""

    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": RouteDecision,
        },
    )

    decision = response.parsed

    print("\n========== ROUTER ==========")
    print("Selected Tool:", decision.tool)
    print("============================\n")

    tool = decision.tool.lower()

    valid_tools = {
    "student",
    "professor",
    "research",
    "collaboration"
    }

    if tool not in valid_tools:
        tool = "student"

    return tool


# ---------------------------------------
# Student Node
# ---------------------------------------

def student_node(state):

    answer = recommend_professors(
        state["query"]
    )

    return {
        **state,
        "answer": answer
    }


# ---------------------------------------
# Professor Node
# ---------------------------------------

def professor_node(state):

    answer = lookup_professor(
        state["query"],
        state["documents"]
    )

    return {
        **state,
        "answer": answer
    }


# ---------------------------------------
# Research Node
# ---------------------------------------

def research_node(state):

    topic = state["query"][18:].strip()

    answer = research_trends(topic)

    return {
        **state,
        "answer": answer
    }


# ---------------------------------------
# Collaboration Node
# ---------------------------------------

def collaboration_node(state):

    answer = suggest_collaboration(
        state["query"]
    )

    return {
        **state,
        "answer": answer
    }


# ---------------------------------------
# Human Approval Node
# ---------------------------------------

def confirmation_node(state):

    confirm_recommendation(
        state["answer"]
    )

    return state


# ---------------------------------------
# Build Graph
# ---------------------------------------

builder = StateGraph(FacultyState)

builder.add_node("student", student_node)
builder.add_node("professor", professor_node)
builder.add_node("research", research_node)
builder.add_node("collaboration", collaboration_node)
builder.add_node("confirmation", confirmation_node)

builder.set_conditional_entry_point(
    router,
    {
        "student": "student",
        "professor": "professor",
        "research": "research",
        "collaboration": "collaboration"
    }
)

builder.add_edge("student", "confirmation")
builder.add_edge("professor", "confirmation")
builder.add_edge("research", "confirmation")
builder.add_edge("collaboration", "confirmation")

builder.add_edge("confirmation", END)

graph = builder.compile()