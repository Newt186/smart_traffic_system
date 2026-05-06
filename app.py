import streamlit as st
import pandas as pd
import plotly.express as px
import time

from modules.data_simulator import generate_traffic_data
from modules.congestion_model import label_congestion, predict_congestion
from modules.accident_detector import detect_accident
from modules.signal_controller import calculate_signal_timing
from modules.route_optimizer import recommend_route

st.set_page_config(
    page_title="Smart Traffic System",
    page_icon="🚦",
    layout="wide"
)

st.markdown("""
    <style>
        .main {
            background-color: #0f1117;
        }

        div[data-testid="metric-container"] {
            background-color: #1e2130;
            border: 1px solid #2e3250;
            border-radius: 10px;
            padding: 15px;
        }

        h1 {
            color: #00d4ff;
        }

        h2, h3 {
            color: #ffffff;
        }

        .accident-alert {
            background-color: #ff4444;
            color: white;
            padding: 10px;
            border-radius: 8px;
            font-weight: bold;
        }

        .route-box {
            background-color: #1a472a;
            border: 2px solid #2ecc71;
            border-radius: 10px;
            padding: 15px;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🚦 Autonomous Smart Traffic System</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='color: #888; font-size: 16px;'>AI-Powered City Traffic Control Dashboard — Live Simulation</p>",
    unsafe_allow_html=True
)

st.markdown("---")

df = generate_traffic_data()
df = label_congestion(df)
df = predict_congestion(df)
df = detect_accident(df)
df = calculate_signal_timing(df)

route_result = recommend_route(df)

st.subheader("📊 Live Traffic Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    total_vehicles = int(df["Vehicle_count"].sum())
    st.metric("🚗 Total Vehicles", total_vehicles)

with col2:
    avg_speed = round(df["avg_speed_kmph"].mean(), 1)
    st.metric("💨 Avg Speed (km/h)", avg_speed)

with col3:
    active_accidents = int(df["accident_flag"].sum())
    st.metric("⚠️ Active Accidents", active_accidents)

with col4:
    best_route = route_result[
        route_result["recommended"] == True
    ]["route_name"].values

    best_route_name = best_route[0] if len(best_route) > 0 else "N/A"

    st.metric("🗺️ Best Route", best_route_name)

st.markdown("---")

st.subheader("📈 Live Congestion Monitor")

color_map = {
    "Low": "#2ecc71",
    "Medium": "#f39c12",
    "High": "#e74c3c"
}

congestion_chart = px.bar(
    df,
    x="location",
    y="Vehicle_count",
    color="predicted_congestion",
    color_discrete_map=color_map,
    title="Vehicle Count per Junction",
    labels={
        "Vehicle_count": "Vehicle Count",
        "location": "Junction"
    },
    template="plotly_dark"
)

st.plotly_chart(congestion_chart, use_container_width=True)

st.markdown("---")

st.subheader("🚨 Accident Detection Alerts")

accident_df = df[df["accident_flag"] == True]

if len(accident_df) > 0:

    for _, row in accident_df.iterrows():

        st.markdown(
            f"""
            <div class='accident-alert'>
                ⚠️ ALERT: {row['location']} —
                {row['alert_message']}
                | Risk Score: {row['accident_risk_score']}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

else:
    st.success("✅ No accidents detected.")

st.markdown("---")

st.subheader("🗺️ Route Recommendation")

col_left, col_right = st.columns([1, 2])

with col_left:

    if best_route_name != "N/A":

        recommended_row = route_result[
            route_result["recommended"] == True
        ].iloc[0]

        st.markdown(
            f"""
            <div class='route-box'>
                <h3>Recommended Route</h3>
                <h2>{recommended_row['route_name']}</h2>
                <p>Junctions: {recommended_row['junctions']}</p>
                <p>Traffic Score: {round(recommended_row['traffic_score'], 1)}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

with col_right:

    route_chart = px.bar(
        route_result,
        x="route_name",
        y="traffic_score",
        color="recommended",
        color_discrete_map={
            True: "#2ecc71",
            False: "#e74c3c"
        },
        title="Route Traffic Score Comparison",
        labels={
            "traffic_score": "Traffic Score",
            "route_name": "Route"
        },
        template="plotly_dark"
    )

    st.plotly_chart(route_chart, use_container_width=True)

st.markdown("---")

st.subheader("🔍 Intersection Control Table")

display_columns = [
    "location",
    "Vehicle_count",
    "avg_speed_kmph",
    "predicted_congestion",
    "accident_status",
    "alert_message",
    "green_time",
    "signal_note"
]

st.dataframe(
    df[display_columns],
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

st.subheader("🚦 Signal Timing Control")

df["green_time_numeric"] = (
    df["green_time"]
    .str.extract(r'(\d+)')
    .astype(int)
)

signal_color_map = {
    "Extended": "#e74c3c",
    "Normal Caution": "#f39c12",
    "Normal": "#2ecc71",
    "EMERGENCY OVERRIDE": "#9b59b6"
}

signal_chart = px.bar(
    df,
    x="green_time_numeric",
    y="location",
    color="signal_note",
    color_discrete_map=signal_color_map,
    orientation="h",
    title="Green Light Duration per Junction",
    labels={
        "green_time_numeric": "Green Light (seconds)",
        "location": "Junction"
    },
    template="plotly_dark"
)

st.plotly_chart(signal_chart, use_container_width=True)

st.markdown("---")

st.subheader("🔄 Auto Refresh")

auto_refresh = st.checkbox(
    "Enable Auto Refresh (every 5 seconds)"
)

if auto_refresh:
    st.info("🔄 Refreshing dashboard...")
    time.sleep(5)
    st.rerun()

st.markdown("---")

st.markdown(
    """
    <p style='text-align:center; color:#555;'>
        Autonomous Smart Traffic System |
        Built with Python & Streamlit
    </p>
    """,
    unsafe_allow_html=True
)