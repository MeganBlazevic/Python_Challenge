import os
import csv
#csvpath= os.path.join('..','ClassHomework/Python_Challenge/PyBank/budget_data/csv')
budget_data= os.path.join('..','Resources','budget_data.csv')

#from sympy import O

with open(budget_data) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csvheader=next(csvfile)
    print(f"Header:{csvheader}")

    monthcount=0
    total=0
    average_change=0
    date=[]
    profits=[]
    previous_profits=0
    difference=[]
    total_difference=0
    increase={"month":"","profits":0}
    decrease={"months":"","losses":0}

    for row in csvreader:
        monthcount +=1
        total += int(row[1])
