import csv

rows = []
fields=[]

with open("input_data.csv", 'r') as file:
    #create a cvs reader object
    csvreader = csv.reader(file)
    fields = csvreader.next()
    for row in csvreader:
        rows.append(row)
        print(row)


        # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))

