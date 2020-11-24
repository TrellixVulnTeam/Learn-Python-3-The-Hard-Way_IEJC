from sys import argv

script, username = argv
prompt = '>'

print(f"Hi user {username}, I'm the {script} script.")
print("I'd like to ask you a few questions")
print("do you like me, {}".format(username))
likes = input(prompt)

print("Where do you {}, {}?".format('live', username))
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print("""all right so you have said you {} like me,
you live in {}. No clue where that is lol.
And u have a {} computer. Where I live. hmmm
""".format(likes, lives, computer)
)