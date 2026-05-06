"""YOUR STEP 3 — accident_detector.py
----------------------------------------------------------------
PURPOSE:
Scan each intersection and flag it if there's a possible accident.
Uses a combination of low speed + high vehicle count + high risk score.

WHAT TO BUILD:
One function: detect_accidents(df)

LOGIC TO IMPLEMENT:
For each row, check this condition:
    IF avg_speed_kmph < 15
    AND vehicle_count > 100
    AND accident_risk_score > 0.7
    THEN → mark as possible accident

Add two new columns:
    - accident_flag    → True or False
    - alert_message   → "⚠️ Possible Accident Detected" or "Clear" """

import numpy as np #for safety imports 
import pandas as pd 
from data_simulator import generate_traffic_data
from congestion_model import label_congestion, predict_congestion
import datetime

def detect_accident(df):

    accident_flags = []
    alert_messages = []
    for index ,row in df.iterrows():
        if row["avg_speed_kmph"] < 20 and row["Vehicle_count"] > 100 and row["accident_risk_score"] > 0.7 :
            accident_flag = True 
            alert_message = "Chances of accident - HIGH"
        elif row["avg_speed_kmph"] < 12 and row["Vehicle_count"] > 130 and row["accident_risk_score"]  > 0.9:
            accident_flag = True   
            alert_message = "chances of accident - Possible"
        else:
            accident_flag = False
            alert_message = "chances of accident - LOW "
            accident_flags.append(accident_flag)
            alert_messages.append(alert_message)

    df["accident_flag"] = accident_flags
    df["alert_message"] = alert_messages
    return df
    
        
    
df = generate_traffic_data()
acci_data = detect_accident(df)
print(acci_data)






