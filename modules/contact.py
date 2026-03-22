import streamlit as st


def render():
    st.markdown("# 📬 Contact")
    st.markdown("*Get in touch with the developer — let's build a cleaner future together!*")
    st.markdown("---")

    # ── Developer Card ───────────────────────────────────────
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown(
            """
            <div class="stat-box" style="padding: 2rem;">
                <div class="stat-number">👨‍💻</div>
                <div class="stat-label" style="font-size:1.15rem; margin-top:0.8rem;">
                    <strong>Ratnesh Chaurasiya</strong>
                </div>
                <div class="stat-label">Developer & Researcher</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="info-card animate-in">
                <h4>🌍 About EduWaste</h4>
                <p>
                    <strong>EduWaste</strong> is a digital platform built to educate communities 
                    about proper waste management, test their knowledge through interactive quizzes, 
                    collect real-time awareness data via surveys, and visualize community impact 
                    through interactive dashboards.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # ── Contact Buttons ──────────────────────────────────────
    st.markdown("## 📨 Connect With Me")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            <a href="mailto:ratnesh1930@gmail.com" style="text-decoration:none;">
                <div class="info-card animate-in" style="text-align:center; cursor:pointer; padding:2rem 1rem;">
                    <div style="margin-bottom:12px;">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="56" height="56">
                            <path fill="#EA4335" d="M24 24L6 12V36c0 2.2 1.8 4 4 4h28c2.2 0 4-1.8 4-4V12L24 24z"/>
                            <path fill="#4285F4" d="M42 12L24 24 6 12V8c0-2.2 1.8-4 4-4h28c2.2 0 4 1.8 4 4v4z"/>
                            <path fill="#34A853" d="M6 12v2l18 12 18-12v-2L24 22 6 12z" opacity=".5"/>
                        </svg>
                    </div>
                    <h4 style="margin:0 0 6px 0; color:#EA4335;">Gmail</h4>
                    <p style="color:#555; font-weight:600; font-size:0.9rem; margin:0;">ratnesh1930@gmail.com</p>
                </div>
            </a>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
            <a href="https://www.linkedin.com/in/ratneshchaurasiya/" target="_blank" style="text-decoration:none;">
                <div class="info-card animate-in" style="text-align:center; cursor:pointer; padding:2rem 1rem;">
                    <div style="margin-bottom:12px;">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="56" height="56">
                            <rect fill="#0A66C2" x="2" y="2" width="44" height="44" rx="6"/>
                            <path fill="#fff" d="M14.5 17.5h-4v14h4v-14zM12.5 15.5c1.4 0 2.5-1.1 2.5-2.5s-1.1-2.5-2.5-2.5S10 11.6 10 13s1.1 2.5 2.5 2.5zM36 31.5c0-4.4-2.6-6.5-5.5-6.5-2.2 0-3.5 1.2-4 2.1v-1.6h-4v14h4v-7.8c0-2.1 1-3.2 2.7-3.2 1.5 0 2.8 1 2.8 3.1v7.9h4V31.5z"/>
                        </svg>
                    </div>
                    <h4 style="margin:0 0 6px 0; color:#0A66C2;">LinkedIn</h4>
                    <p style="color:#555; font-weight:600; font-size:0.9rem; margin:0;">Ratnesh Chaurasiya</p>
                </div>
            </a>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            """
            <a href="https://www.instagram.com/lavleshh_/" target="_blank" style="text-decoration:none;">
                <div class="info-card animate-in" style="text-align:center; cursor:pointer; padding:2rem 1rem;">
                    <div style="margin-bottom:12px;">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="56" height="56">
                            <defs>
                                <linearGradient id="ig" x1="0%" y1="100%" x2="100%" y2="0%">
                                    <stop offset="0%" style="stop-color:#feda75"/>
                                    <stop offset="20%" style="stop-color:#fa7e1e"/>
                                    <stop offset="45%" style="stop-color:#d62976"/>
                                    <stop offset="70%" style="stop-color:#962fbf"/>
                                    <stop offset="100%" style="stop-color:#4f5bd5"/>
                                </linearGradient>
                            </defs>
                            <rect fill="url(#ig)" x="2" y="2" width="44" height="44" rx="12"/>
                            <circle cx="24" cy="24" r="8" fill="none" stroke="#fff" stroke-width="3"/>
                            <circle cx="35" cy="13" r="2.2" fill="#fff"/>
                            <rect x="8" y="8" width="32" height="32" rx="8" fill="none" stroke="#fff" stroke-width="3"/>
                        </svg>
                    </div>
                    <h4 style="margin:0 0 6px 0; color:#d62976;">Instagram</h4>
                    <p style="color:#555; font-weight:600; font-size:0.9rem; margin:0;">@lavleshh_</p>
                </div>
            </a>
            """,
            unsafe_allow_html=True,
        )

