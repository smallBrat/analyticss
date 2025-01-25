import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files
compartive_statement = pd.read_csv('Country/RHS-2019-Comparative-Statements-2019-Statement-11C.csv')
rural_achievement = pd.read_csv('Country\RHS-2019-Section-IX-Rural-Health-Care-Some-parameters-of-achievement-Table-69.csv')

def plot_state_comparison(state_name):
    # Filter data for the selected state
    state_data = compartive_statement[compartive_statement['State/UT'] == state_name]
    
    # Get the top two states based on 2019 Nursing Staff In Position
    top_states = compartive_statement.nlargest(2, '2019 - Nursing Staff - In Position - (P)')
    
    # Combine the selected state data with the top states data
    comparison_data = pd.concat([state_data, top_states])
    
    # Plot the data
    comparison_data.plot(x='State/UT', y=['2019 - Nursing Staff - Required1 - (R)', '2019 - Nursing Staff - Sanctioned - (S)', '2019 - Nursing Staff - In Position - (P)'], kind='bar')
    plt.title(f'Nursing Staff Comparison for {state_name} with Top 2 States')
    plt.xlabel('State/UT')
    plt.ylabel('Number of Nursing Staff')
    plt.legend(['Required', 'Sanctioned', 'In Position'])
    plt.show()

# Example usage
state_name = input("Enter the name of the state: ")
plot_state_comparison(state_name)
