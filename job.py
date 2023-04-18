import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

##########################################################################################################################################################

# Read the CSV file
df = pd.read_csv('https://raw.githubusercontent.com/snvice/allocations/main/job.csv')

# Set the page configuration to fit on a mobile screen
st.set_page_config(layout="centered")

##############################################################################################################################################################

# Add a header
st.subheader('Ongoing tasks')

# Calculate the total number of values in the DataFrame
total_values = df.count().sum()

# Calculate the reference value for the delta indicator
reference = df.count().sum() - (df.size - df.count().sum()) 

# Create the figure for the indicator
fig = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = total_values,
    domain = {'x': [0, 1], 'y': [0, 1]},
    #title = {'text': "Pending Verification", 'font': {'size': 20}},
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
fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"}, height=340, width=400)

# Display the figure in the Streamlit app
st.plotly_chart(fig, margin=(20, 20, 20, 20))

#############################################################################################################################################################

# Add a header
st.subheader('N0. of assignments in progress')

# Count non-null values for each column and plot as horizontal stacked bar chart
fig, ax = plt.subplots()
df.notnull().sum().plot(kind='barh', stacked=True, color=sns.color_palette('rocket'))

# Set labels and title
ax.set_xlabel('Count')
#ax.set_title('Pending')

# Remove the background and show only the lines
ax.set_facecolor('none')
ax.spines['bottom'].set_color('gray')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(axis='y', which='both', length=0)

# Display the plot in Streamlit
st.pyplot(fig)


#############################################################################################################################################################

# Add a header
st.subheader('Allocations')

# Display the table
st.write(df,index=False)

##########################################################################################################################################################

# Create a search box
search_term = st.text_input("Batch no. ")

# Filter the DataFrame based on the search term
filtered_data = data[data.apply(lambda row: row.astype(str).str.contains(search_term).any(), axis=1)]

# Display the filtered DataFrame
if not filtered_data.empty:
    st.write("Showing results for term: ", search_term)
    st.write(filtered_data)
else:
    st.write("No results found for term: ", search_term)




