import openpyxl


def excel_update(file, key, value):
    wb = openpyxl.load_workbook(file)
    sheet = wb.worksheets[0]
    value.encode('gbk')
    sheet[key].value = value
    wb.save(file)
    # print("成功将" + str(key) + "的值修改为 " + str(value))
