#Before beginnning convert the whole file into text formate if possible

import pandas as pd

excel_file_path = 'file.excel'  #if file is in the same path as .py file
df = pd.read.excel(excel_file_path)

print(df.head(2))

for column in df.columns:
    df[column] = df[column].str.replace(r'\W',"")

df.to_excel("removed_characters.xlsx")  #Output to new excel sheet
