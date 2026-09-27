import streamlit as st

st.set_page_config(page_title="Decision Matrix", page_icon="🚀", layout="wide")

# Global Light Theme CSS
st.markdown("""
    <style>
    .stApp { background-color: #F8FAFC; color: #0F172A; }
    section[data-testid="stSidebar"] { background-color: #1E293B !important; }
    section[data-testid="stSidebar"] * { color: #F8FAFC !important; }
    .stButton>button {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Branding
st.sidebar.markdown("### 🛡️ **DataTrace AI**")
st.sidebar.caption("Enterprise Decision Engine v2.4")

st.title("🚀 Action Recommendation & Approval Matrix")
st.caption("Human-in-the-loop approval gateway for high-impact enterprise actions.")
st.markdown("---")

if "analysis" not in st.session_state:
    st.warning("Please run an analysis on the Executive Console (app) first.")
    st.stop()

res = st.session_state["analysis"]

for idx, dec in enumerate(res["decisions"]):
    with st.container(border=True):
        c1, c2, c3 = st.columns([3, 2, 1])
        with c1:
            st.markdown(f"### {dec['option']} `{dec['id']}`")
            st.write(dec['action'])
        with c2:
            st.markdown(f"**Expected ROI:** `{dec['roi']}`")
            st.markdown(f"**Risk Profile:** `{dec['risk']}` | **Confidence:** `{dec['confidence']}`")
        with c3:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button(f"Approve Action", key=f"btn_page_{idx}", type="primary"):
                st.toast(f"✅ Approved {dec['id']}! Webhook triggered.", icon="🚀")
                st.success(f"Status: Executed")