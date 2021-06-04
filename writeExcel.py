from openpyxl.workbook import Workbook

workbook = Workbook()
sheet =workbook.active

sheet['A1'] = 'Hello'
sheet['B1'] = 'world!!!'

#workbook.save(filename='hello_world.xlsx')
workbook.save(filename='hello_worlds.csv')
print('succesfully saved !!! ')

