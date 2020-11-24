def cheese_and_crackers(cheese_count, box_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {box_of_crackers} boxes of crackers")
    print("partyyyyyyyyyyy!")

def funky_funk(a,b):
    b = a*2
    b += a
    print(b)

print("we can give the function numbers directly")
cheese_and_crackers(20,30)

print("or we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("we can do math inside the function: ")
cheese_and_crackers(10+20, 5+6)

print("we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)


print("here goes some practice: ")
funky_funk(10,20)
