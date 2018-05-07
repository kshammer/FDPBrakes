import csv
output = open("out.txt", "w")
with open('NAPA.csv', newline="") as f:
    for row in f:
        row = "\"" + row[:-1] + "\"" + "," 
        output.write(row)
