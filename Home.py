import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

from utils.postcode_validator import validate_postcode
from services.location_service import get_location_data
from services.property_service import get_house_price_data

# Set page config
st.set_page_config(
    page_title="UK Property Search Dashboard",
    page_icon="🏠",
    layout="wide"
)

# Title and description
st.title("UK Property & Location Dashboard")
st.markdown("""
Welcome to the UK Property and Location Dashboard! This application provides comprehensive information about UK locations by postcode, including:

- **Property Information**: Search for property details and price trends
- **Crime Statistics**: Explore crime data and statistics for UK postcodes
- **Flood Risk**: View flood zone data and assess flood risk
- **Location Data**: View detailed information about UK postcodes

Use the sidebar navigation to explore different features.
""")

# Main content - Feature showcase
st.header("Dashboard Features")

# Create columns for feature highlights
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📊 Property Search")
    st.write("""
    - View detailed property price information
    - Explore house price trends over time
    - Compare prices across property types
    - Analyze yearly price changes
    """)
    if st.button("Go to Property Search", use_container_width=True):
        st.switch_page("pages/0_Property_Search.py")

with col2:
    st.subheader("🚓 Crime Statistics")
    st.write("""
    - Explore crime data by location
    - View crime hotspots on interactive maps
    - Analyze crime type breakdowns
    - Track monthly crime trends
    """)
    if st.button("Go to Crime Map", use_container_width=True):
        st.switch_page("pages/1_Crime_Map.py")
        
with col3:
    st.subheader("🌊 Flood Risk")
    st.write("""
    - View flood zone maps
    - Check flood risk by postcode
    - See Flood Zone 2 and 3 areas
    - Get flood risk assessment
    """)
    if st.button("Go to Flood Risk Map", use_container_width=True):
        st.switch_page("pages/2_Flood_Risk.py")

# Add a section for getting started
st.header("Getting Started")
st.write("""
To get started, simply select a feature from the sidebar navigation or use the buttons above.
Then enter a UK postcode to retrieve information for that location.
""")

# Example postcodes
st.subheader("Example postcodes to try:")
example_postcodes = ["SW1A 1AA", "E14 9GE", "M1 1AE", "EH1 1YZ", "CF10 1EP"]
st.write(", ".join(example_postcodes))

# Footer
st.markdown("---")
st.caption("© 2023 UK Property & Location Dashboard | Data sources: UK Land Registry, OpenStreetMap, Police UK Data API, Environment Agency Flood Map for Planning")