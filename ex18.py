def print_two(*args):
    arg1, arg2 = args
    print("arg1: {}, arg2: {}".format(arg1, arg2))

def print_two_again(arg1, arg2):
    print("arg1: {}, arg2: {}".format(arg1, arg2))

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin'")

print_two("zed", "shaw")
print_two_again(1, 2)
print_one("first!")
print_none()
