import streamlit as st
import pandas as pd
import numpy as np
import time

# --- 1. PAGE CONFIGURATION ---
# Sets the browser tab title and layout style
st.set_page_config(page_title="Advanced ML Dashboard", layout="wide")

# --- 2. SIDEBAR & NAVIGATION ---
# The Sidebar acts as a 'Navigation Menu' or 'Control Panel'
st.sidebar.header("User Settings")
user_theme = st.sidebar.radio("Choose App Mode:", ("Light", "Dark", "Custom"))

# --- 3. TITLE & DESCRIPTION ---
st.title("🚀 Advanced AI-ML Streamlit Dashboard")
st.markdown("""
This application serves as a **dynamic data source** and **UI interface**. 
Unlike Flask, Streamlit handles the 'Request-Response' cycle automatically.
""")

# --- 4. DATA CREATION & DISPLAY ---
# Using columns for a cleaner layout (Jinja2-like grid system but easier)
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Structured Data Table")
    df = pd.DataFrame({
        'ID': [101, 102, 103, 104],
        'Feature_X': [1.2, 2.5, 3.8, 4.1],
        'Category': ['A', 'B', 'A', 'C']
    })
    # st.dataframe provides an interactive, searchable table
    st.dataframe(df, use_container_width=True)

with col2:
    st.subheader("📈 Real-time Analytics")
    # Generating random weights (Simulating ML Model output)
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Loss', 'Accuracy', 'Validation']
    )
    # Built-in interactive visualization
    st.line_chart(chart_data)

# --- 5. INTERACTIVE WIDGETS & LOGIC ---
st.divider() # Adds a horizontal line for visual separation
st.header("🎛️ Interactive Model Controls")

name = st.text_input("Enter Student/User Name:", placeholder="e.g., John Doe")
age = st.slider("Select Input Value (Variable Rule):", 0, 100, 25)

# Conditional Logic (Matches the 'if-else' logic from Jinja2)
if name:
    # Use st.success/warning/info/error for formatted feedback
    if age >= 50:
        st.success(f"Hello {name}! The model predicts a SUCCESS status.")
    else:
        st.warning(f"Hello {name}! The model predicts a FAILURE status.")

# --- 6. ADVANCED INPUTS ---
col3, col4 = st.columns(2)

with col3:
    options = ['Python', 'Java', 'C++', 'JavaScript']
    choice = st.selectbox("Select ML Backend Language:", options)
    st.info(f"System configured for: {choice}")

with col4:
    # File Uploader (Acts as the 'Data Source' for ML ingestion)
    uploaded_file = st.file_uploader("Upload Dataset (CSV only)", type="csv")
    
    if uploaded_file is not None:
        # Progress bar simulation (Enhances User Experience)
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        
        data = pd.read_csv(uploaded_file)
        st.write("### Preview of Uploaded Data")
        st.table(data.head(5)) # st.table is static (non-scrollable)

# --- 7. FOOTER & STATUS ---
st.sidebar.success("Status: Application Running")