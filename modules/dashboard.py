import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os


DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "survey_results.csv")


def render():
    st.markdown("# 📊 Community Impact Dashboard")
    st.markdown("*Real-time insights from survey responses — see how our community is progressing!*")
    st.markdown("---")

    # ── Load data ────────────────────────────────────────────
    if not os.path.exists(DATA_PATH):
        st.warning("No survey data found yet. Be the first to take the **📝 Survey**!")
        return

    try:
        df = pd.read_csv(DATA_PATH)
    except pd.errors.EmptyDataError:
        st.warning("No survey data found yet. Be the first to take the **📝 Survey**!")
        return

    if df.empty:
        st.warning("No survey data found yet. Be the first to take the **📝 Survey**!")
        return

    # ── Key Metrics ──────────────────────────────────────────
    st.markdown("## 🔑 Key Metrics")

    total = len(df)
    aware_count = len(df[df["Awareness_Level"] == "Aware"])
    segregation_yes = len(df[df["Waste_Segregation"] == "Yes"])
    recycling_yes = len(df[df["Recycling_Habit"] == "Yes"])

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Participants", total)
    m2.metric("Fully Aware", f"{aware_count} ({aware_count/total*100:.0f}%)")
    m3.metric("Segregate Waste", f"{segregation_yes} ({segregation_yes/total*100:.0f}%)")
    m4.metric("Recycle Actively", f"{recycling_yes} ({recycling_yes/total*100:.0f}%)")

    st.markdown("---")

    # ── Charts Row 1 ─────────────────────────────────────────
    st.markdown("## 📈 Awareness & Habits")

    chart1, chart2 = st.columns(2)

    with chart1:
        # Awareness-Level pie
        awareness_counts = df["Awareness_Level"].value_counts().reset_index()
        awareness_counts.columns = ["Level", "Count"]
        fig_pie = px.pie(
            awareness_counts,
            names="Level",
            values="Count",
            title="Awareness Level Distribution",
            color_discrete_sequence=["#4caf50", "#ff9800", "#f44336"],
            hole=0.4,
        )
        fig_pie.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="#e0e0e0",
            title_font_size=16,
        )
        st.plotly_chart(fig_pie, width='stretch')

    with chart2:
        # Waste segregation bar
        seg_counts = df["Waste_Segregation"].value_counts().reset_index()
        seg_counts.columns = ["Response", "Count"]
        fig_bar = px.bar(
            seg_counts,
            x="Response",
            y="Count",
            title="Waste Segregation Practice",
            color="Response",
            color_discrete_map={"Yes": "#4caf50", "No": "#f44336", "Sometimes": "#ff9800"},
        )
        fig_bar.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="#e0e0e0",
            title_font_size=16,
            showlegend=False,
            xaxis_title="",
            yaxis_title="Respondents",
        )
        st.plotly_chart(fig_bar, width='stretch')

    st.markdown("---")

    # ── Charts Row 2 ─────────────────────────────────────────
    chart3, chart4 = st.columns(2)

    with chart3:
        # Recycling habit bar
        rec_counts = df["Recycling_Habit"].value_counts().reset_index()
        rec_counts.columns = ["Response", "Count"]
        fig_rec = px.bar(
            rec_counts,
            x="Response",
            y="Count",
            title="Recycling Habit",
            color="Response",
            color_discrete_map={"Yes": "#4caf50", "No": "#f44336", "Sometimes": "#ff9800"},
        )
        fig_rec.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="#e0e0e0",
            title_font_size=16,
            showlegend=False,
            xaxis_title="",
            yaxis_title="Respondents",
        )
        st.plotly_chart(fig_rec, width='stretch')

    with chart4:
        # Composting pie
        comp_counts = df["Composting"].value_counts().reset_index()
        comp_counts.columns = ["Response", "Count"]
        fig_comp = px.pie(
            comp_counts,
            names="Response",
            values="Count",
            title="Composting Practice",
            color_discrete_sequence=["#4caf50", "#f44336", "#2196f3"],
            hole=0.4,
        )
        fig_comp.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="#e0e0e0",
            title_font_size=16,
        )
        st.plotly_chart(fig_comp, width='stretch')

    st.markdown("---")

    # ── Plastic Reduction ────────────────────────────────────
    st.markdown("## 🚫 Plastic Reduction Efforts")

    plastic_counts = df["Reduce_Plastic"].value_counts().reset_index()
    plastic_counts.columns = ["Response", "Count"]
    fig_plastic = px.bar(
        plastic_counts,
        x="Response",
        y="Count",
        title="Actively Reducing Plastic Use",
        color="Response",
        color_discrete_map={"Yes": "#4caf50", "No": "#f44336", "Sometimes": "#ff9800"},
    )
    fig_plastic.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#e0e0e0",
        title_font_size=16,
        showlegend=False,
        xaxis_title="",
        yaxis_title="Respondents",
    )
    st.plotly_chart(fig_plastic, width='stretch')

    st.markdown("---")

    # ── Raw Data ─────────────────────────────────────────────
    with st.expander("🗃️ View Raw Data"):
        st.dataframe(df, width='stretch')
