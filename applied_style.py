from openpyxl import Workbook
from openpyxl.styles import Font

mywb = Workbook()
mysheet = mywb.get_sheet_by_name('Sheet')

italic32Font = Font(size=32, italic=True)

cell = mysheet['F6']
cell.font = italic32Font
cell.value = 'Applying Styles!'

mywb.save('applied_style.xlsx')
