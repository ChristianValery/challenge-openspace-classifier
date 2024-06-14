import pandas as pd

# Correcting the file path issue
file_name = r"C:\Users\ankin\Downloads\excel_Antoine.xlsx"

# Reading the Excel file
df = pd.read_excel(file_name)

# Converting the 'Colleagues' column to a list
Colleagues_list = df['Colleagues'].tolist()

# Printing the list of colleagues
print(Colleagues_list)