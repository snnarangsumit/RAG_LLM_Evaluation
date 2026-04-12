# RAG LLM Evaluation Framework

A Python-based test automation framework for evaluating **Retrieval-Augmented Generation (RAG)** pipelines using [RAGAS](https://docs.ragas.io/) metrics and GPT-4. Built with `pytest`, `LangChain`, and `python-dotenv` for secure, scalable LLM quality assessment.

---

## 🧠 What This Project Does

This framework sends questions to a live RAG API endpoint and evaluates the quality of its responses using industry-standard RAGAS metrics. It measures how well the RAG system retrieves relevant context and generates accurate answers — critical for validating AI-powered applications in production.

---

## 📁 Project Structure

```
RAG_LLM_Evaluation/
│
├── Test1.py              # Context Precision (without reference)
├── Test2.py              # Context Recall (with reference answer)
├── Test3_framework.py    # Parametrized Context Recall using test data factory
├── Test4.py              # Additional RAGAS metric evaluation
├── Test5.py              # Additional RAGAS metric evaluation
├── Test6.py              # Additional RAGAS metric evaluation
├── Test7.py              # Additional RAGAS metric evaluation
├── conftest.py           # Shared pytest fixtures (LLM wrapper)
├── testDataFactory.py    # Synthetic test data generation using RAGAS TestsetGenerator
├── utils.py              # Helper functions (API calls, test data loading)
├── pytest.ini            # Pytest configuration
├── requirements.txt      # Project dependencies
├── testdata/             # Test data files (JSON/YAML)
└── .env                  # API keys (not committed — see setup below)
```

---

## 📊 RAGAS Metrics Covered

| Test File | Metric | Description |
|---|---|---|
| `Test1.py` | **Context Precision** | Are retrieved docs relevant to the question? |
| `Test2.py` | **Context Recall** | Do retrieved docs cover the reference answer? |
| `Test3_framework.py` | **Context Recall (Parametrized)** | Data-driven recall tests across multiple questions |

---

## ⚙️ Tech Stack

- **Python** 3.8+
- **pytest** + **pytest-asyncio** — async test execution
- **RAGAS** — LLM evaluation metrics
- **LangChain** + **LangChain-OpenAI** — LLM and embedding wrappers
- **OpenAI GPT-4** — evaluation model
- **python-dotenv** — secure API key management
- **requests** — RAG API integration

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/snnarangsumit/RAG_LLM_Evaluation.git
cd RAG_LLM_Evaluation
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your-openai-api-key-here
RAGAS_APP_TOKEN=your-ragas-token-here
DOCS_PATH=./testdata
NLTK_DATA_PATH=./nltk_data
```

> ⚠️ Never commit your `.env` file. It is listed in `.gitignore`.

### 4. Run the tests
```bash
# Run all tests
pytest

# Run a specific test
pytest Test1.py -v

# Run with detailed output
pytest -v --tb=short
```

---

## 🔐 Security

- All API keys are loaded via `.env` using `python-dotenv`
- No secrets are hardcoded in any source file
- `.env`, `__pycache__/`, and `.idea/` are excluded via `.gitignore`

---

## 📌 Key Concepts

**RAG (Retrieval-Augmented Generation)** — An AI architecture that retrieves relevant documents from a knowledge base before generating an answer, improving factual accuracy.

**RAGAS** — An open-source framework for evaluating RAG pipelines using metrics like Context Precision, Context Recall, Faithfulness, and Answer Relevancy.

---

## 👤 Author

**Sumit Narang**  
Senior QA Engineer | Test Automation | AI/LLM Testing | PSMI | PSPO I  
[GitHub](https://github.com/snnarangsumit) • [LinkedIn](https://linkedin.com/in/your-profile)
