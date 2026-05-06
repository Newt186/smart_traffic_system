# Autonomous Smart Traffic System

An AI-powered smart city traffic control system that monitors real-time traffic data, predicts congestion, dynamically adjusts signal timings, detects accidents, and recommends the least congested route — all from a unified live dashboard.

---

## Problem Statement

Urban traffic congestion costs cities billions of dollars every year in lost productivity, fuel waste, and delayed emergency response.

Traditional traffic systems rely on fixed signal timers that do not adapt to real-time conditions. These systems lack:

- Real-time traffic awareness  
- Dynamic signal optimization  
- Accident detection mechanisms  
- Intelligent route recommendations  

This project addresses these limitations with a data-driven, adaptive system.

---

## Solution Overview

The Autonomous Smart Traffic System simulates a network of smart traffic sensors and applies machine learning and rule-based intelligence to:

- Predict congestion levels before they escalate  
- Dynamically adjust traffic signal timings  
- Detect potential accidents using multi-factor analysis  
- Recommend optimal routes based on real-time conditions  
- Visualize the entire system through a live dashboard  

---

## Features

| Feature                     | Description |
|---------------------------|------------|
| Real-Time Data Simulation | Simulates IoT traffic sensor data across multiple intersections |
| Congestion Prediction     | Classifies congestion as Low, Medium, or High using ML |
| Smart Signal Control      | Dynamically adjusts green light duration |
| Accident Detection        | Identifies high-risk traffic conditions |
| Route Optimization        | Recommends least congested route |
| Live Dashboard            | Interactive Streamlit interface with auto-refresh |

---

## Tech Stack

- Python — Core logic and computation  
- Streamlit — Interactive dashboard  
- Pandas, NumPy — Data processing  
- Plotly — Data visualization  
- Scikit-learn — Machine learning model  

---

## Project Structure

```text
smart_traffic_system/
│
├── app/
│   └── dashboard.py
│
├── simulator/
│   └── traffic_simulator.py
│
├── models/
│   └── congestion_model.py
│
├── engine/
│   ├── signal_control.py
│   ├── accident_detection.py
│   └── route_optimizer.py
│
├── utils/
│   └── data_processor.py
│
├── data/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## How to Run

1. Clone the repository:

git clone https://github.com/Newt186/smart_traffic_system.git

cd smart_traffic_system


2. Install dependencies:

pip install -r requirements.txt


3. Run the application:

streamlit run app/dashboard.py


4. Open browser:

http://localhost:8501


---

## Dashboard Overview

The dashboard includes:

- Metric Cards — Total vehicles, average speed, accidents, recommended route  
- Live Congestion Chart — Intersection-wise congestion visualization  
- Route Recommendation Panel — Best route with reasoning  
- Intersection Table — Real-time traffic data and signal timings  
- Signal Timing Chart — Visual representation of signal durations  
- Auto Refresh — Updates every few seconds  

---

## System Logic

### Congestion Prediction

- Model: Random Forest Classifier  
- Inputs:
  - Vehicle count  
  - Average speed  
  - Time of day  
- Output:
  - Low / Medium / High congestion  

Training data is generated from simulated traffic patterns.

---

### Accident Detection

An intersection is flagged when:

- Average speed < 15 km/h  
- Vehicle count > 100  
- Risk score > 0.7  

Severity Levels:
- Clear  
- Warning  
- Critical  

---

### Signal Control Logic

- High congestion → 90 seconds green  
- Medium congestion → 60 seconds green  
- Low congestion → 30 seconds green  
- Accident detected → 120 seconds with priority override  

---

### Route Optimization

- Multiple routes defined across intersections  
- Each route scored using:
  - Vehicle density  
  - Congestion level  
  - Accident penalties  
- Lowest score route is recommended  

---

## Team

| Member        | Role |
|--------------|------|
| Soham Mulay  | AI Logic, Simulation, ML Model, Optimization |
| Sharwil Aher | Dashboard, UI, Integration, Presentation |

---

## Future Scope

- Integration with real IoT sensors (MQTT / APIs)  
- Live map integration (Google Maps / HERE Maps)  
- Weather-aware traffic modeling  
- Reinforcement learning for adaptive signals  
- Cloud deployment (AWS / GCP)  
- Computer vision-based vehicle detection  
- Full road network graph optimization  

---

## Requirements


streamlit
pandas
numpy
plotly
scikit-learn


Install using:

pip install -r requirements.txt


---

## License

This project is developed for educational and hackathon purposes.

---

Smart cities are not defined by how much data they collect, but by how effectively they use it.