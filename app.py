import pandas as pd

# List of uploaded files
file_paths = [
    'reports/Export_3_2024.xls',
    'reports/Export_5_2024.xls',
    'reports/Export_4_2024.xls',
    'reports/Export_6_2024.xls',
    'reports/Export_7_2024.xls',
    'reports/Export_8_2024.xls'
]

# New column names (assuming you have 10 columns)
new_column_names = ['Date', 'Vendor Name', 'Amount', 'Currency', 'Amount (Charged)', 'Currency (Charged)', 'Transaction ID', 'Notes']

# Initialize a dictionary to store dataframes with sheet names
dfs = {}

# Iterate through each file and load it into a dictionary
for file_path in file_paths:
    # Extract month from the file name for sheet name
    sheet_name = file_path.split('/')[-1].split('_')[1].split('.')[0]
    # Load the Excel file
    df = pd.read_excel(file_path, sheet_name=0)
    
    # Rename the columns to new_column_names
    df.columns = new_column_names
    
    # Store the dataframe with the corresponding sheet name
    dfs[sheet_name] = df

# Create a new Excel file with all the sheets
with pd.ExcelWriter('reports/combined_months.xlsx') as writer:
    for sheet_name, df in dfs.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

# Convert the combined Excel file to CSV
combined_csv_path = 'reports/combined_months.csv'
combined_df = pd.concat(dfs.values(), ignore_index=True)
combined_df.to_csv(combined_csv_path, index=False)

print(f"CSV file created at: {combined_csv_path}")
