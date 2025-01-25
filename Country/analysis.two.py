import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files
compartive_statement = pd.read_csv('Country/RHS-2019-Comparative-Statements-2019-Statement-11C.csv')
rural_achievement = pd.read_csv('Country/RHS-2019-Section-IX-Rural-Health-Care-Some-parameters-of-achievement-Table-69.csv')
rural_health_care = pd.read_csv('Country/RHS-2019-Section-IX-Rural-Health-Care-Some-parameters-of-achievement-Table-69.csv')

def plot_comparisons(state_name):
    # Filter data for the selected state
    state_data_comparative = compartive_statement[compartive_statement['State/UT'] == state_name]
    state_data_rural = rural_health_care[rural_health_care['State/UT'] == state_name]

    # Get the top two states based on 2019 Nursing Staff In Position
    top_states_comparative = compartive_statement.nlargest(2, '2019 - Nursing Staff - In Position - (P)')
    top_states_rural = rural_health_care.nlargest(
        2, 'Average Rural Population [mid-year population as on 1st July 2019] covered by a - Sub Centre'
    )

    # Combine the selected state data with the top states data
    comparison_data_comparative = pd.concat([state_data_comparative, top_states_comparative])
    comparison_data_rural = pd.concat([state_data_rural, top_states_rural])

    # Create subplots
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Plot the nursing staff comparison
    comparison_data_comparative.plot(
        x='State/UT',
        y=[
            '2019 - Nursing Staff - Required1 - (R)',
            '2019 - Nursing Staff - Sanctioned - (S)',
            '2019 - Nursing Staff - In Position - (P)',
        ],
        kind='bar',
        ax=axes[0],
        color=['#FF9999', '#99FF99', '#9999FF']
    )
    axes[0].set_title(f'Nursing Staff Comparison for {state_name} with Top 2 States')
    axes[0].set_xlabel('State/UT')
    axes[0].set_ylabel('Number of Nursing Staff')
    axes[0].legend(['Required', 'Sanctioned', 'In Position'], loc='upper left')
    axes[0].tick_params(axis='x', rotation=90)

    # Plot the rural health care comparison
    comparison_data_rural.plot(
        x='State/UT',
        y=[
            'Average Rural Population [mid-year population as on 1st July 2019] covered by a - Sub Centre',
            'Average Rural Population [mid-year population as on 1st July 2019] covered by a - PHC',
            'Average Rural Population [mid-year population as on 1st July 2019] covered by a - CHC',
        ],
        kind='bar',
        ax=axes[1],
        color=['#FFC300', '#00C49F', '#C70039']
    )
    axes[1].set_title(f'Rural Health Care Comparison for {state_name} with Top 2 States')
    axes[1].set_xlabel('State/UT')
    axes[1].set_ylabel('Average Rural Population')
    axes[1].legend(['Sub Centre', 'PHC', 'CHC'], loc='upper left')
    axes[1].tick_params(axis='x', rotation=90)

    # Adjust layout
    plt.tight_layout()
    plt.show()

# Example usage
state_name = input("Enter the name of the state: ")
plot_comparisons(state_name)