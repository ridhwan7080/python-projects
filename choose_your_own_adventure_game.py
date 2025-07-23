name = input("Enter your name: ")
print("Welcome", name, "to this adventure!")

answer= input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? \n").lower()

if answer == "left":
    answer= input("You come to a river, you can walk around it or swim accross? Type walk to walk across and swim to swim across: ").lower()

    if answer == "swim":
        print("You swam and were eaten by a crocodile.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print("Not a valid option you lose!.") 

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly , do you want to cross it or head back(cross/back)?\n ").lower()
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and met a stranger. Did you talk to him(yes/no)? \n").lower()
        if answer == "yes":
            print("You talk to the stranger and he give you gold, You win!")
        elif answer == "no":
            print("You ignore the person and he is offended, you lose!!!")
        else:
            print("Not a valid option, You lose!")