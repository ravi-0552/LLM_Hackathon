from config import gemini_client, collection
from graph import graph

# ---------------------------------------
# Read Professor Files
# ---------------------------------------

documents = []
embeddings = []
ids = []

for i in range(1, 12):

    filename = f"professor{i}.txt"

    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    documents.append(text)
    ids.append(str(i - 1))

    embedding = gemini_client.models.embed_content(
        model="models/gemini-embedding-001",
        contents=[text]
    )

    embeddings.append(
        embedding.embeddings[0].values
    )

# ---------------------------------------
# Store Only Once
# ---------------------------------------

if collection.count() == 0:

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings
    )

    print("Professor profiles stored successfully.")

else:

    print("Professor profiles already exist.")

# ---------------------------------------
# Chat Loop
# ---------------------------------------

while True:

    query = input("\nAsk your question (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    state = {
        "query": query,
        "documents": documents,
        "answer": ""
    }

    result = graph.invoke(state)

    print("\n========================================")
    print("Final Answer")
    print("========================================")
    print(result["answer"])
    print("========================================")