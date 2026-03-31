import csv

file_name = "sample.csv"
with open(file_name, "r") as file:
    reader = csv.reader(file)
    
    row_count = 0
    for row in reader:
        row_count += 1

print("Total number of rows:", row_count)