from tavily import TavilyClient
from config import gemini_client, TAVILY_API_KEY

tavily_client = TavilyClient(api_key=TAVILY_API_KEY)


def research_trends(query):

    search_results = tavily_client.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )

    context = ""

    for result in search_results["results"]:
        context += f"""
Title: {result['title']}
Content: {result['content']}
URL: {result['url']}

"""

    prompt = f"""
You are an AI Research Assistant.

Using the web search results below, answer the user's question.

User Question:
{query}

Web Search Results:
{context}

Provide:
1. A concise overview.
2. Latest research trends.
3. Important applications.
4. Future directions.

Keep the answer clear and well-structured.
"""

    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text