import csv

coluna1= list(range(501))
coluna2= list(range(500,1001))
rowt =['coluna1', 'coluna2']

with open ('teste.csv', mode='w',newline='\n') as wt:
    wter=csv.writer(wt, delimiter=';')
    wter.writerow(rowt)
for x in coluna1:
    rowt =[coluna1[x], coluna2[x]]
    with open ('teste.csv', mode='a', newline='\n') as wt1:
        wter=csv.writer(wt1, delimiter=';')
        wter.writerow(rowt)
