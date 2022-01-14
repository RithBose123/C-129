import csv

dataSet1=[]
dataSet2=[]
with open("dataSet1.csv","r")as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        dataSet1.append(row)
with open("dataSet2.csv","r")as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        dataSet2.append(row)
        
header1=dataSet1[0]
header2=dataSet2[0]
planetData1=dataSet1[1:]
planetData2=dataSet2[1:]
header=header1+header2
planetData=[]
for index,datarow in enumerate(planetData1):
    planetData.append(planetData1[index]+planetData2[index])
with open("final.csv","a+")as f:
    csvWriter=csv.writer(f)
    csvWriter.writerow(header)
    csvWriter.writerows(planetData)