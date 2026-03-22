import streamlit as st
import pandas as pd
import os
from datetime import datetime
from modules import certificate


DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "survey_results.csv")


def render():
    st.markdown("# 📝 Waste Management Survey")
    st.markdown(
        "*Help us understand community waste management habits. "
        "Your responses are anonymous and contribute to our impact dashboard.*"
    )
    st.markdown("---")

    with st.form("survey_form", clear_on_submit=True):
        # ── Personal Info ────────────────────────────────────
        st.markdown("### 👤 Personal Information")
        name = st.text_input("Name (Required for Certificate)", placeholder="Enter your full name")

        st.markdown("---")

        # ── Awareness Questions ──────────────────────────────
        st.markdown("### 💡 Awareness")

        awareness_level = st.radio(
            "How would you rate your awareness of waste management?",
            ["Aware", "Somewhat Aware", "Not Aware"],
            horizontal=True,
        )

        st.markdown("---")

        # ── Behaviour Questions ──────────────────────────────
        st.markdown("### 🔄 Your Waste Management Habits")

        col1, col2 = st.columns(2)
        with col1:
            segregation = st.radio(
                "Do you segregate waste at home?",
                ["Yes", "No", "Sometimes"],
                horizontal=True,
            )
            composting = st.radio(
                "Do you compost organic waste?",
                ["Yes", "No", "Planning to start"],
                horizontal=True,
            )

        with col2:
            recycling = st.radio(
                "Do you recycle (paper, plastic, glass)?",
                ["Yes", "No", "Sometimes"],
                horizontal=True,
            )
            reduce_plastic = st.radio(
                "Do you actively try to reduce plastic use?",
                ["Yes", "No", "Sometimes"],
                horizontal=True,
            )

        st.markdown("---")

        submitted = st.form_submit_button("📤 Submit Survey")

    # ── Save data ────────────────────────────────────────────
    if submitted:
        new_row = {
            "Name": name if name.strip() else "Anonymous",
            "Awareness_Level": awareness_level,
            "Waste_Segregation": segregation,
            "Recycling_Habit": recycling,
            "Composting": composting,
            "Reduce_Plastic": reduce_plastic,
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        # Ensure data directory exists
        os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

        # Append to CSV
        try:
            df = pd.read_csv(DATA_PATH)
        except (FileNotFoundError, pd.errors.EmptyDataError):
            df = pd.DataFrame(
                columns=[
                    "Name", "Awareness_Level", "Waste_Segregation",
                    "Recycling_Habit", "Composting", "Reduce_Plastic", "Timestamp",
                ]
            )

        new_df = pd.DataFrame([new_row])
        df = pd.concat([df, new_df], ignore_index=True)
        df.to_csv(DATA_PATH, index=False)

        st.success("🎉 **Thank you!** Your response has been recorded successfully.")
        st.balloons()
        st.info("📊 Head over to the **Dashboard** to see community insights!")
        
        st.session_state.survey_completed = True
        st.session_state.user_name = name.strip() if name.strip() else "Participant"

    # ── Display Certificate ──────────────────────────────────
    if st.session_state.get("survey_completed"):
        if st.session_state.get("quiz_completed"):
            user_name = st.session_state.get("user_name", "Participant")
            st.markdown("---")
            st.markdown("### 🎓 Your Certificate")
            st.success(f"Congratulations **{user_name}**! You have successfully completed the awareness quiz and survey.")
            
            # Generate Certificate
            cert_bytes = certificate.generate_certificate(user_name)
            
            # Display Certificate
            st.image(cert_bytes, use_container_width=True)
            
            st.download_button(
                label="⬇️ Download Certificate (PNG)",
                data=cert_bytes,
                file_name="Waste_Management_Certificate.png",
                mime="image/png"
            )
        else:
            st.markdown("---")
            st.info("ℹ️ **Certificate Locked**: To generate your certificate, you must also pass the **❓ Quiz** with a score of 70% or higher. Go back to the Quiz page, pass it, and your certificate will appear here!")
