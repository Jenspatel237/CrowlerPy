import csv

with open('names.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)

    thewriter.writerow(['jens', 'hsj', 'hhjsd'])


