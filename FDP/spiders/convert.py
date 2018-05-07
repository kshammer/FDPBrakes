import csv
output = open("out.txt", "w")
with open('reilly.csv', newline="") as f:
    for row in f:
        row = "\"" + row[:-2] + "\"" + "," 
        output.write(row)
