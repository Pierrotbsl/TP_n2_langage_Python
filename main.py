import csv

def createGraph(self, idGraph, filename):
    file = open(filename, "rb")
    try:
        reader = csv.reader(file)
        for row in reader:
            print row
    finally:
        file.close()
