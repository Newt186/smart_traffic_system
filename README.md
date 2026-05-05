Autonomous Smart Traffic System

An AI-powered smart city traffic control system that monitors real-time traffic data, predicts congestion, dynamically adjusts signal timings, detects accidents, and recommends the least congested route — all from one live dashboard.

Problem Statement Urban traffic congestion costs cities billions of dollars every year in lost productivity, fuel waste, and emergency response delays. Traditional traffic signals operate on fixed timers — completely blind to actual traffic conditions. There is no real-time intelligence, no accident awareness, and no dynamic routing. We built a system that changes that.

Our Solution The Autonomous Smart Traffic System simulates a network of smart city sensors and uses AI to:

Predict congestion levels before they become critical Adapt traffic signal timings automatically based on real-time data Detect possible accidents using multi-factor risk analysis Recommend the safest and least congested route for drivers Visualize everything on a live, auto-refreshing control dashboard

Features FeatureDescription Real-Time Data SimulationSimulates IoT sensor data from 6 city intersections🤖 Congestion PredictionML model classifies congestion as Low / Medium / High🚦 Smart Signal ControlGreen light timing adjusts dynamically based on congestion Accident DetectionFlags dangerous intersections using speed, volume and risk score🗺️ Route OptimizationScores all routes and recommends the least congested path📊 Live DashboardAuto-refreshing Streamlit dashboard with charts and alerts

Tech Stack

Python — Core logic and data processing Streamlit — Interactive live dashboard Pandas & NumPy — Data handling and manipulation Plotly — Interactive charts and visualizations Scikit-learn — Random Forest model for congestion prediction

Folder Structure smart_traffic_system/ │ ├── app.py # Main Streamlit dashboard (entry point) │ ├── modules/ │ ├── init.py # Makes modules a Python package │ ├── data_simulator.py # Simulates real-time traffic sensor data │ ├── congestion_model.py # ML model: predicts Low/Medium/High congestion │ ├── signal_controller.py # Smart signal timing logic │ ├── accident_detector.py # Detects possible accidents from data │ └── route_optimizer.py # Compares routes and recommends the best one │ ├── data/ │ └── traffic_log.csv # Optional: saved simulation snapshots │ ├── assets/ │ └── city_map.png # Optional: city map visual │ ├── requirements.txt # All Python dependencies └── README.md # Project documentation

How to Run

Clone the repository bashgit clone https://github.com/Newt186/smart_traffic_system.git cd smart_traffic_system
Install dependencies bashpip install -r requirements.txt
Run the dashboard bashstreamlit run app.py The dashboard will open automatically in your browser at http://localhost:8501
Dashboard Preview The dashboard includes:

Metric Cards — Total vehicles, average speed, active accidents, best route Live Congestion Chart — Color-coded bar chart per intersection Recommended Route Panel — Best route with reasoning Intersection Control Table — Full data snapshot with signal timings Signal Timing Chart — Visual of green light durations per junction Auto Refresh — Simulates live sensor updates every 5 seconds

How the AI Works Congestion Prediction

Model: Random Forest Classifier Input features: vehicle count, average speed, hour of day Output: Low / Medium / High congestion label Rule-based labeling creates training data from simulated readings

Accident Detection

Flags an intersection when:

Average speed < 15 km/h AND Vehicle count > 100 AND Accident risk score > 0.7

Severity levels: Clear → Warning → Critical

Route Optimization

3 routes defined across the city junctions Each route scored by average vehicle count of its junctions Accident-affected junctions receive a heavy penalty score Lowest score = recommended route

Signal Control

High congestion → 90 seconds green light Medium congestion → 60 seconds green light Low congestion → 30 seconds green light Accident detected → 120 seconds + Emergency Override

Team MemberRole[Soham Mulay]AI Logic — Data simulation, congestion model, accident detection, route optimizer[Sharwil Aher]Dashboard & UI — Signal controller, Streamlit dashboard, README, presentation

Future Scope

Connect to real IoT traffic sensors via MQTT or REST API Integrate Google Maps or HERE Maps for live GPS routing Add weather data — rain and fog increase accident risk scores Build a mobile alert system to notify drivers in real time Use Reinforcement Learning to optimize signal timing over time Deploy on AWS or GCP for 24/7 city-wide operation Add computer vision (YOLO) for camera-based vehicle counting Expand to full city road graph using NetworkX for routing

Requirements streamlit pandas numpy plotly scikit-learn Install all with: bashpip install -r requirements.txt

License This project was built for educational and hackathon purposes.

"Smart cities don't just collect data — they act on it."