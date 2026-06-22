# 🌞 PROJECT GUIDE
## Forecasting and/or Nowcasting of Solar Flares using combined Soft and Hard X-ray data from Aditya-L1

---

# 📖 Table of Contents

1. Problem Overview
2. Why This Problem Matters
3. What is Aditya-L1?
4. Understanding the L1 Point
5. Understanding Solar Flares
6. Solar Flare Classification
7. Understanding SoLEXS
8. Understanding HEL1OS
9. Soft X-Ray vs Hard X-Ray
10. What is Nowcasting?
11. What is Forecasting?
12. Why Use AI/ML?
13. Project Objectives
14. Expected Outcomes
15. Dataset Information
16. Project Architecture
17. Team Responsibilities
18. Technology Stack
19. Development Roadmap
20. Frequently Asked Questions
21. Judge Questions & Answers

---

# 🚀 Problem Overview

This project focuses on detecting and predicting Solar Flares using data collected by Aditya-L1.

The challenge is to:

- Detect ongoing solar flares (Nowcasting)
- Predict future solar flares before they occur (Forecasting)
- Visualize results through an interactive dashboard

The project uses data from:

- SoLEXS (Soft X-ray)
- HEL1OS (Hard X-ray)

payloads onboard Aditya-L1.

---

# 🌍 Why This Problem Matters

Solar flares can impact:

- Satellites
- GPS systems
- Communication networks
- Power grids
- Space missions

A strong solar flare can disrupt modern infrastructure.

Predicting them in advance helps:

- Satellite operators
- Space agencies
- Communication providers
- Researchers

take preventive actions.

---

# ☀️ What is Aditya-L1?

Aditya-L1 is India's first dedicated solar mission launched by ISRO.

Mission Goals:

- Study the Sun
- Understand solar activity
- Monitor solar flares
- Monitor coronal mass ejections
- Improve space weather forecasting

---

# 🛰 Understanding the L1 Point

L1 stands for Lagrange Point 1.

It is located approximately:

1.5 million kilometers from Earth.

Advantages:

- Continuous view of the Sun
- No Earth eclipses
- Real-time solar monitoring

This makes Aditya-L1 ideal for observing solar flares.

---

# 🔥 Understanding Solar Flares

Solar flares are sudden bursts of energy released from the Sun.

Cause:

- Magnetic field interactions
- Magnetic reconnection

Result:

- Massive energy release
- X-rays
- High-energy particles

Solar flares can last from minutes to hours.

---

# 📊 Solar Flare Classification

Solar flares are classified according to X-ray intensity.

| Class | Strength |
|---------|---------|
| A | Very Weak |
| B | Weak |
| C | Moderate |
| M | Strong |
| X | Extreme |

Example:

- M-class flare = strong
- X-class flare = very powerful

---

# 🔬 Understanding SoLEXS

Full Form:

Solar Low Energy X-ray Spectrometer

Purpose:

Measures Soft X-rays emitted by the Sun.

Helps:

- Detect flare initiation
- Monitor low-energy solar activity

---

# 🔬 Understanding HEL1OS

Full Form:

High Energy L1 Orbiting X-ray Spectrometer

Purpose:

Measures Hard X-rays emitted by the Sun.

Helps:

- Detect energetic flare activity
- Analyze high-energy events

---

# ⚡ Soft X-Ray vs Hard X-Ray

| Soft X-Ray | Hard X-Ray |
|------------|------------|
| Lower Energy | Higher Energy |
| Observed Earlier | Observed During Intense Events |
| SoLEXS | HEL1OS |

Combining both provides a more complete picture of solar flare activity.

---

# 📡 What is Nowcasting?

Nowcasting means:

Detecting an event that is happening right now.

In our project:

Input:

- SoLEXS data
- HEL1OS data

Output:

- Flare Detected
- Flare Class
- Alert Generation

Example:

"An M-class flare is currently occurring."

---

# 🔮 What is Forecasting?

Forecasting means:

Predicting future events before they happen.

In our project:

Input:

- Historical SoLEXS data
- Historical HEL1OS data

Output:

- Probability of flare occurrence
- Early warning

Example:

"There is a 75% probability of a flare occurring in the next 30 minutes."

---

# 🤖 Why Use AI/ML?

Traditional methods rely on fixed thresholds.

Problems:

- False alarms
- Missed events

AI can:

- Learn patterns
- Detect hidden relationships
- Improve prediction accuracy

Potential Models:

- Random Forest
- XGBoost
- LSTM
- GRU

---

# 🎯 Project Objectives

## Objective 1

Build an automated solar flare detection system.

## Objective 2

Build a forecasting model.

## Objective 3

Create an interactive dashboard.

## Objective 4

Generate visual alerts and predictions.

---

# 🏆 Expected Outcomes

### Nowcasting

- Real-time flare detection
- Flare classification

### Forecasting

- Future flare prediction
- Confidence score

### Dashboard

- Interactive visualization
- Alert system

---

# 📂 Dataset Information

Primary Dataset:

Aditya-L1

Sources:

- SoLEXS Level-1 Data
- HEL1OS Level-1 Data

Portal:

ISSDC PRADAN Portal

Possible Data Fields:

- Timestamp
- X-ray Flux
- Intensity
- Energy Channels

(To be updated after dataset access)

---

# 🏗 Project Architecture

```text
SoLEXS Data
       +
HEL1OS Data
       ↓
Data Cleaning
       ↓
Feature Engineering
       ↓
Nowcasting Module
       ↓
Forecasting Module
       ↓
Dashboard
       ↓
Alerts & Visualization
```

# 👥 Team Responsibilities

| Member | Role |
|----------|----------|
| Adarsh | Data Analysis, Processing, ML Nowcasting & Forecasting |
| Deepanshi | Solar Flare Analysis & Feature Engineering |
| Hindavi | Dashboard & Visualization |

---

# 🛠 Technology Stack

## Programming

- Python

## Data Processing

- Pandas
- NumPy

## Visualization

- Plotly
- Matplotlib

## Machine Learning

- Scikit-Learn
- XGBoost

## Dashboard

- Streamlit

## Version Control

- Git
- GitHub

---

# ❓ Frequently Asked Questions

## Why did we choose this problem?

Because it combines:

- Space Science
- AI/ML
- Data Analysis
- Real-world impact

and can be implemented within the hackathon timeline.

---

## Why use both SoLEXS and HEL1OS?

Because Soft and Hard X-rays provide complementary information.

Using both improves detection and forecasting.

---

## Why build Nowcasting first?

Because:

- Easier to implement
- Helps understand data
- Creates foundation for forecasting

---

## Why use Streamlit?

Because:

- Fast development
- Python-based
- Easy integration with ML models

---

# 🎤 Judge Questions & Answers

## Q1. Why did you choose this problem?

This problem combines Artificial Intelligence, Space Science, and Data Analytics while solving a real-world challenge in space weather forecasting. It aligns with our team's interests and provides significant societal and scientific impact.

---

## Q2. What is the novelty of your solution?

We combine Soft X-ray and Hard X-ray observations from Aditya-L1 and use AI/ML techniques to build a unified detection and forecasting pipeline.

---

## Q3. Why is solar flare prediction important?

Solar flares can affect:

- GPS
- Satellites
- Communication systems
- Power infrastructure

Early prediction helps mitigate risks.

---

## Q4. Why Aditya-L1?

Aditya-L1 provides continuous solar observations from the L1 point, making it ideal for monitoring and forecasting solar activity.

---

# 🚀 Team Mission

Understand the Sun.

Detect Solar Flares.

Predict Future Solar Activity.

Transform Aditya-L1 observations into actionable Space Weather Intelligence.
