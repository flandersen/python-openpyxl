from openpyxl import Workbook

mywb = Workbook()
mywb.get_sheet_names()

sheet = mywb.active
print(sheet.title)

sheet.title = 'MyNewTitle'
print(mywb.get_sheet_names())

mywb.save('new_excel_file.xlsx')
