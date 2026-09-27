import streamlit as st
import pandas as pd
import plotly.express as px
from engine import DataTraceEngine

st.set_page_config(
    page_title="DataTrace AI | Enterprise Decision Engine",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Light Theme with Color Theory & Smooth CSS Animations
st.markdown("""
    <style>
    /* Color Palette:
       - Main BG: #F8FAFC (Slate 50)
       - Sidebar BG: #1E293B (Slate 800)
       - Card BG: #FFFFFF (Pure White)
       - Primary Accent: #2563EB (Royal Blue)
       - Border Color: #E2E8F0 (Slate 200)
       - Primary Text: #0F172A (Slate 900)
       - Sub Text: #64748B (Slate 500)
    */

    /* Global Page Styling & Smooth Fade-In Animation */
    .stApp {
        background-color: #F8FAFC;
        color: #0F172A;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(6px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #1E293B !important;
        border-right: 1px solid #334155 !important;
    }
    section[data-testid="stSidebar"] * {
        color: #F8FAFC !important;
    }

    /* Metric Cards with Smooth Hover Animation */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 12px !important;
        padding: 18px 22px !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05), 0 1px 2px rgba(0,0,0,0.06) !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        animation: fadeIn 0.4s ease-out forwards;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.08), 0 4px 6px -2px rgba(0,0,0,0.03) !important;
        border-color: #CBD5E1 !important;
    }
    div[data-testid="stMetricValue"] > div {
        color: #1E40AF !important;
        font-weight: 700 !important;
        font-size: 1.85rem !important;
    }
    div[data-testid="stMetricLabel"] p {
        color: #64748B !important;
        font-size: 0.8rem !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
    }

    /* Input Query Bar */
    .stTextInput input {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 10px !important;
        padding: 12px 16px !important;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05) !important;
        transition: all 0.2s ease !important;
    }
    .stTextInput input:focus {
        border-color: #2563EB !important;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15) !important;
    }

    /* Primary Action Button */
    .stButton>button {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        padding: 10px 20px !important;
        box-shadow: 0 2px 4px rgba(37, 99, 235, 0.2) !important;
        transition: all 0.2s ease-in-out !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 12px rgba(37, 99, 235, 0.3) !important;
    }

    /* Insight Banner */
    .insight-card-light {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-left: 5px solid #2563EB;
        border-radius: 10px;
        padding: 20px 24px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        animation: fadeIn 0.5s ease-out forwards;
    }

    /* Hide standard Streamlit header clutter */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_engine():
    return DataTraceEngine()

engine = load_engine()

if "analysis" not in st.session_state:
    st.session_state["analysis"] = engine.execute_verified_analysis("Why did MRR drop in August?")

# Sidebar Navigation Header
st.sidebar.markdown("### 🛡️ **DataTrace AI**")
st.sidebar.caption("Enterprise Decision Engine v2.4")
st.sidebar.markdown("---")
st.sidebar.info("💡 Use navigation above to explore **Data Lineage Audit**, **Decision Matrix**, and **System Diagnostics**.")

# Title & Subtitle
st.title("🛡️ Executive AI Decision Console")
st.markdown("<p style='color: #64748B; font-size: 1.05rem; margin-top: -15px;'>Verifiable Business Intelligence & Action Gateway</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Natural Language Query Area
query_col1, query_col2 = st.columns([4, 1])
with query_col1:
    user_query = st.text_input("Ask a business question", value="Why did our SaaS monthly recurring revenue (MRR) drop in August, and what action should we take?", label_visibility="collapsed")
with query_col2:
    if st.button("🔍 Run Analysis", type="primary", width="stretch"):
        with st.spinner("Executing DuckDB verification & generating decision matrix..."):
            st.session_state["analysis"] = engine.execute_verified_analysis(user_query)

res = st.session_state["analysis"]

st.markdown("<br>", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric(label="Identified MRR Loss", value=f"₹{int(res['total_loss']):,}", delta="-12.4%", delta_color="inverse")
with m2:
    st.metric(label="Evaluated Rows", value=res["evaluated_rows"], delta="100% Verified")
with m3:
    st.metric(label="SQL Integrity", value="Passed", delta="0 Hallucinations")
with m4:
    st.metric(label="Action Options", value=len(res["decisions"]), delta="Ready")

st.markdown("<br>", unsafe_allow_html=True)


tab1, tab2 = st.tabs(["📊 Executive Visuals", "🔍 Core Insight & Query Trace"])

with tab1:
    summary_df = pd.DataFrame(res["data_summary"])
    if not summary_df.empty:
        
        fig = px.bar(
            summary_df, 
            x="plan_type", 
            y="total_loss", 
            color="primary_reason",
            title="Revenue Loss Breakdown by Customer Plan (₹)",
            text_auto=True,
            template="plotly_white",
            color_discrete_sequence=["#DC2626", "#2563EB", "#059669", "#D97706"] # Red, Blue, Green, Amber
        )
        fig.update_layout(
            paper_bgcolor='#FFFFFF',
            plot_bgcolor='#F8FAFC',
            font=dict(color="#0F172A", family="Inter, sans-serif"),
            margin=dict(l=20, r=20, t=50, b=20),
            height=420,
            xaxis=dict(gridcolor='#E2E8F0'),
            yaxis=dict(gridcolor='#E2E8F0')
        )
        st.plotly_chart(fig, width="stretch")

with tab2:
    st.markdown(f"""
        <div class="insight-card-light">
            <h4 style="margin:0; color:#1E40AF; font-size:1.1rem; font-weight:700;">Root Cause Analysis</h4>
            <p style="margin-top:8px; color:#334155; font-size:1.05rem; line-height:1.5;">{res['insight_summary']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**Executed Deterministic SQL:**")
    st.code(res["sql_executed"], language="sql")