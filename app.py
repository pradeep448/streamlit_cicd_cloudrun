import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("🚀 My First Streamlit App")

# Header and Text
st.header("Welcome!")
st.write("This app was built in just a few lines of Python.")

# Interactive Input: Slider
name = st.text_input("What's your name?", "Guest")
age = st.slider("Select your age", 0, 100, 25)

st.success(f"Hello {name}! You are {age} years old.")

# Generate some random data for a chart
st.subheader("Random Data Visualization")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

# Display a Line Chart
st.line_chart(chart_data)

# Show a table
if st.checkbox("Show raw data"):
    st.write(chart_data)