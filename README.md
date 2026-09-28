# 🏠 Building Energy Efficiency Prediction App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://energy-efficiencyy.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Random%20Forest-F7931E?logo=scikitlearn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

An interactive machine learning application that predicts a building's **heating load** and **cooling load** from its architectural and design characteristics.

🚀 **Live Demo:** [energy-efficiencyy.streamlit.app](https://energy-efficiencyy.streamlit.app/)
💻 **Source Code:** [github.com/Netlution/energy-efficiency-app](https://github.com/Netlution/energy-efficiency-app)

---

## 📖 Table of Contents

- [Introduction](#-introduction)
- [Project Objectives](#-project-objectives)
- [Key Features](#-key-features)
- [Machine Learning Model](#-machine-learning-model)
- [Energy Demand Calculation](#-energy-demand-calculation)
- [Application Workflow](#-application-workflow)
- [Dataset](#-dataset)
- [Data Analysis](#-data-analysis)
- [Model Development](#-model-development)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [How to Use](#-how-to-use-the-application)
- [Example Input](#-example-input)
- [Limitations](#-limitations)
- [Why This Project Matters](#-why-this-project-matters)
- [Skills Demonstrated](#-skills-demonstrated)
- [Project Links](#-project-links)
- [Disclaimer](#-disclaimer)
- [Author](#-author)
- [Support](#-support)
- [License](#-license)

---

## 📌 Introduction

Energy efficiency is an important part of modern building design and sustainable development. A building's size, shape, surface area, wall area, roof area, height, orientation, and glazing all influence the energy needed to keep indoor temperatures comfortable.

This project applies **data analytics and machine learning** to investigate the relationship between building characteristics and energy consumption. It uses architectural information to predict two energy-performance measures: **heating load** and **cooling load**.

The project is based on the **UCI Energy Efficiency dataset** and uses a **Random Forest** model. The trained model is integrated into an interactive **Streamlit** web application, so users can enter building characteristics and get predictions without writing or running any code.

The goal is to demonstrate a complete end-to-end data science workflow: data exploration, preparation, visualization, model development, model saving, application development, and deployment.

This project was developed for **educational, analytical, and demonstration purposes**.

---

## 🎯 Project Objectives

- Analyze building characteristics and their relationship with energy consumption
- Explore patterns within building energy-efficiency data
- Develop a machine learning model to predict heating and cooling loads
- Create an interactive application for making energy predictions
- Let users experiment with different building characteristics
- Calculate total predicted energy demand and provide a simple interpretation
- Demonstrate an end-to-end machine learning workflow
- Deploy the application online using Streamlit

---

## ✨ Key Features

- 🏠 Interactive building energy prediction
- 🤖 Random Forest multi-output regression
- 🔥 Heating load prediction
- ❄️ Cooling load prediction
- ⚡ Total energy demand calculation
- 📋 User input summary table
- 🏷️ Simple energy-efficiency classification
- 📈 Data analysis and visualization notebooks
- 🌐 Streamlit web application deployed on the cloud

---

## 🧠 Machine Learning Model

The application uses a **Random Forest Regression** model to predict two target variables:

| Target | Description |
| --- | --- |
| 🔥 Heating Load | Predicted energy required for heating |
| ❄️ Cooling Load | Predicted energy required for cooling |

### Input Features

The model uses eight building characteristics as input (ranges are those found in the training data):

| Feature | Description | Range in dataset |
| --- | --- | --- |
| Relative Compactness | Compactness of the building | 0.62 – 0.98 |
| Surface Area | Total building surface area (m²) | 514.5 – 808.5 |
| Wall Area | Wall surface area (m²) | 245 – 416.5 |
| Roof Area | Roof surface area (m²) | 110.25 – 220.5 |
| Overall Height | Overall building height (m) | 3.5 or 7 |
| Orientation | Building orientation | 2 – 5 |
| Glazing Area | Glazing as a fraction of floor area | 0 – 0.4 |
| Glazing Area Distribution | Distribution of glazing across the building | 0 – 5 |

---

## 📊 Energy Demand Calculation

The application adds the predicted heating and cooling loads to get the total predicted energy demand:

```text
Total Energy Demand = Heating Load + Cooling Load
```

| Total Load | Classification |
| ---: | --- |
| ≤ 35 | Energy Efficient |
| > 35 and ≤ 60 | Moderate Energy Demand |
| > 60 | High Energy Demand |

These thresholds are a simple interpretation of the model's output, not an official standard.

---

## 🔄 Application Workflow

```text
             User Input
                  │
                  ▼
    Building Characteristics
                  │
                  ▼
        Data Preparation
                  │
                  ▼
      Random Forest Model
                  │
         ┌────────┴────────┐
         ▼                 ▼
   Heating Load      Cooling Load
         │                 │
         └────────┬────────┘
                  ▼
      Total Energy Demand
                  │
                  ▼
     Energy Classification
                  │
                  ▼
           User Results
```

---

## 🔬 Dataset

This project uses the **UCI Energy Efficiency dataset**, which contains 768 simulated building configurations together with their heating and cooling loads. It is well suited to investigating how architectural characteristics affect building energy performance.

- **Inputs:** Relative Compactness, Surface Area, Wall Area, Roof Area, Overall Height, Orientation, Glazing Area, Glazing Area Distribution
- **Targets:** Heating Load, Cooling Load

---

## 📊 Data Analysis

Before modeling, the project includes exploratory data analysis (in `Energy.ipynb`) covering:

- Data exploration and preparation
- Data distributions
- Correlation analysis and relationships between variables
- Heating-load and cooling-load patterns
- Visualization and statistical analysis

---

## 🤖 Model Development

The development process (in `Modelenergy.ipynb`) follows these stages:

1. Load the dataset
2. Explore the data
3. Check and prepare the data
4. Select relevant features
5. Separate input features from target variables
6. Train the Random Forest model
7. Evaluate the model
8. Save the trained model
9. Integrate the model into the Streamlit application
10. Deploy the application

The trained model is saved as a `.pkl` file and loaded by the Streamlit app when predictions are requested.

---

## 🛠️ Technologies Used

| Category | Tools |
| --- | --- |
| Language | Python |
| Data Analysis | Pandas, NumPy, Jupyter Notebook |
| Machine Learning | Scikit-learn, Random Forest Regression, Joblib |
| Visualization | Matplotlib, Seaborn |
| Statistics | Statsmodels |
| Web Application | Streamlit |
| Deployment | Streamlit Community Cloud |
| Version Control | Git, GitHub |

All dependencies are listed in `requirements.txt`.

---

## 📂 Project Structure

```text
energy-efficiency-app/
│
├── .devcontainer/
├── Energy/
├── pages/
│
├── Energy.ipynb
├── Modelenergy.ipynb
├── Energy_model.pkl
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

| File | Description |
| --- | --- |
| `main.py` | Main Streamlit application |
| `Energy_model.pkl` | Saved machine learning model |
| `Energy.ipynb` | Data analysis and exploration notebook |
| `Modelenergy.ipynb` | Machine learning model development notebook |
| `requirements.txt` | Required Python packages |
| `.gitignore` | Files excluded from Git |
| `README.md` | Project documentation |

---

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/Netlution/energy-efficiency-app.git
```

**2. Navigate to the project directory**

```bash
cd energy-efficiency-app
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment**

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**5. Install dependencies**

```bash
pip install -r requirements.txt
```

**6. Run the Streamlit application**

```bash
streamlit run main.py
```

The app opens in your browser at `http://localhost:8501`.

---

## 🎯 How to Use the Application

1. Open the [live app](https://energy-efficiencyy.streamlit.app/) or run it locally.
2. Enter the building characteristics in the sidebar.
3. Review the **User Input Summary**.
4. Click **Predict**.
5. View the predicted Heating Load, Cooling Load, and Total Energy Demand.
6. Use the energy-demand classification to interpret the result.
7. Change the inputs to see how different design choices affect the predictions.

---

## 📈 Example Input

This configuration is taken from the training dataset:

```text
Relative Compactness:      0.98
Surface Area:              514.5
Wall Area:                 294
Roof Area:                 110.25
Overall Height:            7
Orientation:               2
Glazing Area:              0
Glazing Area Distribution: 0
```

The application returns predictions for **Heating Load**, **Cooling Load**, **Total Energy Demand**, and the **Energy Classification**.

---

## ⚠️ Limitations

- The dataset contains simulated buildings with a limited set of shapes, so predictions for inputs far outside the ranges above are unreliable.
- The classification thresholds are simple heuristics.
- The model does not account for climate, occupancy, or HVAC systems.

---

## 💡 Why This Project Matters

Understanding how building characteristics relate to heating and cooling requirements shows the potential of data-driven approaches to real-world energy problems.

Rather than stopping at model development inside a Jupyter Notebook, this project deploys the trained model as a web application so users can explore predictions with their own inputs.

```text
Raw Data → Data Exploration → Data Preparation → Exploratory Analysis
   → Feature Selection → Machine Learning → Model Evaluation
   → Model Saving → Streamlit Application → Deployment → Interactive Prediction
```

---

## 📚 Skills Demonstrated

- Python programming
- Data cleaning and preparation
- Exploratory data analysis and statistical analysis
- Data visualization
- Feature selection
- Regression, Random Forest, and multi-output prediction
- Model persistence with Joblib
- Web application development with Streamlit
- Machine learning deployment
- Git, GitHub, and technical documentation

---

## 🌐 Project Links

| Resource | Link |
| --- | --- |
| 🌐 Live Application | [energy-efficiencyy.streamlit.app](https://energy-efficiencyy.streamlit.app/) |
| 💻 GitHub Repository | [github.com/Netlution/energy-efficiency-app](https://github.com/Netlution/energy-efficiency-app) |

---

## 🛡️ Disclaimer

This application is intended for **educational, analytical, and demonstration purposes**.

Predictions are generated by a machine learning model and should not be considered a substitute for professional engineering calculations, building-energy simulations, energy audits, building design decisions, or official energy-efficiency certifications.

---

## 👤 Author

**Netlution**
GitHub: [@Netlution](https://github.com/Netlution)

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE). *(Add a `LICENSE` file to the repo, or change this to "available for educational and demonstration purposes.")*
