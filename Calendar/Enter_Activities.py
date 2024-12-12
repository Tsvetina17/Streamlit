import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title='Enter Activities',
    page_icon='📆',
    layout='wide',
    initial_sidebar_state='expanded'
    )

# Sidebar
with st.sidebar:
    st.sidebar.header('Enter Activities')
    st.sidebar.write('Use this page to enter activities as you wish. They will be added to the calendar and the data will be visualized in the dashboard.')

# File path for storing activities
ACTIVITY_FILE = 'activities.csv'

# Ensure the CSV file exists
def ensure_csv():
    try:
        # Try reading the CSV file to ensure it exists
        pd.read_csv(ACTIVITY_FILE)
    except FileNotFoundError:
        # If the file doesn't exist, create it with the appropriate columns
        df = pd.DataFrame(columns=['Date', 'Activity Type', 'Activity Title', 'Time Planned', 'Time Spent'])
        df.to_csv(ACTIVITY_FILE, index=False)

# Input for adding new activity
def add_activity():
    st.title('Add Activity')
    activity_date = st.date_input('Activity date', min_value=datetime.today())
    activity_type = st.selectbox('Activity type', ['Work', 'Exercise', 'Study', 'Leisure', 'Other'])
    activity_title = st.text_input('Activity title')
    time_planned = st.number_input('Time planned (minutes)', value = None, min_value=1, max_value=1440, step=1)
    time_spent = st.number_input('Time spent (minutes)', value = None, min_value=1, max_value=1440, step=1)

    if st.button('Save Activity'):
        if activity_title and activity_type and activity_date and time_planned and time_spent:
            # Save the activity to the CSV file
            new_activity = pd.DataFrame({
                'Date': [activity_date],
                'Activity Type': [activity_type],
                'Activity Title': [activity_title],
                'Time Planned': [time_planned],
                'Time Spent': [time_spent]  
            })
            # Append the new activity to the CSV file
            new_activity.to_csv(ACTIVITY_FILE, mode='a', header=False, index=False)
            st.success(f'Activity "{activity_title}" saved successfully!')
        else:
            st.error('Please fill all the fields')

# Main function to control the app flow
def main():
    # Ensure the CSV file exists
    ensure_csv()

    add_activity()

if __name__ == '__main__':
    main()
