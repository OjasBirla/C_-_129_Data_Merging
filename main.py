import csv
import pandas as pd 

Data = []

with open("Output.csv") as f:
    reader = csv.reader(f)

    for x in reader:
        Data.append(x)

Header = [0]
Planet_Data = Data[1:]

# print(Planet_Data)

for data in Planet_Data:
    # print(data)
    # print(data[4])
    if data[4] != "":
        NewValue = float(data[4]) * 0.102763
        data[4] = NewValue

for data in Planet_Data:
    NewValue = float(data[3]) * 0.000954588
    data[3] = NewValue

with open("Final.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(Header)
    csv_writer.writerows(Planet_Data)
