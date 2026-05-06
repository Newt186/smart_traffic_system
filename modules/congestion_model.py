#congestion model
import numpy as np 
import pandas as pd
import random 
import datetime 
from data_simulator import generate_traffic_data
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier



def label_congestion(df):
    labels = []
    for index, row in df.iterrows():
        if row["Vehicle_count"] > 150 and row["avg_speed_kmph"] < 20:
            labels.append("High")
        elif row["Vehicle_count"] > 80 and row["avg_speed_kmph"] < 40:
            labels.append("Medium")
        else:
            labels.append("Low")
    df["congestion_level"] = labels
    return df

def predict_congestion(df):
    predicted_congestion = []
    congs_label = label_congestion(df)
    x = congs_label[["Vehicle_count", "avg_speed_kmph", "hour"]]
    y = congs_label["congestion_level"]
    Model_encoder = LabelEncoder()
    encode_y = Model_encoder.fit_transform(y)

    f_classify = RandomForestClassifier()
    f_classify.fit(x, encode_y)

    predicted_result = f_classify.predict(x)
    predicted_labels = Model_encoder.inverse_transform(predicted_result)
    
    congs_label["predicted_congestion"] = predicted_labels
    return congs_label
    

df = generate_traffic_data()
congs_level = label_congestion(df)
print(congs_level)
pd_cong = predict_congestion(df)
print(pd_cong)


