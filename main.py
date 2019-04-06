import xlsxwriter

workbook = xlsxwriter.Workbook('Hello.xlsx')
worksheet = workbook.add_worksheet()

row = 0
column = 0


file = open("output.txt","r",encoding="utf8")   # Reading the file using the utf8 encoding or sinhala words would give errors

  
for line in file:
  #print(line)

  fields = line.split(";")  # the line is splitted into parts using ; delimiter
  
  if (len(fields) > 1):
      
      #print(fields[10])

      #worksheet.write('A1', fields[0])

      for item in fields:         # Writing the data to a Excel file
          worksheet.write(row, column, item)
          column += 1
         
      row += 1
      column = 0
  
  
  
workbook.close()
file.close()
