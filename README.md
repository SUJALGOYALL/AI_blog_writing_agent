# 🧠 AI Blog Writing Agent

An end-to-end **AI-powered blog generation system** built using **LangGraph**, **LangChain**, **Groq LLMs**, and **Streamlit**.

This project autonomously:
- plans a blog structure,
- performs web research when required,
- writes each section using independent agents,
- optionally generates diagrams/images,
- and presents everything through a rich Streamlit interface.

---
## 🎥 Demo – UI Walkthrough


https://github.com/user-attachments/assets/fa837115-aa4f-4cc8-a077-ed7da4834112



## 🚀 Key Features

### ✍️ Intelligent Blog Generation
- Generates structured, high-quality blogs automatically
- Supports multiple blog types:
  - Explainer
  - Tutorial
  - Comparison
  - System Design
  - News Roundup

### 🧠 LangGraph-Based Multi-Agent Architecture
- Graph-based execution using **LangGraph**
- Modular node-based design:
  - Router
  - Research
  - Orchestrator (Planner)
  - Workers (Section Writers)
  - Reducer (Merge + Images)

### 🔎 Smart Research Routing
- Decides *before planning* whether research is needed
- Uses **Tavily Search API** only when required
- Supports:
  - closed_book – no research
  - hybrid – partial research
  - open_book – news / volatile topics

### 🧩 Parallel Section Writing
- Each section is written by an independent worker agent
- Enforces:
  - bullet order
  - target word count
  - citation rules
- Supports minimal code snippets when needed

### 🖼️ Automatic Image / Diagram Generation
- Decides whether images improve understanding
- Inserts placeholders like [[IMAGE_1]]
- Generates images using **A4F Image API**
- Saves images locally and embeds them into Markdown

### 🖥️ Streamlit Frontend
- Live graph execution status
- Node-by-node progress view
- Markdown preview with local images
- Download options:
  - Markdown only
  - Markdown + images bundle
- Load and view previously generated blogs

---

## 📂 Project Structure

```
AI_BLOG_WRITING_AGENT/
│
├── frontend.py
├── app.py
├── config.py
├── schemas.py
├── prompts.py
├── requirements.txt
├── .env
│
├── nodes/
│   ├── router.py
│   ├── research.py
│   ├── orchestrator.py
│   ├── worker.py
│   └── reducer.py
│
├── services/
│   ├── tavily.py
│   └── image-gen.py
│
├── images/
└── __init__.py
```

---

## 🔄 Workflow

User Topic → Router → Research (if needed) → Orchestrator → Workers → Reducer → Final Blog

---
## 🧠 LangGraph Node Graphs (Execution Flow)

This project uses **LangGraph** to orchestrate a deterministic, multi-agent workflow.  
The system is composed of **two graphs**:

---


## 🔷 Main Agent Graph
<img width="160" height="630" alt="image" src="https://github.com/user-attachments/assets/fad4c63f-fe73-4d20-bffb-298fff1ed335" />



### Node Summary
- **router** – Decides whether web research is required (`closed_book`, `hybrid`, `open_book`)
- **research** – Fetches and deduplicates sources using Tavily (conditional)
- **orchestrator** – Creates the full blog plan (sections, goals, word limits)
- **worker** – Writes each section independently
- **reducer** – Merges sections and triggers post-processing

---

## 🔷 Reducer Subgraph (Post-Processing)
<img width="252" height="432" alt="image" src="https://github.com/user-attachments/assets/184f6cd1-75da-4833-83eb-087fa58b5244" />



### Reducer Responsibilities
- **merge_content** – Orders and merges all sections into a single Markdown file
- **decide_images** – Determines if diagrams improve understanding and inserts placeholders
- **generate_and_place_images** – Generates images, saves them locally, and embeds them into Markdown

---

## ✅ Why This Design
- Modular and debuggable
- Avoids unnecessary API calls
- Scales cleanly with more agents
- Separates reasoning, writing, and rendering stages




## ⚙️ Installation & Usage

### Clone Repository
```bash
git clone https://github.com/SUJALGOYALL/AI_BLOG_WRITING_AGENT.git
cd AI_BLOG_WRITING_AGENT
```

### Setup Environment
```bash
python -m venv env
env\Scripts\activate  # Windows
# or
source env/bin/activate  # Mac/Linux
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Application
```bash
streamlit run frontend.py
```

---

## 🔐 Environment Variables (.env)

```
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
A4F_API_KEY=your_image_api_key
```

---

## ⚠️ Notes
- Groq has token-per-minute limits; retries are recommended.
- Use smaller models for development to avoid rate limits.

---

## 📜 License
Open-source, for educational and research purposes.

---

## ⭐ Author
###     Sujal Goyal
- Passionate AI Engineer
- (IIIT Bhagalpur)
- Built with ❤️ using LangGraph and Streamlit.
