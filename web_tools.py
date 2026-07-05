from tavily import TavilyClient
from dotenv import load_dotenv
from config import gemini_client
import os

load_dotenv()

# -----------------------------------
# Tavily Client
# -----------------------------------

tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

# -----------------------------------
# Research Trends Tool
# -----------------------------------

def research_trends(topic):

    # Search the web
    search_results = tavily_client.search(
        query=f"Latest research trends in {topic}",
        max_results=5
    )

    context = ""

    sources = []

    for result in search_results["results"]:

        title = result.get("title", "")
        content = result.get("content", "")
        url = result.get("url", "")

        context += f"""
Title: {title}

Content:
{content}

Source:
{url}

-----------------------------------------
"""

        sources.append(url)

    # Ask Gemini to summarize
    prompt = f"""
You are an AI Research Assistant.

Below are web search results.

Topic:
{topic}

Search Results:
{context}

Your job is to:

1. Explain the latest research trends.
2. Mention important breakthroughs.
3. Mention popular datasets, models or techniques.
4. Mention future research directions.
5. Keep the answer under 400 words.
6. Use ONLY the supplied search results.
7. Do NOT invent facts.

End your answer with a short bullet list called

Useful Sources
"""

    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    answer = response.text

    answer += "\n\nUseful Sources:\n"

    for url in sources:
        answer += f"- {url}\n"

    return answer