import streamlit as st
import pandas as pd
import joblib
# from style import set_black_background

# set_black_background()

st.set_page_config(page_title="Building Energy Performance Prediction App", layout="wide")

# ✅ Custom CSS for dropdowns, sliders, and buttons
st.markdown("""
    <style>
    /* Dropdown (selectbox) main box */
    div[data-baseweb="select"] > div {
        background-color: #001f3f !important; /* Deep blue background */
        color: white !important;              /* White text */
        border-radius: 8px;
    }

    /* Selected text inside dropdown */
    div[data-baseweb="select"] span {
        color: white !important; 
        font-weight: bold;
    }

    /* Dropdown arrow */
    div[data-baseweb="select"] svg {
        fill: white !important;
    }

    /* Dropdown menu (when opened) */
    ul[role="listbox"] {
        background-color: #001f3f !important; 
        color: white !important;
    }

    /* Dropdown options text */
    ul[role="listbox"] li {
        color: white !important; 
        font-weight: normal;
    }

    /* Hover effect for dropdown options */
    ul[role="listbox"] li:hover {
        background-color: #004080 !important; 
        color: white !important;
    }

    /* Slider track */
    .stSlider > div[data-baseweb="slider"] > div > div {
        background: #001f3f !important; 
    }

    /* Slider thumb (circle) */
    .stSlider > div[data-baseweb="slider"] > div > div > div {
        background-color: #001f3f !important;
        border: 2px solid white !important;
    }

    /* Style for Streamlit button */
    div.stButton > button:first-child {
        background-color: #001f3f; 
        color: white;              
        border-radius: 8px;        
        height: 3em;
        width: 100%;
        border: none;
        font-weight: bold;
    }
    div.stButton > button:first-child:hover {
        background-color: #004080; 
        color: white;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)


st.title("🏠 Building Energy Efficiency Prediction App")
st.write("This app predicts the **Heating Load** and **Cooling Load** of a building based on its architectural features.")
 
# Sidebar Inputs
st.sidebar.header("User Input Features")
 
Relative_Compactness = st.sidebar.slider("Relative Compactness", 0.60, 1.00, 0.75)
Surface_Area = st.sidebar.number_input("Surface Area", min_value=500.0, max_value=850.0, value=650.0)
Wall_Area = st.sidebar.number_input("Wall Area", min_value=240.0, max_value=420.0, value=300.0)
Roof_Area = st.sidebar.number_input("Roof Area", min_value=100.0, max_value=225.0, value=150.0)
Overall_Height = st.sidebar.selectbox("Overall Height", options=[3.5, 7.0])
Orientation = st.sidebar.selectbox("Orientation", options=[2, 3, 4, 5])
Glazing_Area = st.sidebar.selectbox("Glazing Area", options=[0.0, 0.10, 0.25, 0.40])
Glazing_Area_Distribution = st.sidebar.selectbox("Glazing Area Distribution", options=[0, 1, 2, 3, 4, 5])
 
# Collect Data
input_data = {
    "Relative_Compactness": Relative_Compactness,
    "Surface_Area": Surface_Area,
    "Wall_Area": Wall_Area,
    "Roof_Area": Roof_Area,
    "Overall_Height": Overall_Height,
    "Orientation": Orientation,
    "Glazing_Area": Glazing_Area,
    "Glazing_Area_Distribution": Glazing_Area_Distribution
}
 
df_input = pd.DataFrame([input_data])
 
st.subheader("User Input Summary")
st.dataframe(df_input)


# ---------------- Prediction ----------------
if st.button("Predict"):
    model = joblib.load("energy_model.pkl")  # Load trained model
    prediction = model.predict(df_input)[0]  # [Heating_Load, Cooling_Load]
 
    heating_load, cooling_load = prediction[0], prediction[1]
 
    st.subheader("Prediction Result")
    col1, col2 = st.columns(2)
    col1.metric("Predicted Heating Load", f"{heating_load:.2f} kWh/m²")
    col2.metric("Predicted Cooling Load", f"{cooling_load:.2f} kWh/m²")
 
    total_load = heating_load + cooling_load
    if total_load > 60:
        st.error("This design has a **high overall energy demand**.")
    elif total_load > 35:
        st.warning("This design has a **moderate overall energy demand**.")
    else:
        st.success("This design is **energy efficient** (low overall load).")
 
st.caption(
    "Model: Random Forest (multi-output) trained on the UCI Energy Efficiency dataset."
)