import pandas as pd
import os

# Define the file path
base_dir = os.path.dirname(
    os.path.abspath(__file__)
)  # Get the current script directory
print(f"base_dir :: ${base_dir}")
file_path = os.path.join(
    base_dir, "../data/SalesData.xlsx"
)  # Adjust the path relative to src or util

# Read the Excel file
try:
    excel_data = pd.ExcelFile(file_path)

    # Dictionary to hold data from all sheets
    sheets_data = {}

    for sheet_name in excel_data.sheet_names:
        sheets_data[sheet_name] = excel_data.parse(sheet_name)

    # Example: Print data from each sheet
    for sheet_name, data in sheets_data.items():
        print(f"Data from sheet: {sheet_name}")
        print(data)
        print("\n")
except FileNotFoundError:
    print(f"File not found at: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
