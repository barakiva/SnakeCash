import os
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime
import os
import pandas as pd
from datetime import datetime

load_dotenv()
# New column names (assuming you have 10 columns)
new_column_names = [
    "Date",
    "Vendor Name",
    "Amount",
    "Currency",
    "Amount (Charged)",
    "Currency (Charged)",
    "Transaction ID",
    "Notes",
]
# Read the vendors from the .env file
vendors = os.getenv("USER_VENDORS").split(",")

def sum_for_vendors(df, vendors_list, value_column, vendor_column):
    # Filter the DataFrame to include only the rows where the vendor is in the vendors_list
    filtered_df = df[df[vendor_column].isin(vendors_list)]

    # Sum the values in the specified value_column
    total_sum = filtered_df[value_column].sum()

    return total_sum


# Initialize a dictionary to store dataframes with sheet names
dfs = {}

# Iterate through each file and load it into a dictionary
folder_path = "reports"

for file in os.listdir('reports'):
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path) and file_path.endswith(".xls"):
        df = pd.read_excel(file_path, sheet_name=0)
        # Clean
        df = df.iloc[5:]
        df.columns = new_column_names
        # Find date
        cell_date = df.iloc[1]["Date"]
        date = datetime.strptime(cell_date, "%d/%m/%Y")
        month_name = date.strftime("%B")
        spend = sum_for_vendors(df, vendors, "Amount", "Vendor Name")
        print(f'Food spend for {month_name} is: {spend}')
        # Store the dataframe with the corresponding sheet name
        dfs[month_name] = df


# Create a new Excel file with all the sheets
with pd.ExcelWriter("out/combined_months.xlsx", engine='openpyxl') as writer:
    for sheet_name, df in dfs.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

# Convert the combined Excel file to CSV
combined_csv_path = "out/combined_months.csv"
combined_df = pd.concat(dfs.values(), ignore_index=True)
combined_df.to_csv(combined_csv_path, index=False)

print(f"CSV file created at: {combined_csv_path}")


def sum_for_vendors(df, vendors_list, value_column, vendor_column):
    # Filter the DataFrame to include only the rows where the vendor is in the vendors_list
    filtered_df = df[df[vendor_column].isin(vendors_list)]

    # Sum the values in the specified value_column
    total_sum = filtered_df[value_column].sum()

    return total_sum


# Initialize a dictionary to store dataframes with sheet names
dfs = {}


def monthly_spend_by_vendor(vendor, df):
    # Group by 'Vendor Name' and sum the 'Amount' column
    monthly_spend = df[df["Vendor Name"] == vendor]["Amount"].sum()
    # Truncate to 2 significant figures
    monthly_spend = round(monthly_spend, 2)
    return monthly_spend


# Iterate through each file and load it into a dictionary
folder_path = "reports"

for file in os.listdir('reports'):
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path) and file_path.endswith(".xls"):
        df = pd.read_excel(file_path, sheet_name=0)
        # Clean
        df = df.iloc[5:]
        df.columns = new_column_names
        # Find date
        cell_date = df.iloc[1]["Date"]
        date = datetime.strptime(cell_date, "%d/%m/%Y")
        month_name = date.strftime("%B")
        # print(f"Processing file: {file_path} for month: {month_name}")
        spend = sum_for_vendors(df, vendors, "Amount", "Vendor Name")
        print(f'Food spend for {month_name} is: {spend}')
        # Store the dataframe with the corresponding sheet name
        dfs[month_name] = df


# Create a new Excel file with all the sheets
with pd.ExcelWriter("out/combined_months.xlsx", engine='openpyxl') as writer:
    for sheet_name, df in dfs.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

# Convert the combined Excel file to CSV
combined_csv_path = "out/combined_months.csv"
combined_df = pd.concat(dfs.values(), ignore_index=True)
combined_df.to_csv(combined_csv_path, index=False)

print(f"CSV file created at: {combined_csv_path}")
