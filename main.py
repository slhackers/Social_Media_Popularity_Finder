from textblob import TextBlob
import xlrd
import xlsxwriter

workbook = xlsxwriter.Workbook('Hello.xlsx')
worksheet = workbook.add_worksheet()

dateAndTimeArray = [];
dateArray = [];



if __name__ == '__main__':

    workbook = xlsxwriter.Workbook('Hello.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    column = 0

    isAHash = 0
    isAMention = 0

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

    wb = xlrd.open_workbook("Hello.xlsx")

    sheet = wb.sheet_by_index(0)

    sheet.cell_value(0, 0)
   

    for i in range(sheet.nrows):
        #print(sheet.cell_value(i,1))

        if sheet.cell_value(i, 1) != "date":
            dateAndTimeArray = sheet.cell_value(i, 1).split(" ")
            dateArray.append(dateAndTimeArray[0])

                

    for j in dateArray:
        print(j)
