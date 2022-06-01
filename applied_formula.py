from openpyxl import Workbook

mywb = Workbook()
mysheet = mywb.active

mysheet['A2'] = 500
mysheet['A3'] = 800
mysheet['A4'] = '=SUM(A2:A3)'

mywb.save('applied_formula.xlsx')
