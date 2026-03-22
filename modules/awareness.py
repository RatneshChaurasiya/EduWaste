import streamlit as st


def render():
    st.markdown("# 📚 Waste Management Awareness")
    st.markdown(
        "*Learn about different waste categories, their environmental impact, "
        "and the best practices you can adopt today.*"
    )
    st.markdown("---")

    # ── 1. Waste Segregation ─────────────────────────────────
    st.markdown("## 🗂️ Waste Segregation")
    st.markdown(
        "Proper segregation at source is the **first and most important step** "
        "in effective waste management."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="info-card animate-in">
                <h4>🥬 Wet Waste</h4>
                <ul>
                    <li>Kitchen scraps & leftover food</li>
                    <li>Fruit & vegetable peels</li>
                    <li>Tea bags, coffee grounds</li>
                    <li>Garden leaves & flowers</li>
                </ul>
                <p><strong>Tip:</strong> Wet waste can be composted into nutrient-rich manure!</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="info-card animate-in">
                <h4>📦 Dry Waste</h4>
                <ul>
                    <li>Paper, cardboard, newspapers</li>
                    <li>Plastic bottles & bags</li>
                    <li>Metal cans & foil</li>
                    <li>Glass bottles & jars</li>
                </ul>
                <p><strong>Tip:</strong> Most dry waste is recyclable — keep it clean and dry!</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="info-card animate-in">
                <h4>☣️ Hazardous Waste</h4>
                <ul>
                    <li>Batteries & electronics</li>
                    <li>Medicines & syringes</li>
                    <li>Paints, chemicals, solvents</li>
                    <li>Fluorescent bulbs</li>
                </ul>
                <p><strong>Tip:</strong> Never mix hazardous waste with regular trash — use designated bins!</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # ── 2. Why It Matters ────────────────────────────────────
    st.markdown("## 🌍 Why Waste Management Matters")

    with st.expander("🌿 Environmental Impact", expanded=True):
        st.markdown(
            """
            - **Landfill overflow** — India generates over **1.5 lakh tonnes** of solid waste daily; improper disposal leads to toxic landfills.
            - **Soil & water contamination** — Chemicals from waste seep into groundwater and soil, affecting agriculture.
            - **Air pollution** — Open burning of waste releases harmful gases including dioxins and furans.
            - **Climate change** — Decomposing organic waste in landfills produces methane, a greenhouse gas **25× more potent** than CO₂.
            - **Ocean pollution** — Around **8 million tonnes** of plastic end up in oceans every year, harming marine life.
            """
        )

    with st.expander("🏥 Health Impact"):
        st.markdown(
            """
            - **Respiratory diseases** from inhaling toxic fumes of burning waste.
            - **Waterborne diseases** (cholera, typhoid) from contaminated water sources.
            - **Skin infections** from direct contact with untreated waste.
            - **Vector-borne diseases** — Accumulated waste attracts mosquitoes (dengue, malaria) and rodents.
            - **Long-term effects** — Exposure to heavy metals and chemicals from e-waste can lead to neurological damage.
            """
        )

    st.markdown("---")

    # ── 3. Best Practices ────────────────────────────────────
    st.markdown("## ✅ Best Practices")

    with st.expander("♻️ Reduce, Reuse, Recycle", expanded=True):
        st.markdown(
            """
            | Practice | Examples |
            |----------|----------|
            | **Reduce** | Avoid single-use plastics, buy in bulk, choose minimal packaging |
            | **Reuse** | Use cloth bags, repurpose glass jars, donate old clothes |
            | **Recycle** | Separate recyclables, use designated recycling bins, buy recycled products |
            """
        )

    with st.expander("🌱 Composting Tips"):
        st.markdown(
            """
            1. **Start small** — Use a pot or a small bin on your balcony.
            2. **Layer it** — Alternate between green waste (food scraps) and brown waste (dry leaves, cardboard).
            3. **Keep it moist** — Add water occasionally; the pile should feel like a wrung-out sponge.
            4. **Turn it** — Mix the compost every few days to allow air circulation.
            5. **Patience** — Compost is ready in **2-3 months**; use it in your garden!
            """
        )

    with st.expander("💡 Quick Daily Habits"):
        st.markdown(
            """
            - 🛍️ Carry a **reusable bag** whenever you go shopping.
            - 🚰 Use a **refillable water bottle** instead of buying packaged water.
            - 📰 Go **paperless** — switch to digital bills and notes.
            - 🍱 Use **steel or glass containers** for lunch instead of plastic.
            - 🔋 Dispose of **batteries and e-waste** at collection centres.
            """
        )

    st.markdown("---")

    # ── Did You Know ─────────────────────────────────────────
    st.markdown("## 💡 Did You Know?")
    facts_col1, facts_col2 = st.columns(2)
    with facts_col1:
        st.markdown(
            """
            <div class="info-card">
                <h4>🌎 Global Facts</h4>
                <ul>
                    <li>The world generates <strong>2.01 billion tonnes</strong> of municipal solid waste annually.</li>
                    <li>Only <strong>13.5%</strong> of waste is recycled globally.</li>
                    <li>A plastic bottle takes <strong>450+ years</strong> to decompose.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with facts_col2:
        st.markdown(
            """
            <div class="info-card">
                <h4>🇮🇳 India Facts</h4>
                <ul>
                    <li>India generates about <strong>62 million tonnes</strong> of waste per year.</li>
                    <li>Only <strong>22-28%</strong> of waste is processed and treated.</li>
                    <li>The Swachh Bharat Mission has significantly improved solid waste collection coverage.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.success("✅ You're now ready to test your knowledge! Head over to the **❓ Quiz** section from the sidebar.")
