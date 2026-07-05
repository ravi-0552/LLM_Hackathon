from config import gemini_client, collection


def recommend_professors(user_query):
    """
    Retrieves the most relevant professors from ChromaDB
    and asks Gemini to recommend the best faculty.
    """

    # -----------------------------------
    # Embed User Query
    # -----------------------------------

    query_embedding = gemini_client.models.embed_content(
        model="models/gemini-embedding-001",
        contents=[user_query]
    )

    query_embedding = query_embedding.embeddings[0].values

    # -----------------------------------
    # Retrieve Top Matching Professors
    # -----------------------------------

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    retrieved_docs = results["documents"][0]

    # Debug (can remove later)
    print("\nRetrieved IDs:")
    print(results["ids"])

    print("\nRetrieved Distances:")
    print(results["distances"])

    # -----------------------------------
    # Build Context
    # -----------------------------------

    context = "\n\n".join(retrieved_docs)

    # -----------------------------------
    # Prompt Gemini
    # -----------------------------------

    prompt = f"""
You are an AI Faculty Recommendation Assistant.

Use ONLY the faculty profiles provided below.

Faculty Profiles:
{context}

Student Request:
{user_query}

Your responsibilities:

1. Recommend the TOP 3 professors.
2. Rank them from best to least suitable.
3. Explain why each professor matches.
4. Mention:
   • Research Interests
   • Courses
   • Projects
5. Keep the answer concise.
6. NEVER invent information.
7. If the information is unavailable, clearly say so.

Return the answer in this format:

🥇 Professor 1
Reason:
Research Areas:

🥈 Professor 2
Reason:
Research Areas:

🥉 Professor 3
Reason:
Research Areas:
"""

    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text