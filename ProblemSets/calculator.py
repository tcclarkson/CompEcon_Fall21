import math

data = [4, 2, 6]
def display():
    print("Sum of 2 and 6:", data[1] + data[2])
    print("Square Root of 4:", int(math.sqrt(data[0])))

display()

def sum_arg(x, y):
    return x + y

print(sum_arg(3, 4))

def product_arg(a, b):
    return a * b 

def hypotenuse(x, y):
    return math.sqrt(x**2 + y**2)