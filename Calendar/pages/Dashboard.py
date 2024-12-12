import streamlit as st
import pandas as pd
import calplot
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title='Dashboard',
    page_icon='📆',
    layout='wide',
    initial_sidebar_state='expanded'
    )

# Sidebar
with st.sidebar:
    st.sidebar.header('Dashboard')
    st.sidebar.write('Here you can visualize data about your activities as you wish.')

# File path for storing activities
df = pd.read_csv('activities.csv')
