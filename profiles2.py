import csv

with open('profiles2.csv','w',newline='') as file:
    writer = csv.writer(file)
    row_list=[["name","age","country"],
             ["Ethan Justus","23","Kenya"],
             ["Cindy Marks","22","Somalia"],
             ["Mike Dean", "31","England"],]

    writer.writerows(row_list)


