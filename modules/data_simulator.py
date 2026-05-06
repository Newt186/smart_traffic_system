import pandas as pd 
import numpy as np
import random 
import datetime 



Roads = ["Junction A" , "Junction B" , "Junction C" , "Junction D","Junction E", "Junction F"] #list containing Junctionss (Random Roads/Juction)
rows = []

def generate_traffic_data():

    rows.clear()

    for junction in Roads: 
        vehicle_count = random.randint(10, 200) #---  generating random vehicle counts
        avg_speed_kmph = round(random.uniform(5, 80,), 2) 
        accident_risk_score = round(random.uniform(0.0, 1.0), 2) 
        now = datetime.datetime.now()
        hour = now.hour

        row = {             
                                                
        "location" : junction,
        "time" : now,
        "Vehicle_count" : vehicle_count,
        "avg_speed_kmph" : avg_speed_kmph,
        "accident_risk_score" : accident_risk_score,
        "hour" : hour
        }
        rows.append(row)
    df = pd.DataFrame(rows)

    return df
func_call = generate_traffic_data()
print(func_call)
