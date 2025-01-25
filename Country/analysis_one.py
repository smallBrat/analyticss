import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files
# ayush_colleges = pd.read_csv('Country/List_of_Aided_PG_AYUSH_College_0.csv')
phc_chc_data = pd.read_csv('Country/RS_Session_257_AU_282_1.csv')
health_manpower = pd.read_csv('Country/RHS-2019-Section-V-Status-of-Health-Manpower-in-Rural-areas-Table-39.csv')
compartive_statement = pd.read_csv('Country/RHS-2019-Comparative-Statements-2019-Statement-11C.csv')

# Function to plot graphs for a particular state
def plot_state_analysis(state):
    # Filter data for the selected state
    phc_chc_state_data = phc_chc_data[phc_chc_data['State/UT'] == state]
    health_manpower_state_data = health_manpower[health_manpower['State/UT'] == state]

    # Get top 3 states for comparison
    top_3_phc_chc_states = phc_chc_data.groupby('State/UT')['PHCs - Total'].sum().nlargest(3).index
    top_3_health_manpower_states = health_manpower.groupby('State/UT')['District Hospital - In Position'].sum().nlargest(3).index

    # Plot PHCs and CHCs data
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 2, 1)
    phc_chc_comparison_data = phc_chc_data[phc_chc_data['State/UT'].isin(top_3_phc_chc_states) | (phc_chc_data['State/UT'] == state)]
    phc_chc_comparison_data.groupby('State/UT')[['PHCs - Total', 'CHCs - Total']].sum().plot(kind='bar', ax=plt.gca())
    plt.xlabel('State/UT')
    plt.ylabel('Total Count')
    plt.title(f'PHCs and CHCs in {state} and Top 3 States')
    plt.xticks(rotation=90)

    # Plot health manpower data
    plt.subplot(1, 2, 2)
    health_manpower_comparison_data = health_manpower[health_manpower['State/UT'].isin(top_3_health_manpower_states) | (health_manpower['State/UT'] == state)]
    health_manpower_comparison_data.groupby('State/UT')[['District Hospital - In Position', 'Sub District/Sub Divisional Hospital - In Position']].sum().plot(kind='bar', ax=plt.gca())
    plt.xlabel('State/UT')
    plt.ylabel('In Position Count')
    plt.title(f'Health Manpower in {state} and Top 3 States')
    plt.xticks(rotation=90)

    plt.tight_layout()
    plt.show()

# Get user input for the state
state = input("Enter the name of the state: ")
plot_state_analysis(state)
