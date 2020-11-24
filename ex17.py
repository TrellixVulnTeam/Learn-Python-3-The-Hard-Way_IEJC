from sys import argv
#from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# in_file = open(from_file)
# indata = in_file.read()

#print(f"The input file is {len(indata)} bytes long")

#print("Does the output file really exist? {}", exists(to_file))
#print("Ready? hit return to continue, CTRL-C to abort")
#input()

#out_file = open(to_file, 'w')
open(to_file, 'w').write(open(from_file).read())

print("All right, it's done")

# close(to_file)
# close(from_file)