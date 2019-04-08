import xlrd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
#from nltk.stem.porter import PorterStemmer
import xlsxwriter
import enchant
import pandas as pd


di=dict()


e=enchant.Dict("en_GB")

# Give the location of the file 
loc = ("twitter data.xlsx")
words = []
wordsnew = []

# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)

#extracting text column 
for i in range(sheet.nrows): 
    text=sheet.cell_value(i, 4)
    #split into words
    tokens = word_tokenize(text)
    
    # convert to lower case
    tokens = [w.lower() for w in tokens]

    # remove all tokens that are not alphabetic
    words = [word for word in tokens if word.isalpha()]

    #Filter out Stop Words (and Pipeline)
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]

    for w in words:
        if((e.check(w)==1)and(len(w)>2)):
            wordsnew.append(w)


for w in wordsnew:
    if w in di:
        di[w]=di[w]+1
    else:
        di[w]=1

words=di.keys()
count=di.values()



workbook=xlsxwriter.Workbook('generatedData.xlsx')
worksheet=workbook.add_worksheet()

worksheet.write(0,0,'word')
worksheet.write(0,1,'count')

row=1
col=0

for item in words:
    worksheet.write(row,col,item)
    row+=1

row=1
col=1
for item in count:
    worksheet.write(row,col,item)
    row+=1

workbook.close()

df = pd.read_excel('generatedData.xlsx')
word1= df['word'].tolist()
count1 = df['count'].tolist()

#decending order
n=len(count1)
for i in range(n):
    for j in range(0,n-i-1):
        if(count1[j]<count1[j+1]):
            count1[j],count1[j+1]=count1[j+1],count1[j]
            word1[j],word1[j+1]=word1[j+1],word1[j]



workbook=xlsxwriter.Workbook('generatedData.xlsx')
worksheet=workbook.add_worksheet()

worksheet.write(0,0,'word')
worksheet.write(0,1,'count')

worksheet.write(0,5,'word')
worksheet.write(0,6,'count')

row=1
col=0

for item in words:
    worksheet.write(row,col,item)
    row+=1

row=1
col=1
for item in count:
    worksheet.write(row,col,item)
    row+=1


row=1
col=5

for item in word1:
    worksheet.write(row,col,item)
    row+=1

row=1
col=6
for item in count1:
    worksheet.write(row,col,item)
    row+=1


worksheet.write(0,8,'finalword')
worksheet.write(0,9,'finalcount')

row=1
col=8

for item in range(0,50):
    worksheet.write(row,col,word1[item])
    row+=1

row=1
col=9
for item in range(0,50):
    worksheet.write(row,col,count1[item])
    row+=1

workbook.close()

#plotting 





            
