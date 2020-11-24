def add(a,b):
    print("Adding {a} + {b}")
    return a+b

def subtract(a,b):
    print("Subtracting {a} - {b}")
    return a-b

def multiply(a,b):
    print("Multipying {a} * {b}")
    return a*b

def divide(a,b):
    print("Dividing {a} / {b}")
    return float(a/b)

print("maths time!!!!!!!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print("Age: {}, Height: {}, Weight: {}, IQ: {}".format(age, height, weight, iq))

print("puzzle for extra credits")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print("That becomes: ", what, "can you do it by hand?")