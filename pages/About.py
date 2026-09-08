import streamlit as st

st.set_page_config(page_title="Energy Efficiency App", page_icon="🏠", layout="centered")

st.title("🏠 Building Energy Efficiency App")

st.write(
    """
    Welcome! This app is built on the **UCI Energy Efficiency dataset**, which contains
    768 simulated building designs and their resulting heating and cooling energy demand.

    Each building is described by 8 shape/design features:
    """
)

st.markdown(
    """
    | Feature | Description |
    |---|---|
    | Relative Compactness | Ratio of building volume to surface area |
    | Surface Area | Total external surface area (m²) |
    | Wall Area | Total wall area (m²) |
    | Roof Area | Total roof area (m²) |
    | Overall Height | Building height (m) |
    | Orientation | Compass direction the building faces |
    | Glazing Area | Fraction of floor area that is glazed (windows) |
    | Glazing Area Distribution | How glazing is distributed across sides |
    """
)

st.write(
    """
    From these features, the app predicts two **targets**:
    - **Heating Load** — energy needed to heat the building (kWh/m²)
    - **Cooling Load** — energy needed to cool the building (kWh/m²)

    ### 👉 Use the sidebar to navigate:
    - **Predict** — enter your own building features and get a prediction
    - **Data Insights** — explore the dataset and how features relate to energy load
    """
)

st.info("Select a page from the sidebar on the left to get started.")