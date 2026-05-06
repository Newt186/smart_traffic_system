import pandas as pd
from accident_detector import detect_accident 
import datetime 
from congestion_model import label_congestion, predict_congestion
from data_simulator import generate_traffic_data
"""PURPOSE:
Decide traffic signal timing for each intersection based on
predicted congestion level and accident flags.

WHAT TO BUILD:
One function: calculate_signal_timing(df)

LOGIC TO IMPLEMENT:
For each row, assign green light duration based on congestion:
    - "High" congestion   → green_time = 90 seconds
    - "Medium" congestion → green_time = 60 seconds
    - "Low" congestion    → green_time = 30 seconds

Emergency override:
    - If accident_flag is True → green_time = 120 seconds
    (emergency vehicles need maximum clearance)
    and add a note: signal_note = "EMERGENCY OVERRIDE"

Add two columns:
    - green_light_seconds
    - signal_note (e.g., "Normal", "Extended", "EMERGENCY OVERRIDE")

Return the updated DataFrame."""

def calculate_signal_timing(df):
            green_light_seconds = []
            signal_notes = []
            for index , row in df.iterrows():
                    if row["congestion_level"] == "High":
                            green_time = "90 sec"
                            signal_note = "Extended"
                    elif row["congestion_level"] == "Medium": 
                            green_time = "60 sec"
                            signal_note = "Normal caution"
                    else:
                            green_time = "30 sec"
                            signal_note = "Normal"
                    green_light_seconds.append(green_time)
                    signal_notes.append(signal_note)

            df["green_time"] = green_light_seconds
            df["signal_note"] = signal_notes
            return df
df = generate_traffic_data()
congs_level = label_congestion(df)
print(congs_level)
pd_cong = predict_congestion(df)
print(pd_cong)
s_time = calculate_signal_timing(df)
print(s_time)




        
            