types_of_people = 10
x = f"There are {types_of_people} types of people." 

binary = "binary"
do_not = "don't"

y = f"those who know {binary} and those who {do_not}." #found1

print(x)
print(y)

print(f"I said: {x}")  #found2
print(f"I also said: '{y}'") #found3

hilarious = False
joke_evaluation = "Isn't my joke so funny?! {}"

print(joke_evaluation.format(hilarious)) #found4 #basically .format() is used to put value of hilarious where {} existed in the original sentence 

w = "This is the left side of ..."
e = "a string with a right side"
print(w + e)