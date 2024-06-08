import pandas as pd

# خواندن داده‌ها از فایل TXT
file_path = 'data.txt'
df = pd.read_csv(file_path, delimiter=',')

# نوشتن داده‌ها به فایل Excel
excel_file_path = 'data.xlsx'
df.to_excel(excel_file_path, index=False)

print(f'Data has been successfully converted from {file_path} to {excel_file_path}')
