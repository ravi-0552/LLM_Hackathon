# 🎓 AI Faculty Recommendation & Research Assistant

An intelligent AI-powered Faculty Recommendation and Research Assistant built for our LLM Hackathon. The system helps students discover suitable professors based on their interests, learn about faculty members, explore current research trends, and identify potential research collaborations using Retrieval-Augmented Generation (RAG) and LangGraph.

---

## 🚀 Features

### 🎯 Faculty Recommendation

* Recommends the most suitable professors based on a student's research interests.
* Uses semantic search with ChromaDB and Gemini embeddings.
* Ranks professors by relevance.

### 👨‍🏫 Professor Information

* Retrieves detailed information about professors including:

  * Research Interests
  * Courses
  * Publications
  * Current Projects
  * Office Hours

### 🔍 Research Trends

* Fetches and summarizes the latest developments in a research area.
* Helps students stay updated with emerging technologies.

### 🤝 Collaboration Suggestions

* Suggests professors who could collaborate on interdisciplinary research based on their expertise.

### 🧠 Intelligent Routing

* Uses LangGraph to intelligently route user queries to the appropriate tool instead of relying on fixed command formats.

### 📚 Retrieval-Augmented Generation (RAG)

* Stores professor profiles in ChromaDB.
* Uses Gemini Embeddings for semantic similarity search.
* Retrieves only the most relevant professor profiles before generating responses.

---

# 🏗️ Project Architecture

```text
                User Query
                     │
                     ▼
              LangGraph Router
                     │
     ┌──────────┬───────────┬────────────┬──────────────┐
     ▼          ▼           ▼            ▼
Student     Professor    Research   Collaboration
 Tool          Tool         Tool          Tool
     │          │            │             │
     └──────────┴────────────┴─────────────┘
                     │
                     ▼
              Gemini 2.5 Flash
                     │
                     ▼
               Final Response
```

---

# 🛠️ Tech Stack

* Python
* Google Gemini API
* Gemini Embeddings
* ChromaDB
* LangGraph
* LangChain
* Tavily Search API
* python-dotenv

---

# 📂 Project Structure

```text
LLM_Hackathon/
│
├── main.py
├── graph.py
├── config.py
├── student_tools.py
├── professor_tools.py
├── collaboration_tools.py
├── web_tools.py
├── confirmation_tools.py
│
├── professor1.txt
├── professor2.txt
...
├── professor16.txt
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd LLM_Hackathon
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
GEMINI_KEY=YOUR_GEMINI_API_KEY
TAVILY_API_KEY=YOUR_TAVILY_API_KEY
```

Run the project:

```bash
python main.py
```

---

# 💬 Example Queries

### Faculty Recommendation

* I am interested in Artificial Intelligence. Which professor should I approach?
* Suggest professors working on Machine Learning and Robotics.
* Who would be a good research supervisor for NLP?

### Professor Information

* Tell me about Dr. Ananya Sharma.
* What are Dr. Rahul Iyer's research interests?
* Which courses does Dr. Priya Nair teach?

### Research Trends

* What are the latest trends in Explainable AI?
* Tell me about current research in Quantum Computing.
* What's new in Computer Vision?

### Collaboration

* Suggest professors who can collaborate on Healthcare AI.
* Which faculty members should work together on Robotics and IoT?
* Recommend an interdisciplinary research team.

---

# 📈 Future Enhancements

* Multi-turn conversational memory
* Real-time faculty database integration
* PDF publication retrieval
* Student profile personalization
* Voice-enabled assistant
* Web dashboard deployment

---

# 👥 Team
- B.Ravichandra Raj
- N.sartak
Developed as part of the LLM Hackathon.

## 🙏 Acknowledgements

This project was developed using the following open-source libraries and APIs:

* **Google Gemini API & Google GenAI Python SDK** – Used for text generation and embedding generation.
* **ChromaDB** – Used as the vector database for storing and retrieving professor profile embeddings.
* **LangGraph** – Used to build the AI agent workflow and tool routing.
* **LangChain Core** – Used alongside LangGraph for workflow components.
* **Tavily Search API** – Used to retrieve up-to-date research information from the web.
* **python-dotenv** – Used for securely loading API keys from environment variables.
* **Pydantic** – Used for structured output parsing and data validation.

We thank the developers and maintainers of these open-source projects for making them available to the community.

Thank you for checking out our project!
