import xlrd
'''
1. open_workbook will return a workbook reference, and now control is available on workbook now
2. sheet_by_name will make us let us work on desired sheet in excel file
3 cell_value('which row ?', 'which column(first column is 0)')
'''
workbook = xlrd.open_workbook('Data_file.xls')
sheet = workbook.sheet_by_name("Sheet1")
row_count = sheet.nrows
cols_count = sheet.ncols
print(row_count)
print(cols_count)
for curr_row in range(1, row_count):
    username = sheet.cell_value(curr_row, 0)
    password = sheet.cell_value(curr_row, 1)
    print(username+"  "+password)


