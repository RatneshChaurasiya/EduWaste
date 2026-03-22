import streamlit as st
import os

# ── Page Config ──────────────────────────────────────────────
st.set_page_config(
    page_title="EduWaste — Waste Management Awareness",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Load Custom CSS ──────────────────────────────────────────
css_path = os.path.join(os.path.dirname(__file__), "style.css")
if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ── Import Pages ─────────────────────────────────────────────
from modules import home, awareness, quiz, survey, dashboard, contact, about

# ── Sidebar Navigation ──────────────────────────────────────
import base64
logo_path = os.path.join(os.path.dirname(__file__), "data", "logo.png")
if os.path.exists(logo_path):
    with open(logo_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.sidebar.markdown(
        f"""
        <div style="text-align: center; margin-bottom: 20px;">
            <a href="/" target="_self" title="Go to Home Page">
                <img src="data:image/png;base64,{encoded}" style="width: 110px; cursor: pointer; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
st.sidebar.markdown("## ♻️ Navigation")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "📚 Awareness", "❓ Quiz", "📝 Survey", "📊 Dashboard", "📬 Contact", "ℹ️ About"],
    label_visibility="collapsed",
)

# ── Handle "Take the Quiz" button redirect ───────────────────
if st.session_state.pop("quiz_nav", False):
    page = "❓ Quiz"

# ── Route to Page ────────────────────────────────────────────
if page == "🏠 Home":
    home.render()
elif page == "📚 Awareness":
    awareness.render()
elif page == "❓ Quiz":
    quiz.render()
elif page == "📝 Survey":
    survey.render()
elif page == "📊 Dashboard":
    dashboard.render()
elif page == "📬 Contact":
    contact.render()
elif page == "ℹ️ About":
    about.render()

# ── Footer ───────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    '<div class="footer">© 2026 EduWaste · '
    'Built by <strong>Ratnesh Chaurasiya</strong></div>',
    unsafe_allow_html=True,
)
