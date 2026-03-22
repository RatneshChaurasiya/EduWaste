import streamlit as st


def render():
    # ── Hero Section ─────────────────────────────────────────
    import os
    import base64
    logo_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "logo.png")
    
    logo_html = "♻️"
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as f:
            encoded_string = base64.b64encode(f.read()).decode()
            logo_html = f'<img src="data:image/png;base64,{encoded_string}" style="height: 2.2em; vertical-align: middle; margin-right: 15px;">'

    st.markdown(
        f"""
        <style>
        @keyframes blinker {{
            50% {{ opacity: 0; }}
        }}
        .cert-blink {{
            animation: blinker 1.5s linear infinite;
            color: red !important;
            font-weight: bold !important;
            margin-top: 10px;
        }}
        </style>
        <div class="hero-section animate-in">
            <h1>{logo_html} EduWaste</h1>
            <p>Educate · Engage · Empower — Building a cleaner, greener future together</p>
            <p class="cert-blink">Complete the quiz and survey to generate the certificate</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Take the Quiz Button ────────────────────────────────
    col_left, col_center, col_right = st.columns([1, 1, 1])
    with col_center:
        if st.button("🚀 Take the Quiz", use_container_width=True):
            st.session_state["quiz_nav"] = True
            st.rerun()

    # ── Quick Stats ──────────────────────────────────────────
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(
            '<div class="stat-box"><div class="stat-number">3</div>'
            '<div class="stat-label">Waste Categories</div></div>',
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            '<div class="stat-box"><div class="stat-number">10</div>'
            '<div class="stat-label">Quiz Questions</div></div>',
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            '<div class="stat-box"><div class="stat-number">5+</div>'
            '<div class="stat-label">Best Practices</div></div>',
            unsafe_allow_html=True,
        )
    with col4:
        st.markdown(
            '<div class="stat-box"><div class="stat-number">📊</div>'
            '<div class="stat-label">Live Dashboard</div></div>',
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── What You'll Discover ─────────────────────────────────
    st.markdown("## 🌍 What You'll Discover")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            """
            <div class="info-card animate-in">
                <h4>📚 Learn</h4>
                <p>Understand waste segregation, environmental impact, and best practices for a sustainable lifestyle.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="info-card animate-in">
                <h4>❓ Test Yourself</h4>
                <p>Take our interactive quiz to challenge your waste management knowledge and earn badges!</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """
            <div class="info-card animate-in">
                <h4>📊 See Impact</h4>
                <p>View real-time community data on the dashboard and track collective awareness growth.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── How It Works ─────────────────────────────────────────
    st.markdown("## 🔄 How It Works")
    st.markdown(
        """
        <div class="info-card animate-in">
            <ol style="color: #444444; line-height: 2;">
                <li><strong>Learn</strong> — Browse the <em>Awareness</em> module to understand waste categories and best practices.</li>
                <li><strong>Quiz</strong> — Test your knowledge with 10 multiple-choice questions and earn a badge.</li>
                <li><strong>Survey</strong> — Share your waste management habits to contribute to our community dataset.</li>
                <li><strong>Dashboard</strong> — Explore charts and statistics built from real survey responses.</li>
            </ol>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── CTA ──────────────────────────────────────────────────
    st.markdown("### 🚀 Ready to get started?")
    st.info("👈 Use the **sidebar** to navigate between modules — start with **📚 Awareness**!")
