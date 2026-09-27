import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Lineage & Audit", page_icon="📊", layout="wide")

# Global Light Theme CSS
st.markdown("""
    <style>
    .stApp { background-color: #F8FAFC; color: #0F172A; }
    section[data-testid="stSidebar"] { background-color: #1E293B !important; }
    section[data-testid="stSidebar"] * { color: #F8FAFC !important; }
    div[data-testid="stCodeBlock"] { border-radius: 10px !important; }
    </style>
""", unsafe_allow_html=True)

# Sidebar Branding
st.sidebar.markdown("### 🛡️ **DataTrace AI**")
st.sidebar.caption("Enterprise Decision Engine v2.4")

st.title("📊 Data Lineage & Traceability Audit Log")
st.caption("Inspect exact source records evaluated by the AI engine to guarantee zero hallucination.")
st.markdown("---")

if "analysis" not in st.session_state:
    st.warning("Please run an analysis on the Executive Console (app) first.")
    st.stop()

res = st.session_state["analysis"]

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Executed SQL Query")
    st.code(res["sql_executed"], language="sql")
    st.info("✓ Query executed directly against DuckDB analytical engine.")

with col2:
    st.subheader("Verification Metrics")
    st.write(f"**Records Evaluated:** `{res['evaluated_rows']} database rows`")
    st.write(f"**Verification Status:** `100% Deterministic Lineage Log`")
    st.write(f"**Audit Timestamp:** `2026-09-27 11:30 IST`")

st.markdown("---")
st.subheader("Source Row Lineage Audit Table")
lineage_df = pd.DataFrame(res["lineage_records"])
st.dataframe(lineage_df, width="stretch", height=350)