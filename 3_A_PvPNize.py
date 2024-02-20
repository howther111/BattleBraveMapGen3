import csv
import random

outputcsv = ""
with open('input_map_csv.csv') as f:
    reader = csv.reader(f)
    l = [row for row in reader]
    for row in reader:
        print(row)

    xmax = len(l[0])
    ymax = len(l)

    rnd = random.randint(0, 3)

    if rnd == 0:
        l[0][0] = "青"
        l[0][1] = "青"
        l[1][0] = "青"
        l[1][1] = "青"
        l[ymax - 1][xmax - 1] = "赤"
        l[ymax - 2][xmax - 1] = "赤"
        l[ymax - 1][xmax - 2] = "赤"
        l[ymax - 2][xmax - 2] = "赤"
    elif rnd == 1:
        l[0][0] = "赤"
        l[0][1] = "赤"
        l[1][0] = "赤"
        l[1][1] = "赤"
        l[ymax - 1][xmax - 1] = "青"
        l[ymax - 2][xmax - 1] = "青"
        l[ymax - 1][xmax - 2] = "青"
        l[ymax - 2][xmax - 2] = "青"
    elif rnd == 2:
        l[ymax - 1][0] = "青"
        l[ymax - 2][0] = "青"
        l[ymax - 1][1] = "青"
        l[ymax - 2][1] = "青"
        l[0][xmax - 1] = "赤"
        l[1][xmax - 1] = "赤"
        l[0][xmax - 2] = "赤"
        l[1][xmax - 2] = "赤"
    elif rnd == 3:
        l[ymax - 1][0] = "赤"
        l[ymax - 2][0] = "赤"
        l[ymax - 1][1] = "赤"
        l[ymax - 2][1] = "赤"
        l[0][xmax - 1] = "青"
        l[1][xmax - 1] = "青"
        l[0][xmax - 2] = "青"
        l[1][xmax - 2] = "青"

    for row in l:
        print(row)

    outputcsv = l

with open('input_map_csv.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(outputcsv)

