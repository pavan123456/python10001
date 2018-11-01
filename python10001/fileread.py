import sys

def new_file(filename):
    return readingfile(filename)

def readingfile(filename):
    results = dict()
    with open(filename, 'r') as file:
        for line in file:
            for word in line.split():
                print(word)
                
x = new_file(r"C:\Users\pavankuk\source\repos\python10001\python10001\lambda.py")
print(x)


