excel_file_loc = r'C:\Users\parvatithalal\PycharmProjects\Captcha_Auto_Project\Input\Input Data.xlsx'
excel_data = pd.read_excel(excel_file_loc,sheet_name='Sheet1',engine='openpyxl')
df = pd.DataFrame(excel_data)

df.to_excel("Test.xlsx")