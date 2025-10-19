import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(page_title="I Hug Trees - Melbourne Greenness", page_icon="🌳")

st.title("🌿 Greenness Around Melbourne")
st.write("""
Welcome to **I Hug Trees**, where we explore how cities breathe through their green spaces.
This interactive view uses synthetic greenness data around the **Melbourne region** to visualize
how vegetation might appear from above. Soon, we’ll link this to real NDVI satellite insights
from [ihugtrees.org](https://ihugtrees.org).

Streamlit supports advanced mapping through PyDeck, Folium, and Kepler.gl — ideal for
urban ecology, predictive analytics, and tree-cover studies.
""")

# Generate random green-cover sample data around Melbourne CBD
chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [-37.8136, 144.9631],
   columns=['lat', 'lon']
)

# Create interactive 3D map
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/satellite-streets-v12",
    initial_view_state=pdk.ViewState(
        latitude=-37.8136,
        longitude=144.9631,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[139, 195, 74, 160]',  # spring green tone 🌱
            get_radius=200,
        ),
    ],
))

st.markdown("""
---
### 💚 About I Hug Trees
At [ihugtrees.org](https://ihugtrees.org), we combine data, emotion, and purpose — connecting
remote sensing, urban ecology, and AI-driven insights to create a greener planet.  
Explore our upcoming projects and city-wise greenness reports soon at:
- [Research Portal](https://research.ihugtrees.org)
- [Home Page](https://ihugtrees.org)
""")
