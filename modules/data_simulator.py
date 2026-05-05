#-----data center----#
# ============================================================
# FILE: data_simulator.py
# PURPOSE: Simulates real-time traffic sensor data for 6 city
#          intersections. This acts as the "data source" for the
#          entire Smart Traffic System. In a real system, this
#          data would come from physical IoT sensors on the road.
# AUTHOR: [Your Name]
# PROJECT: Autonomous Smart Traffic System
# ============================================================

# --- IMPORTS ---
# pandas  : used to create and manage the data table (DataFrame)
# numpy   : imported for any future numerical operations
# random  : used to generate random traffic values per junction
# datetime: used to capture the current timestamp for each reading

import pandas as pd 
import numpy as np
import random 
import datetime 

# --- JUNCTION LIST ---
# This list represents 6 intersections across the city.
# In a real system, these would be physical sensor locations
# sending live data. Here we simulate them with random values.

Roads = ["Junction A" , "Junction B" , "Junction C" , "Junction D","Junction E", "Junction F"] #list containing Junctionss (Random Roads/Juction)

# --- ROW STORAGE ---
# An empty list that will collect one dictionary per junction.
# After the loop, this gets converted into a DataFrame (table).

rows = []

def generate_traffic_data():
# ============================================================
# FUNCTION: generate_traffic_data()
# PURPOSE : Loops through all 6 junctions and generates random
#           traffic data for each one. Returns a complete
#           DataFrame with one row per junction.
# RETURNS : pandas DataFrame with 6 rows and 6 columns
# ============================================================ 

    rows.clear()
    # Clear the rows list every time the function is called.
                # This ensures fresh data on every refresh — not accumulated old data.

    for junction in Roads: # loops 6 times, once per junction

        # --- MAIN LOOP ---
    # For each junction in the Roads list, generate a full set
    # of traffic readings and store them as one row (dictionary).

        vehicle_count = random.randint(10, 200) #---  generating random vehicle counts

        # Number of vehicles currently at this intersection.
        # randint gives a random whole number between 10 and 200.


        avg_speed_kmph = round(random.uniform(5, 80,), 2) 

        # Average speed of vehicles at this intersection in km/h.
        # uniform gives a random decimal between 5.0 and 80.0.
        # round(..., 2) keeps it to 2 decimal places for cleanliness.

        accident_risk_score = round(random.uniform(0.0, 1.0), 2) 

        # A score between 0.0 and 1.0 representing accident risk.
        # 0.0 = completely safe, 1.0 = extremely dangerous.

        now = datetime.datetime.now()

        # Capture the exact current date and time for this reading.
        # datetime.datetime.now() → first 'datetime' is the module,
        # second 'datetime' is the class inside that module.

        hour = now.hour

        # Extract just the hour number from the timestamp (0–23).
        # Example: if time is 14:32:10, hour = 14
        # This is useful later for the ML congestion model since
        # traffic patterns change based on time of day.

        row = {             
            ## --- BUILD ONE ROW ---
            # Package all the generated values into a dictionary.
            # Each key is a column name, each value is the data.
            # This dictionary represents ONE intersection's data snapshot.                                    
        "location" : junction,
        "time" : now,
        "Vehicle_count" : vehicle_count,
        "avg_speed_kmph" : avg_speed_kmph,
        "accident_risk_score" : accident_risk_score,
        "hour" : hour
        }
        rows.append(row)
    df = pd.DataFrame(rows)
    # --- BUILD DATAFRAME ---
    # Convert the list of 6 dictionaries into a pandas DataFrame.
    # Each dictionary becomes one row, each key becomes a column.
    return df
func_call = generate_traffic_data()
print(func_call)
