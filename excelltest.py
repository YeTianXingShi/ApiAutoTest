import openpyxl

file = 'Files/手工单正常.xlsx'
file2 = '1234.xlsx'
wb = openpyxl.load_workbook(file2)
sheet = wb.worksheets[0]

print(sheet['A1'].value)
sheet['A1'].value = '11112s111'

wb.save('1234.xlsx')
