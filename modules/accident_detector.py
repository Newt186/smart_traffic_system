
import numpy as np #for safety imports 
import pandas as pd 
from data_simulator import generate_traffic_data


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






