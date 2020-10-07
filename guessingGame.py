import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The String that the user will see, when
    they're prompted to enter the value.

    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)  # Converting strings to integers with int
        print("{0} is not a valid number".format(temp))
        # else:
        #     print("{0} is not a valid number".format(temp))


highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing
guess = 0  # initialise to any number that doesnt equal the answer

print("Please guess a number between 1 and {}: ".format(highest))
while guess != answer:
    guess = get_integer(": ") # shows up when np number is entered

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it!")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")




# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Please try again")
#         guess = int(input())
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Please try again")
#         guess = int(input())
# else:
#     print("You got it the first time!")

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Please try again")
#         guess = int(input())
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Please try again")
#         guess = int(input())
# else:
#     print("You got it the first time!")