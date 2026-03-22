import streamlit as st


def render():
    st.markdown("# ℹ️ About This Project")
    st.markdown("---")

    # ── Project Overview ─────────────────────────────────────
    st.markdown(
        """
        <div class="info-card animate-in">
            <h4>🎯 Project Overview</h4>
            <p>
                The <strong>Waste Management Awareness System</strong> is a digital platform 
                built to educate communities about proper waste management, test their knowledge, 
                collect real-time awareness data through surveys, and visualize community impact 
                through interactive dashboards.
            </p>
            <p>
                The platform covers <strong>waste segregation</strong> (wet, dry, hazardous), 
                <strong>environmental &amp; health impacts</strong>, and <strong>best practices</strong> 
                like the 3R principle and composting — all in an engaging, easy-to-use interface.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # ── Developer Info ───────────────────────────────────────
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown(
            """
            <div class="stat-box" style="padding: 2rem;">
                <div class="stat-number">👨‍💻</div>
                <div class="stat-label" style="font-size:1.1rem; margin-top:0.8rem;">
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
                <h4>👨‍💻 Developer Details</h4>
                <ul>
                    <li><strong>Name:</strong> Ratnesh Chaurasiya</li>
                    <li><strong>Role:</strong> Developer &amp; Researcher</li>
                    <li><strong>Project Type:</strong> Social Impact / Community Awareness</li>
                    <li><strong>Focus Area:</strong> Waste Management & Environmental Sustainability</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # ── Project Objective ────────────────────────────────────
    st.markdown("## 🎯 Project Objective")
    st.markdown(
        """
        <div class="info-card animate-in">
            <ol style="color:#444444; line-height:2;">
                <li>Spread <strong>awareness</strong> about waste management practices in communities.</li>
                <li>Engage users through an <strong>interactive quiz</strong> to reinforce learning.</li>
                <li>Collect <strong>real-world data</strong> on waste management habits via surveys.</li>
                <li>Visualize <strong>community impact</strong> using a live data dashboard.</li>
                <li>Demonstrate the power of <strong>digital tools</strong> for social impact.</li>
            </ol>
        </div>
        """,
        unsafe_allow_html=True,
    )


