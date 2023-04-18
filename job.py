import pandas as pd
import streamlit as st

# Read the CSV file
df = pd.read_csv('job.csv')

# Display the table
st.write(df)
