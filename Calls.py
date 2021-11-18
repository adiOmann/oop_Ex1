import csv


class Calls:
    ro = []
    scores = []
    with open("Ex1_Calls/Calls_a.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            ro.append(row)
    #ro1=ro[0]
    #ro1[4:]
    di = {}
    for row in ro:
        deadLine = row[1:2]
        source = row[2:3]
        dest = row[3:4]
        scores.append(deadLine)
