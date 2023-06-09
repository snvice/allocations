import streamlit as st
from streamlit.components.v1 import components
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="scanning")

# Home page
def home():
    
    ##########################################################################################################################################################

    import streamlit as st

# rest of your code here


    # Set up the title with a larger font size, a custom color, and an underline
    st.markdown("<h1 style='text-align: center; color: #FF6600; font-size: 45px; text-decoration: overline dotted #33afff; font-family:Fixedsys;'>Scan Squad</h1>", unsafe_allow_html=True)

    #########################################################################################################################################################

    import time
    import requests
    import streamlit as st
    from streamlit_lottie import st_lottie

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Load the Lottie animation from a URL
    lottie_url_hello = "https://assets9.lottiefiles.com/packages/lf20_Che8IZ2raX.json"
    lottie_hello = load_lottieurl(lottie_url_hello)

    # Display the animation with reduced dimensions
    st_lottie(lottie_hello, speed=1, width=225, height=225, key="hello")

    #########################################################################################################################################################

    # Read the CSV file
    df = pd.read_csv('https://raw.githubusercontent.com/snvice/allocations/main/job.csv')

    # Set the page configuration to fit on a mobile screen
    #st.set_page_config(layout="centered")

    ##############################################################################################################################################################

    # Add a header
    st.subheader('Continuing tasks')

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
        #delta = {'reference': reference, 'decreasing': {'color': "red"}, 'increasing': {'color': "green"}},
        gauge = {
            'axis': {'range': [None, total_values], 'tickwidth': 1, 'tickcolor': "darkblue"},
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
    fig.update_layout(paper_bgcolor = "white", font = {'color': "darkblue", 'family': "Arial"}, height=340, width=400)

    # Display the figure in the Streamlit app
    st.plotly_chart(fig, margin=(10, 10, 10, 10))

    #############################################################################################################################################################
    
    st.subheader('')

    
    # Display the table
    st.write(df,index=False)

    ##########################################################################################################################################################
    
    # Load the Lottie animation from a URL
    lottie_url_hellooo = "https://assets5.lottiefiles.com/packages/lf20_PcXPXSc857.json"
    lottie_hellooo = load_lottieurl(lottie_url_hellooo)

    # Display the animation with reduced dimensions
    st_lottie(lottie_hellooo, speed=1, width=200, height=200, key="hello3")
    
    
    
    #########################################################################################################################################################
    # Add a header
    # st.subheader('')

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
    #st.pyplot(fig)


    #############################################################################################################################################################

    # Load the Lottie animation from a URL
    lottie_url_helloo = "https://assets4.lottiefiles.com/private_files/lf30_gd2unfh8.json"
    lottie_helloo = load_lottieurl(lottie_url_helloo)

    # Display the animation with reduced dimensions
    #st_lottie(lottie_helloo, speed=1, width=250, height=250, key="hello2")

    ##########################################################################################################################################################

    # Add a text input widget to allow the user to search
    search_term = st.text_input("Search")

    # Add a button to trigger the search
    search_button = st.button("Search")

    # Convert dataframe to string
    df_str = df.astype(str)

    # Check if the search term matches any columns
    if search_button and search_term:
        match_found = False
        for col in df_str.columns:
            for i, row in enumerate(df_str[col]):
                if search_term in row:
                    st.write(f" {col}  {row}.")
                    match_found = True
        if not match_found:
            st.write(f"No match found for '{search_term}'.")


    # Add your content for the home page here

# Second page
def second_page():
    
    # Add your content for the second page here
    # Add a header
    st.subheader('All Allocations')
    df = pd.read_csv('https://raw.githubusercontent.com/snvice/allocations/main/lvoh.csv')     
    st.write(df,index=False)
    
    st.subheader('')
    
    st.subheader('Complete')
    # Read the CSV file
    df = pd.read_csv('https://raw.githubusercontent.com/snvice/allocations/main/complete.csv')     
    st.write(df,index=False)
    
    ##########################################################################################################################

# Sidebar navigation
menu = ["Home", "Admininja"]
choice = st.sidebar.selectbox("Select a page", menu)

# Display the selected page
if choice == "Home":
    home()
elif choice == "Admininja":
    second_page()
