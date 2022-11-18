import csv
import sys

def print_file_content(fileName):
    with open(fileName, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)

print_file_content("./data/DKstat_bykoder.csv")

strings = ["test", "test2", "test3"]
def write_list_to_file(list):
    for string in strings:
        with open("02-output.txt", 'a+') as file:
            file.write(f"{string}\n")
            file.close()

write_list_to_file(strings)

def read_csv(fileName):
    csvList = []
    with open(fileName, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            csvList.append(row)

    print(csvList)

#read_csv("./data/DKstat_bykoder.csv")
read_csv(sys.argv[1])