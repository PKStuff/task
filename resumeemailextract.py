import PyPDF2
import os
import re
import csv

path = input("Enter the absolute path:")
os.chdir(path)

files = os.listdir(os.getcwd())

data = []

for file in files:
    if file.endswith('pdf'):
        data.append(file)

print(data)
alldata = []

for fl in data:
    pdfFileObject = open(fl, 'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

    pageObj = pdfReader.getPage(0)

    data = pageObj.extractText()

    test = re.findall(r'[A-Za-z]+.?[A-Za-z0-9]*@[A-Za-z]+.[a-z]{1,3}', data)
    alldata.append(test)

with open(r'file.csv','a') as f:
    writer = csv.writer(f)
    for char in alldata:
        writer.writerow(char)
    print("Successfully written to file.csv file.")





