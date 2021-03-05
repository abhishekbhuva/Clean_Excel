'''
Import Excel
Clean Excel Data
Write back to Excel
'''

import pandas as pd

excel_workbook = 'file.xlsx' #type the File name
sheet1 = pd.read.excel(excel_workbook, sheet_name='Sheet1')  #Sheet1 make sure it's the name of Sheet
#print(sheet1.head(10))

first_names_list =[]
last_names_list = []

excel_names = sheet1['First Name, Last Name']
#print(excel_names)

for name in excel_names:
    first_name, last_name = name.split(' ',1)
    first_names_list.append(first_name.upper())
    last_names_list.append(last_name.upper())

#print(first_names_list)

sheet1.insert(0,"First Name",first_names_list)
sheet1.insert(1,"Last Name",last_names_list)
del sheet1['First Name, Last Name']
print(sheet1.head(10))

Important_numbers = sheet1['Important Number']
pd.to_numeric(Important_numbers)   # Convert data to Numeric using Panda Library
print(Important_numbers)
Edited_Important_Numbers = Important_numbers
sheet1['Important Number'] = Edited_Important_Numbers
print(sheet1.head(10))

sheet1.to_excel("output.xlsx")  #Output file with new data
