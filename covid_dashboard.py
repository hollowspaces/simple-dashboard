from enum import unique
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Read data from following link
data = pd.read_csv('https://raw.githubusercontent.com/hollowspaces/Datasets/master/covid_19_indonesia_time_series_all.csv')

st.markdown("Dashboard by Sri Puji Astuti - Kelompok 7 - Bombe Class")

# Create title
st.title("INDONESIA COVID-19 DASHBOARD")
st.markdown("The dashboard will help you to get to know \
more about the information of COVID-19 cases in Indonesia.")

# Create sidebar title
st.sidebar.title("Select Visual Charts")
st.sidebar.markdown("Select the Charts/Plots accordingly:")

# Create dataframe
show_data = st.sidebar.checkbox("Show Dataframe", True, key = 1)

# Create sidebar selectbox to select plot type
chart_visual = st.sidebar.selectbox(
    'Select Charts/Plot type',
    ('Line Chart', 'Bar Chart'))

# Create sidebar selectbox to select data based on location in Indonesia
Location = st.sidebar.selectbox(
    'Select Location',
    data.Location.unique())
  
fig = go.Figure()

# Show all data
if show_data:
    st.write(data)

# Divide data per year
Year_2020 = pd.date_range(start='3/1/2020', end='12/31/2020')
Year_2021 = pd.date_range(start='1/1/2021', end='12/3/2021')

# Create sidebar selectbox to select year
select_year = st.sidebar.selectbox(
    'Select Data per Year',
    ['2020', '2021']
)

# Create line chart for case per year
st.markdown("\n")
st.subheader('Total Cases, Total Deaths, and Total Recovered in {}'.format(select_year))
if select_year == '2020':    
    if chart_visual == 'Line Chart':
        fig.add_trace(go.Scatter(
            x = Year_2020, 
            y = data.Total_Cases,
            mode = 'lines',
            name = 'Total Cases'))
        fig.add_trace(go.Scatter(
            x = Year_2020, 
            y = data.Total_Deaths,
            mode = 'lines', 
            name = 'Total Deaths'))
        fig.add_trace(go.Scatter(
            x = Year_2020, 
            y = data.Total_Recovered,
            mode = 'lines', 
            name = 'Total_Recovered'))
        fig.update_layout(  # Update chart layout
            title='Line Chart Indonesia COVID-19 Cases',
            xaxis_title='Year 2020',
            yaxis_title='Total Cases, Total Deaths, and Total Recovered)')
    elif chart_visual == 'Bar Chart':
        fig.add_trace(go.Bar(
            x = Year_2020, 
            y = data.Total_Cases, 
            name = 'Total_Cases'))
        fig.add_trace(go.Bar(
            x = Year_2020, 
            y = data.Total_Deaths, 
            name = 'Total_Deaths'))
        fig.add_trace(go.Bar(
            x = Year_2020, 
            y = data.Total_Recovered, 
            name = 'Total_Recovered'))
        fig.update_layout(  # Update chart layout
            title='Bar Chart Indonesia COVID-19 Cases')
    st.plotly_chart(fig)

# Show data based on location
st.subheader("Show the COVID-19 Cases Based on Selected Location")
st.markdown('You selected: {}'.format(Location))
st.write(data[(data.Location == Location)])

# Create plot to show total case, total deaths, and total recovered in selected Location
st.markdown(" \n")
st.subheader('Total Cases, Total Deaths, and Total Recovered in {}'.format(Location))
chart_data = pd.DataFrame(
     data[(data.Location == Location)],
     columns=['Total_Cases', 'Total_Deaths', 'Total_Recovered'])
st.line_chart(chart_data)