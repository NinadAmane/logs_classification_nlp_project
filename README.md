# 🧠 Log Classification with Hybrid Classification Framework

A production-inspired hybrid log classification system that intelligently combines **Rule-Based Logic**, **Traditional ML**, and **Large Language Models (LLMs)** to handle logs of varying complexity and structure.

---

## 🚀 Overview

This project implements a **three-layer hybrid architecture** to classify system logs efficiently:

1. **Regex Layer** → Fast & deterministic rule-based filtering
2. **Sentence Transformer + Logistic Regression (BERT Layer)** → Structured ML-based semantic classification
3. **LLM Layer (Groq + Llama 3.3)** → Intelligent reasoning for complex and legacy log patterns

The system dynamically routes logs based on their source and complexity.

---

## 🏗️ Hybrid Classification Strategy

### 1️⃣ Regular Expression (Regex)

- Handles predictable and well-structured patterns.
- Ideal for:
  - `User Action`
  - `System Notification`
- Fast and explainable.
- Used as the first classification layer for non-legacy systems.

---

### 2️⃣ Sentence Transformer + Logistic Regression (BERT)

- Uses `all-MiniLM-L6-v2` for embedding generation.
- Applies a pre-trained Logistic Regression classifier.
- Handles complex patterns when labeled training data exists.
- Used as fallback when Regex does not classify.

---

### 3️⃣ LLM (Groq + Llama 3.3-70B)

- Used for ambiguous or poorly structured logs.
- Specifically routed for `LegacyCRM` source logs.
- Classifies into:
  - `Workflow Error`
  - `Deprecation Warning`
  - `Unclassified`

This enables intelligent reasoning where rule-based and traditional ML fall short.

---

## 📁 Project Structure

```
├── models/
│   └── log_classifier.joblib
├── resources/
│   ├── output.csv
│   └── test.csv
├── training/
│   ├── dataset/
│   │   └── synthetic_logs.csv
│   └── training.ipynb
├── .gitignore
├── classify.py
├── processor_bert.py
├── processor_llm.py
├── processor_regex.py
├── requirements.txt
└── server.py
```

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies

Make sure Python is installed (recommended: Python 3.11).

```bash
pip install -r requirements.txt
```

⚠️ **Important:** Ensure you have a `.env` file configured with:

```
GROQ_API_KEY=your_api_key_here
```

### 2️⃣ Run the FastAPI Server

```bash
python -m uvicorn server:app --reload
```

Once running, access:

- **API Base:** `http://127.0.0.1:8000/`
- **Swagger Docs:** `http://127.0.0.1:8000/docs`

## 📊 Usage

Upload a CSV file to the `/classify/` endpoint.

### Required CSV Format

| source    | log_message |
| --------- | ----------- |
| ModernCRM | ...         |
| LegacyCRM | ...         |

### Routing Logic

- **LegacyCRM** → LLM
- **Others** → Regex → (if no match) → BERT

## 📝 Output

The system returns a processed CSV file containing:

- `source`
- `log_message`
- `target_label`

### Example Output

| source    | log_message | target_label   |
| --------- | ----------- | -------------- |
| ModernCRM | ...         | User Action    |
| LegacyCRM | ...         | Workflow Error |

## 🧠 Architectural Highlights

- ⚡ **Hybrid Pipeline:** Integrates Deterministic (Regex), ML (BERT), and Generative AI (LLM)
- 🧩 **Source-based routing:** Logic specifically handles legacy vs. modern system logs
- 🧠 **Semantic fallback:** Uses embedding-based classification when rules fail
- 🤖 **LLM reasoning:** Leverages Groq for complex edge cases
- 🚀 **API-ready:** Built with FastAPI for easy integration

## 🔒 Notes

- **Do NOT commit:** `.env`, `venv/`, or large model files
- **Compatibility:** Ensure `scikit-learn` version matches the training version when loading models
- **Connectivity:** LLM calls require internet access and a valid Groq API key

## 💡 Future Improvements

- Confidence scoring aggregation across layers
- Batch LLM inference
- Model caching
- Monitoring & logging layer
- Dockerized deployment

## 👨‍💻 Author

**Ninad Amane** | [LinkedIn](https://www.linkedin.com/in/ninad-amane/) | [Email](ninadamane@gmail.com)
