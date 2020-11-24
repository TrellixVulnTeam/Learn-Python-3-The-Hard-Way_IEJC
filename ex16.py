from sys import argv
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C")
print("If you do want that, hit RETURN")

input("?")

print("opening the file now")
target = open(filename, 'w')

print("Truncating the file. Bye-bye!")
target.truncate()

print("now I'm going to ask you for three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("now I'm going to write these to the file woohoo uwu")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("closing it now soz")
target.close()