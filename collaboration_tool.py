from config import gemini_client, collection


def suggest_collaboration(user_query):
    """
    Suggests possible collaborations between professors
    based on their research interests and expertise.
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
    # Retrieve Relevant Professors
    # -----------------------------------

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=4
    )

    retrieved_docs = results["documents"][0]

    print("\nRetrieved IDs:")
    print(results["ids"])

    print("\nRetrieved Distances:")
    print(results["distances"])

    context = "\n\n".join(retrieved_docs)

    # -----------------------------------
    # Prompt Gemini
    # -----------------------------------

    prompt = f"""
You are an AI Faculty Collaboration Assistant.

Use ONLY the faculty profiles below.

Faculty Profiles:
{context}

User Request:
{user_query}

Your task is to:

1. Identify the best professors who can collaborate.
2. Explain WHY they complement each other.
3. Mention overlapping research interests.
4. Mention complementary expertise.
5. Suggest ONE interdisciplinary research project they could work on together.
6. Mention possible expected outcomes of this collaboration.
7. If the information is not available, clearly state that instead of inventing facts.

Return the answer in the following format:

Suggested Collaboration

Professor 1:
Professor 2:

Why this collaboration works:
...

Common Research Areas:
...

Complementary Expertise:
...

Possible Joint Project:
...

Expected Outcomes:
...
"""

    response = gemini_client.models.generate_content(
        model="-flash",
        contents=prompt
    )

    return response.text