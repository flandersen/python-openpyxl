from openpyxl import Workbook

mywb = Workbook()
mysheet = mywb.active

mysheet['A3'] = 'Tall row'
mysheet['F1'] = 'Wide column'

mysheet.row_dimensions[3].height = 65
mysheet.column_dimensions['F'].width = 25

mywb.save('change_height_and_width.xlsx')
