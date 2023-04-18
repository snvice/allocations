import pandas as pd
import streamlit as st
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# Read the CSV file
df = pd.read_csv('https://raw.githubusercontent.com/snvice/allocations/main/job.csv')

# Set the page configuration to fit on a mobile screen
st.set_page_config(layout="centered")

##############################################################################################################################################################

# Calculate the total number of values in the DataFrame
total_values = df.count().sum()

# Calculate the reference value for the delta indicator
reference = df.count().sum() - (df.size - df.count().sum()) 

# Create the figure for the indicator
fig = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = total_values,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Pending Verification", 'font': {'size': 20}},
    delta = {'reference': reference, 'decreasing': {'color': "red"}, 'increasing': {'color': "green"}},
    gauge = {
        'axis': {'range': [None, 30], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "darkblue"},
        'bgcolor': "white",
        'borderwidth': 3,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 12], 'color': 'limegreen'},
            {'range': [12, 24], 'color': 'yellowgreen'},
            {'range': [24, 36], 'color': 'Crimson'}],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': 90}}))

# Customize the layout of the figure
fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"}, height=300, width=400)

# Display the figure in the Streamlit app
st.plotly_chart(fig)

#############################################################################################################################################################


# Add a header
st.subheader('Allocations')

# Display the table
st.write(df,index=False)
