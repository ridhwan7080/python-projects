import random
# To set what should be the max number 
top_of_range = (input("Enter a number for the range: "))
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Enter a number greater than 0 next time.")
        quit()
else:
    print("Please type a number next time!!!")
    quit()

random_number = random.randint(0,top_of_range) 
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time!!!")
        continue
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number. ")
    else:
        print("you were below the number.")
print("You got it in",guesses,"guesses")




