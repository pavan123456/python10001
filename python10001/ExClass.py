#multiplication table

print("Enter the number for multiplication Table")

number = int(input("Enter the number \n"))

i = 1

while i < 10:
    print("%d X %d = %d"% (number, i, number * i))
    i = i+1