import pandas as pd
import streamlit as st

# Read the CSV file
df = pd.read_csv('https://raw.githubusercontent.com/snvice/allocations/main/job.csv')

# Add a header
st.header('Allocations', font_size = 20)

# Display the table
st.write(df)
