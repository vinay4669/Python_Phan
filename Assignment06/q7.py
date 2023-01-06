import csv

f = open('sample5.csv', 'r', newline='')
ob = csv.reader(f)
u = input("Enter userID : ")
for i in ob:
    if i[0]==u:
        print("Password :", i[1])