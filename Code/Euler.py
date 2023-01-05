#Euler Magic Square
#Birthday Magic Square (https://youtu.be/hNn0j4Kay8g)
from tabulate import tabulate

a = int(input("First Number: "))
b = int(input("Second Number: "))
c = int(input("Third Number: "))
d = int(input("Fourth Number: "))

table = [[a, b, c, d],
        [c+1, d-1, a-1, b+1],
        [d+1, c+3, b-1, a-3],
        [b-2, a-2, d+2, c+2]]

print("\nYour Euler Magic Square")
print(tabulate(table, tablefmt='grid'))
print(f"Magic Number: {a+b+c+d}")