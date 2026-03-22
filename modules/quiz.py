import streamlit as st


# ── Question Bank ────────────────────────────────────────────
QUESTIONS = [
    {
        "q": "Which of the following is an example of **wet waste**?",
        "options": ["Plastic bottle", "Banana peel", "Newspaper", "Glass jar"],
        "answer": "Banana peel",
    },
    {
        "q": "What does the **3R principle** stand for?",
        "options": [
            "Reduce, Reuse, Recycle",
            "Remove, Repair, Restore",
            "Reduce, Repair, Recycle",
            "Remove, Reuse, Recycle",
        ],
        "answer": "Reduce, Reuse, Recycle",
    },
    {
        "q": "Which waste category do **used batteries** belong to?",
        "options": ["Wet waste", "Dry waste", "Hazardous waste", "Organic waste"],
        "answer": "Hazardous waste",
    },
    {
        "q": "Composting is best suited for which type of waste?",
        "options": ["Plastic waste", "E-waste", "Organic / wet waste", "Metal waste"],
        "answer": "Organic / wet waste",
    },
    {
        "q": "How long does a plastic bottle take to decompose?",
        "options": ["10 years", "50 years", "100 years", "450+ years"],
        "answer": "450+ years",
    },
    {
        "q": "Which gas is released when organic waste decomposes in landfills?",
        "options": ["Oxygen", "Nitrogen", "Methane", "Hydrogen"],
        "answer": "Methane",
    },
    {
        "q": "What is the primary benefit of **waste segregation at source**?",
        "options": [
            "Makes waste look organised",
            "Easier recycling and composting",
            "Reduces the weight of waste",
            "Eliminates all waste",
        ],
        "answer": "Easier recycling and composting",
    },
    {
        "q": "Which of these is a **single-use plastic** item?",
        "options": ["Steel bottle", "Cotton bag", "Plastic straw", "Glass plate"],
        "answer": "Plastic straw",
    },
    {
        "q": "Approximately how many **million tonnes** of waste does India generate annually?",
        "options": ["10", "30", "62", "100"],
        "answer": "62",
    },
    {
        "q": "Which mission focuses on cleanliness and waste management in India?",
        "options": [
            "Make in India",
            "Swachh Bharat Mission",
            "Digital India",
            "Startup India",
        ],
        "answer": "Swachh Bharat Mission",
    },
]


def render():
    st.markdown("# ❓ Waste Management Quiz")
    st.markdown("*Test your knowledge with **10 questions**. Select an answer for each and hit **Submit** to see your score!*")
    st.markdown("---")

    # ── Initialise session state ─────────────────────────────
    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False
    if "quiz_answers" not in st.session_state:
        st.session_state.quiz_answers = {}

    # ── Render questions ─────────────────────────────────────
    with st.form("quiz_form"):
        user_answers = {}
        for i, item in enumerate(QUESTIONS, start=1):
            st.markdown(f"**Q{i}. {item['q']}**")
            user_answers[i] = st.radio(
                f"Select answer for Q{i}",
                item["options"],
                index=None,
                key=f"quiz_q{i}",
                label_visibility="collapsed",
            )
            st.markdown("")  # spacing

        submitted = st.form_submit_button("🚀 Submit Quiz")

    # ── Evaluate ─────────────────────────────────────────────
    if submitted:
        st.session_state.quiz_submitted = True
        st.session_state.quiz_answers = user_answers

    if st.session_state.quiz_submitted:
        score = 0
        st.markdown("---")
        st.markdown("## 📝 Results")

        for i, item in enumerate(QUESTIONS, start=1):
            selected = st.session_state.quiz_answers.get(i, "")
            correct = item["answer"]
            if selected == correct:
                score += 1
                st.success(f"**Q{i}.** ✅ Correct! — {correct}")
            elif selected is None:
                st.error(f"**Q{i}.** ❌ You didn't select an answer.")
            else:
                st.error(f"**Q{i}.** ❌ Your answer: *{selected}* is incorrect.")

        st.markdown("---")

        # ── Score summary ────────────────────────────────────
        pct = score / len(QUESTIONS) * 100
        st.markdown(f"### 🎯 Your Score: **{score}/{len(QUESTIONS)}** ({pct:.0f}%)")

        # ── Badge system ─────────────────────────────────────
        if pct == 100:
            badge_class = "badge-gold"
            badge_text = "🏆 Gold — Waste Management Champion!"
        elif pct >= 70:
            badge_class = "badge-silver"
            badge_text = "🥈 Silver — Great Awareness!"
        elif pct >= 40:
            badge_class = "badge-bronze"
            badge_text = "🥉 Bronze — Keep Learning!"
        else:
            badge_class = "badge-green"
            badge_text = "🌱 Beginner — Room to Grow!"

        st.markdown(
            f'<div style="text-align:center;margin:1.5rem 0;">'
            f'<span class="badge {badge_class}">{badge_text}</span></div>',
            unsafe_allow_html=True,
        )

        # ── Encouragement ────────────────────────────────────
        if pct < 70:
            st.info("💡 Head back to the **📚 Awareness** section to brush up on the concepts, then try again!")
            st.session_state.quiz_completed = False
        else:
            st.success("🎉 Excellent! Now share your waste management habits in the **📝 Survey** section.")
            st.session_state.quiz_completed = True

        # ── Retry button ─────────────────────────────────────
        if st.button("🔄 Retry Quiz"):
            st.session_state.quiz_submitted = False
            st.session_state.quiz_answers = {}
            st.rerun()
