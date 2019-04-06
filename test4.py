import matplotlib.pyplot as plt
import xlrd

hashTagArray = [];
mentionsArray = [];




 
if __name__ == '__main__':

    isAHash = 0
    isAMention = 0

    


    wb = xlrd.open_workbook("Hello.xlsx")

    sheet = wb.sheet_by_index(0)

    sheet.cell_value(0, 0)


    for i in range(sheet.nrows):

        array1 = sheet.cell_value(i,4).split(" ")

        for j in array1:

            if isAHash == 1:
                hashTagArray.append(j);
                #hashTagArray.append("#"+j);  # Cannot be used since if it is used to calculate the frequent words
                isAHash = 0;

            if isAMention == 1:
                mentionsArray.append(j);
                isAMention = 0;
                
                
            if j == "#":        # For Hashtags
                #print("GO1")
                isAHash = 1;

            if j == "@":        # FOr Mentions
                isAMention = 1;
            

    for x in mentionsArray:
         print(x)

    #print(len(hashTagArray))       
