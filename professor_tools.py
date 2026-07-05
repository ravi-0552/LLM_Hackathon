from config import gemini_client


def lookup_professor(user_query, documents):
    """
    Looks up a professor by name and returns a summary.
    """

    professor_name = user_query[13:].strip()

    professor_doc = None

    for doc in documents:
        if professor_name.lower() in doc.lower():
            professor_doc = doc
            break

    if professor_doc is None:
        return "Professor not found."

    prompt = f"""
You are an AI Faculty Assistant.

Use ONLY the information below.

Professor Profile:
{professor_doc}

Student Question:
{user_query}

Provide:

- Research Interests
- Courses
- Publications
- Projects
- Office Hours (if available)

Do NOT invent information.
"""

    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text