print("Let's play a quiz game!!!")

playing_status = input("Are you ready to play? ")

if playing_status.lower() != "yes":
    quit()

print("Okay let's play :) ")
score = 0
answer = input("What does CPU stands for: ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!!!")

answer = input("What does GPU stands for: ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!!!")

answer = input("What does RAM stands for: ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!!!")

answer = input("What does PSU stands for: ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!!!")

print("You have obtained " + str(score) + " correct answers.")
print("You got " + str((score/4)*100) + "%.")