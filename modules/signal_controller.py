import pandas as pd
from modules.accident_detector import detect_accident 
import datetime 
from modules.congestion_model import label_congestion, predict_congestion
from modules.data_simulator import generate_traffic_data


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




        
            