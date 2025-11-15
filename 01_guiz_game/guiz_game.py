# This is a simple computer quiz game.
# The program asks the user four questions about basic computer components (CPU, GPU, RAM, PSU).
# The user inputs their answers, and the program checks if they are correct.
# It keeps track of the score and displays the total correct answers and the percentage at the end.
print("Welcome to my computer quiz!")

playing = input("Do you want to play (y/n)? ").lower()

if playing != "y":
    quit()


print("Lets play!")
score = 0

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What does PSU stand for? ")
if answer == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Your got :"+ str(score)+ "questions correct!")

print("Your got :"+ str((score/4)*100) + "%")

