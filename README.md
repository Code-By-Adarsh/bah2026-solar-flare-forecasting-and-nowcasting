# 🚀 Aditya-L1 Solar Flare Nowcasting & Forecasting

## 📌 Problem Statement

**Forecasting and/or Nowcasting of Solar Flares using combined Soft and Hard X-ray data from Aditya-L1**

This project aims to build an AI-powered space weather monitoring system using data from Aditya-L1's:

- SoLEXS (Soft X-ray)
- HEL1OS (Hard X-ray)

The system will:

- Detect ongoing solar flares (Nowcasting)
- Predict future solar flare events (Forecasting)
- Visualize alerts through an interactive dashboard

---

## 👥 Team Anant

| Team Member | Responsibility |
|-------------|---------------|
| **Adarsh** | Data Analysis, Processing, ML Nowcasting & Forecasting |
| **Deepanshi** | Solar Flare Analysis & Feature Engineering |
| **Hindavi** | Dashboard & Visualization |

---

# 🎯 Objectives

## Phase 1: Nowcasting

Detect solar flares from incoming X-ray data.

### Expected Output

- Flare Detected
- Flare Classification
- Visual Alert

---

## Phase 2: Forecasting

Predict whether a flare may occur in the next N minutes.

### Expected Output

- Flare Probability
- Early Warning Alert
- Lead Time Estimation

---

# 👥 Team Roles

## 1️⃣ Data Engineering & Preprocessing

### Responsibilities

- Download datasets from the PRADAN portal
- Read SoLEXS data
- Read HEL1OS data
- Clean missing values
- Align timestamps
- Create merged dataset

### Deliverables

```text
solexs_clean.csv
helios_clean.csv
merged_data.csv
```

---

## 2️⃣ Solar Flare Analysis & Feature Engineering

### Responsibilities

- Study solar flare classes
- Analyze Soft X-ray and Hard X-ray behavior
- Identify historical flare events
- Design useful features for ML models

### Possible Features

- Flux Change Rate
- Rolling Mean
- Rolling Standard Deviation
- Gradient
- Moving Average
- Peak Flux
- Flux Ratios

### Deliverables

```text
flare_catalog.csv
feature_document.md
```

---

## 3️⃣ ML Nowcasting & Forecasting

### Responsibilities

- Dataset labeling
- Feature engineering
- Model training
- Model evaluation

### Phase 1

Flare vs Non-Flare Detection

### Phase 2

Future Flare Prediction

### Models

- Random Forest
- XGBoost
- LSTM (Optional)
- GRU (Optional)

### Deliverables

```text
model.pkl
evaluation_report.md
```

---

## 4️⃣ Dashboard & Visualization

### Responsibilities

- Streamlit Dashboard
- Interactive Charts
- Alert System
- Prediction Display

### Dashboard Features

- SoLEXS Graph
- HEL1OS Graph
- Flare Detection Alerts
- Forecast Probability
- Model Performance Metrics

### Deliverables

```text
dashboard_app.py
```

---

# 🛠 Tech Stack

## Programming Language

- Python

## Data Processing

- Pandas
- NumPy

## Data Visualization

- Matplotlib
- Plotly

## Machine Learning

- Scikit-learn
- XGBoost

## Dashboard

- Streamlit

## Version Control

- Git
- GitHub

---

# 📂 Project Structure

```text
solar-flare-project/

│
├── .devcontainer/
│
├── .streamlit/
│
├── Asset/
│
├── Backend/
│   ├── catalog_builder.py/
│   ├── file_reader.py/
│   ├── flare_detector.py/
│
├── Data/
│   ├── processed/
│   ├── sample_data/
│        ├── HEL1OS/
│             ├── 15_june_cdte1_data_part1/
│             ├── 15_june_cdte1_data_part2/
│        ├── SoLEXS/
│             ├── 15_june_data/
│
├── Documents/
│
├── License
│
├── PROJECT_GUIDE.md
│
├── README.md
│
├── app1.py
|
└── requirements.txt
```

---

# 📚 Learning Resources

## Solar Flares

- NASA Solar Flare Basics
- Aditya-L1 Mission Overview
- SoLEXS Documentation
- HEL1OS Documentation

## Python

- Pandas Documentation
- NumPy Documentation

## Machine Learning

- Scikit-learn Documentation
- XGBoost Documentation

## Dashboard

- Streamlit Documentation

---

# 🌞 Vision

Build a lightweight AI-powered space weather monitoring system using Aditya-L1 data that can detect and forecast solar flares while providing clear visual alerts through an interactive dashboard.

---

# 🚀 Team Mission

Understand the Sun.

Detect Solar Flares.

Predict Future Events.

Transform Aditya-L1 data into actionable space-weather intelligence.
