#Euler Magic Square
from tabulate import tabulate

x = int(input("How many: "))
data =[0 for i in range(x)]
data2 =[0 for i in range(x)]

for i in range(x):
    data[i] = int(input(f"{i+1} number: "))

#Alfa, Beta, Theta ect
custom = input("Custom number? (Y/N) ")
if custom =='Y':
    print("For Custom alfa, beta, ect")
    for i in range(x):
        data2[i] = int(input(f"{i+1} number: "))
else:   #If NO then automaticly create number from 0 to X
    for i in range(x):
        data2[i] = i+1
        i+=1

euler = []
a = 0
for i in range(x):
    euler.append([])
    for j in range(x):
        aa = j+a
        if aa >= x:
            aa = aa - x

        ab = j-a
        if ab < 0:
            ab = ab + x

        #euler[i].append([aa, ab])
        euler[i].append(data[aa]+data2[ab])
    a+=1

spn = 0 #SUM of the number (Not diagonal)
for i in range (x):
    spn += euler[0][i]

print("\n================== Euler ==================")
print(f"Special Number: {spn}")
print(tabulate(euler, tablefmt='grid'))
