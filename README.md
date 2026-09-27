# 🛡️ DataTrace AI — Enterprise AI Decision Engine for Business Data

> **Problem Statement 4:** AI Decision Engine for Business Data  
> **Submission Title:** An AI decision engine that converts business data into traceable insights and verified actions.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B.svg)](https://streamlit.io/)
[![DuckDB](https://img.shields.io/badge/DuckDB-0.9%2B-FFF000.svg)](https://duckdb.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📌 Executive Summary

Traditional Business Intelligence (BI) dashboards show **what happened** (e.g., *"Sales dropped 12% in August"*), but fail to explain **why** or recommend **what to do next**. On the other hand, standard AI tools act as "black boxes" that frequently hallucinate metrics without data provenance.

**DataTrace AI** bridges this gap:
1. **Deterministic Analytics:** Queries local structured data via an in-memory DuckDB engine.
2. **100% Data Lineage:** Maps every metric back to exact database record IDs to guarantee zero LLM hallucinations.
3. **Action Recommendation Matrix:** Transforms raw data findings into ranked, risk-evaluated business strategies.
4. **Human-in-the-Loop Gateway:** Requires explicit human approval before executing high-impact workflows.

---

## 🏗️ System Architecture

```text
[ Business Data (CSV / DuckDB) ]
               │
               ▼
┌────────────────────────────────────────────────────────┐
│  1. Text-to-SQL / Query Engine                         │
│  • Executes deterministic SQL queries on DuckDB        │
│  • Performs fast in-memory aggregation                 │
└────────────────────────┬───────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────┐
│  2. Data Lineage & Traceability Auditor                │
│  • Captures exact Row IDs and provenance logs          │
│  • Eliminates black-box AI hallucinations              │
└────────────────────────┬───────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────┐
│  3. Strategy & Decision Matrix                         │
│  • Calculates expected ROI, risk profile, & confidence │
│  • Ranks action choices for business leaders           │
└────────────────────────┬───────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────┐
│  4. Multi-Page Enterprise Dashboard                    │
│  • Executive Console & Interactive Visuals             │
│  • Lineage Audit Trail Modal                           │
│  • Human Approval Gateway & Webhook Triggers           │
│  • Real-Time Diagnostic Test Suite (`eval.py`)        │
└────────────────────────────────────────────────────────┘
```
**Key Features**
Executive AI Console: Ask questions in natural language and receive verified root-cause analysis with high-contrast Plotly visual models.

Traceability & Audit Trail: Full auditability displaying executed SQL code alongside row-level database logs.

Action Recommendation Cards: Auto-generated strategic recommendations complete with estimated ROI (in ₹ INR), risk profile (Low/Medium/High), and confidence scoring.

Human-in-the-Loop Approval: Interactive triggers for business managers to review and execute decisions safely.

Automated Diagnostic Suite: Built-in test harness verifying DuckDB query validity, schema integrity, and lineage precision.

## 📂 Repository Structure

```text
datatrace-ai/
├── .streamlit/
│   └── config.toml                  # Global SaaS Light Theme Configuration
├── pages/
│   ├── 1_📊_Data_Lineage_&_Audit.py  # Row-level verification & audit trail
│   ├── 2_🚀_Decision_Matrix.py        # Strategy simulation & approval gateway
│   └── 3_⚙️_System_Diagnostics.py   # Live diagnostic suite for judges
├── app.py                           # Main Executive Console
├── engine.py                        # Core Analytics Engine & DuckDB Integration
├── eval.py                          # Automated Test Suite script
├── synthetic_data.csv               # Auto-generated dataset (created on first run)
├── requirements.txt                 # Project Dependencies
└── README.md                        # Documentation
```
## 🚀 Quick Start & Installation
Prerequisites
Python 3.10 or higher

Git

Step-by-Step Local Setup
Clone the Repository:

Bash
git clone [https://github.com/damasvasree/datatrace-ai.git](https://github.com/damasvasree/datatrace-ai.git)
cd datatrace-ai
Create a Virtual Environment (Optional but recommended):

Bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Install Dependencies:

Bash
pip install -r requirements.txt
Run the Diagnostic Test Suite:

Bash
python eval.py
Launch the Web Application:

Bash
streamlit run app.py
Open your browser at http://localhost:8501.

🧪 Testing & Reliability
The application includes an automated diagnostic suite (eval.py) that tests core system functionality:

Bash
python eval.py
Expected Output:

Plaintext
========================================
Running DataTrace AI Diagnostic Test Suite
========================================
[TEST 1] Testing DuckDB Execution...
  --> Passed: Engine correctly queried DuckDB local store.
[TEST 2] Testing Traceability Lineage...
  --> Passed: Lineage verified for data rows.
[TEST 3] Testing Recommendation Matrix...
  --> Passed: Decision framework correctly generated.

ALL TESTS PASSED: System is 100% Ready for Submission!

## 🛠️ Technology Stack
Frontend & UI: Streamlit (Custom Light Theme CSS, Plotly Data Visualizations)

Analytical Engine: DuckDB (In-memory SQL analytics)

Data Processing: Pandas, NumPy

LLM Integration: OpenAI GPT-4o-mini (Text-to-SQL query generation with deterministic fallbacks)

Testing: Custom Pydantic & Python Assert diagnostic suite

---

## 👨‍💻 Author

**Damasvasree N** ([@damasvasree](https://github.com/damasvasree))  
💡 *Passionate about AI, Data Analytics & Enterprise Decision Systems*

---

## 📌 Conclusion

**DataTrace AI** is not just a hackathon project — it is a future-ready enterprise decision framework designed to eliminate LLM hallucinations, make business analytics fully auditable, and empower leaders with verifiable, risk-evaluated actions.

⭐ **If you like this project, give it a star on GitHub!**
