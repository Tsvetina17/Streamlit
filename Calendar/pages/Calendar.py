import streamlit as st
import pandas as pd
import calplot
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title='Calendar',
    page_icon='📆',
    layout='wide',
    initial_sidebar_state='expanded'
    )

# Sidebar
with st.sidebar:
    st.sidebar.header('Calendar')
    st.sidebar.write('Select a date from the calendar to view all the activities scheduled for the day, how much time you planned for them and how much time you actually spent.')

# File path for storing activities
df = pd.read_csv('activities.csv')

# Convert the Date column into a datetime format and drop any rows with invalid dates.
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df.dropna(subset=['Date'], inplace=True)  # Drop rows with invalid dates

# Convert the columns Time Spent and Time Planned to integers 
df['Time Spent'] = df['Time Spent'].astype('int32')
df['Time Planned'] = df['Time Planned'].astype('int32')

# Display Calendar with Activities
def display_calendar(df):
    st.title('Activity Calendar')

    # Group activities by date
    activity_counts = df.groupby('Date').size()

    # Convert the activity counts to a Series with datetime index for calplot
    activity_series = pd.Series(activity_counts, index=pd.to_datetime(activity_counts.index))

    # Plot the calendar
    calplot.calplot(activity_series, cmap='YlGnBu', colorbar=True, figsize=(10, 6))

    # User selects a date
    selected_date = st.date_input('Select a date to view activities', min_value=min(df['Date']), max_value=max(df['Date']))

    # Display the activities for the selected date
    activities_on_date = df[df['Date'] == pd.to_datetime(selected_date)]

    if not activities_on_date.empty:
        st.write(f'Activities for {selected_date}:')
        for idx, row in activities_on_date.iterrows():
            st.write(f'- **{row['Activity Type']}** ({row['Activity Title']}): {row['Time Planned']} minutes planned and {row['Time Spent']} minutes spent.')
    else:
        st.write(f'No activities found for {selected_date}.')

# Main function to control the app flow
def main():

    st.session_state.df = df  # Store data in session state to persist across pages
    display_calendar(df)

if __name__ == '__main__':
    main()