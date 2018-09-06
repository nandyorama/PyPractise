# Program extracting first column
import xlrd
 
loc = ("Test.xlsx")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
 
for i in range(sheet.nrows):
    #print(sheet.cell_value(i, 0))
	fileName = str(sheet.cell_value(i, 0))+".txt"
	print(fileName)
	f = open(fileName, "w")
	for c in range(sheet.ncols):
		if c+1 < len(range(sheet.ncols)):# The next statement z giving index out of range error as c+1 out of range
			s=str(sheet.cell_value(i, c+1))
			res=s.split('.', 1)[0]
			print(res)
			f.write(str(res))
			f.write("\n")
	f.close()
