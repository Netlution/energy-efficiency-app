import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
 
st.set_page_config(page_title="Data Insights | Energy Efficiency", page_icon="📊", layout="wide")
 
st.title("📊 Data Insights")
st.write(
    "Explore the underlying dataset (768 building designs) and how each feature "
    "relates to Heating Load and Cooling Load."
)


# @st.cache_data
# @st.cache_data
# def load_data():
#     df = pd.read_excel(
#         r"C:\Users\user\Downloads\energy efficiency\Energy\ENB2012_data.xlsx"
#     )

#     df.rename(columns={
#         'X1': 'Relative_Compactness',
#         'X2': 'Surface_Area',
#         'X3': 'Wall_Area',
#         'X4': 'Roof_Area',
#         'X5': 'Overall_Height',
#         'X6': 'Orientation',
#         'X7': 'Glazing_Area',
#         'X8': 'Glazing_Area_Distribution',
#         'Y1': 'Heating_Load',
#         'Y2': 'Cooling_Load'
#     }, inplace=True)

#     df.index = range(1, len(df) + 1)

#     return df

# df = load_data()

from pathlib import Path
import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "Energy" / "ENB2012_data.xlsx"


@st.cache_data
def load_data():
    df = pd.read_excel(DATA_PATH)

    df.columns = [
        "Relative_Compactness",
        "Surface_Area",
        "Wall_Area",
        "Roof_Area",
        "Overall_Height",
        "Orientation",
        "Glazing_Area",
        "Glazing_Area_Distribution",
        "Heating_Load",
        "Cooling_Load"
    ]

    return df


df = load_data()


with st.expander("Show raw data table"):
    st.dataframe(df, use_container_width=True)
 
st.divider()
 
# 1. Is there a relationship between Heating Load and Cooling Load? ----------------
st.subheader("Is there a relationship between Heating Load and Cooling Load?")
 
fig, ax = plt.subplots()
sns.scatterplot(x=df['Heating_Load'], y=df['Cooling_Load'], ax=ax)
ax.set_xlabel('Heating Load')
ax.set_ylabel('Cooling Load')
ax.set_title('Heating Load vs Cooling Load')
st.pyplot(fig)
 
st.write("Correlation =", df['Heating_Load'].corr(df['Cooling_Load']))
 
st.divider()
 
# 2. What is the distribution of Heating Load and Cooling Load? ----------------
st.subheader("What is the distribution of Heating Load and Cooling Load?")
 
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(df['Heating_Load'], bins=20)
ax.set_title('Heating Load Distribution')
ax.set_xlabel('Heating Load')
ax.set_ylabel('Frequency')
st.pyplot(fig)
 
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(df['Cooling_Load'], bins=20)
ax.set_title('Cooling Load Distribution')
ax.set_xlabel('Cooling Load')
ax.set_ylabel('Frequency')
st.pyplot(fig)
 
st.divider()
 
# 3. Analyze whether larger window areas increase cooling requirements ----------------
st.subheader("Analyze whether larger window areas increase cooling requirements")
 
fig, ax = plt.subplots()
sns.scatterplot(x=df['Glazing_Area'], y=df['Cooling_Load'], ax=ax)
ax.set_xlabel('Glazing Area')
ax.set_ylabel('Cooling Load')
ax.set_title('Glazing Area vs Cooling Load')
st.pyplot(fig)
 
st.divider()
 
# ---------------- 4. Average heating load by overall height ----------------
st.subheader("Average heating load by overall height")
 
result = df.groupby('Overall_Height')['Heating_Load'].mean()
 
fig, ax = plt.subplots()
result.plot(kind="bar", ax=ax)
ax.set_xlabel('Overall Height')
ax.set_ylabel('Average Heating Load')
st.pyplot(fig)