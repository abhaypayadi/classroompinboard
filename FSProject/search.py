from openpyxl import *
wb = load_workbook(r'/Users/abhaypayadi/Desktop/Data Set/monday.xlsx')
flag=0
name=input("Enter a name")
sheet = wb.active
column_a=sheet['A']
column_e=sheet['E']


for cell in column_a:
	if(cell.value==name):
		rowno=cell.row
		flag=1
if(flag==0):
	print("no subject found ")	
else:
	for cell in column_e:
		if(cell.row==rowno):
			print(cell.value)
		
wb.save(r'/Users/abhaypayadi/Desktop/Data Set/monday.xlsx')	