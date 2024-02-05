import pandas as pd

# Load the CSV file
file_path = 'extracted_scenarios_old.csv'
data = pd.read_csv(file_path)

# Define the keywords to search for
keywords = ["stripe", "checkout", "paypal"]

# Initialize columns for the keywords in the DataFrame
for keyword in keywords:
    data[keyword + "_in_scenario"] = 0
    data[keyword + "_in_steps"] = 0


# Function to count occurrences of a keyword in a given text, ignoring commented out lines
def count_keyword(text, keyword):
    return sum(keyword in line for line in text.split('\n') if not line.strip().startswith('#'))


# Analyze each row for the presence of keywords in scenario and steps
for index, row in data.iterrows():
    scenario = row['Scenario']
    steps = row['Steps']

    for keyword in keywords:
        data.at[index, keyword + "_in_scenario"] = count_keyword(scenario, keyword)
        data.at[index, keyword + "_in_steps"] = count_keyword(steps, keyword)

# Extracting relevant information for the report
report_data = data[['Scenario', 'Steps'] + [k + "_in_scenario" for k in keywords] + [k + "_in_steps" for k in keywords]]

# Save the report data to a new CSV file
output_file_path = 'keyword_analysis_report.csv'
report_data.to_csv(output_file_path, index=False)
