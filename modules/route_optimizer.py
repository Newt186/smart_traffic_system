# ============================================================
# FILE: route_optimizer.py
# PURPOSE:
# Analyze traffic conditions across predefined routes
# and recommend the least congested route.
# ============================================================

# Import pandas for DataFrame handling
import pandas as pd


# ============================================================
# FUNCTION: recommend_route(df)
# PURPOSE:
# Takes the main traffic DataFrame as input,
# compares multiple routes,
# calculates traffic scores,
# and returns the best route.
# ============================================================

def recommend_route(df):

    # --------------------------------------------------------
    # Define available city routes
    # Each route contains multiple junctions
    # --------------------------------------------------------
    routes = {
        "Route 1": ["Junction A", "Junction B", "Junction C"],
        "Route 2": ["Junction D", "Junction E", "Junction F"],
        "Route 3": ["Junction B", "Junction D", "Junction F"]
    }

    # --------------------------------------------------------
    # Empty list to store route analysis results
    # Each route's data will be stored as a dictionary
    # --------------------------------------------------------
    route_results = []

    # --------------------------------------------------------
    # Loop through each route
    # --------------------------------------------------------
    for route_name, junctions in routes.items():

        # Total traffic score for this route
        total_traffic = 0

        # Total accident penalty score
        accident_penalty = 0

        # ----------------------------------------------------
        # Check every junction inside the route
        # ----------------------------------------------------
        for junction in junctions:

            # Get the row matching current junction
            row = df[df["location"] == junction]

            # Extract vehicle count
            vehicles = row["Vehicle_count"].values[0]

            # Add vehicle count to total traffic
            total_traffic += vehicles

            # ------------------------------------------------
            # Accident penalty logic
            # If accident detected → increase route score
            # Higher score = worse route
            # ------------------------------------------------
            if row["accident_flag"].values[0] == True:
                accident_penalty += 100

        # ----------------------------------------------------
        # Calculate average traffic across route
        # ----------------------------------------------------
        average_traffic = total_traffic / len(junctions)

        # Final traffic score
        # Lower score = better route
        traffic_score = average_traffic + accident_penalty

        # ----------------------------------------------------
        # Store route analysis result
        # ----------------------------------------------------
        route_results.append({
            "route_name": route_name,
            "junctions": ", ".join(junctions),
            "average_traffic": average_traffic,
            "accident_penalty": accident_penalty,
            "traffic_score": traffic_score
        })

    # --------------------------------------------------------
    # Convert results into DataFrame
    # --------------------------------------------------------
    route_df = pd.DataFrame(route_results)

    # --------------------------------------------------------
    # Find route with LOWEST traffic score
    # --------------------------------------------------------
    best_route_index = route_df["traffic_score"].idxmin()

    # --------------------------------------------------------
    # Create recommendation column
    # False for all routes initially
    # --------------------------------------------------------
    route_df["recommended"] = False

    # Mark best route as recommended
    route_df.loc[best_route_index, "recommended"] = True

    # --------------------------------------------------------
    # Return final route analysis DataFrame
    # --------------------------------------------------------
    return route_df