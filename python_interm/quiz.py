#!/usr/bin/python3

from time import sleep

print("Welcome to my computer quiz!")

playing = input('Do you want to play? ')

checking_readiness = input('You have 5 question to answer, are you ready for this? ')
if checking_readiness.lower() != 'yes':
    quit()
else:
    if playing.lower() != 'yes':
        quit()
    else:
        print("Okay let's play :)")
    
    sleep(3)
    
    score = 0
    
    question1 = input("Q1: What does cpu stand for? ")
    if question1.capitalize() == "Central Processing Unit".capitalize():
        print('correct!')
        score += 1
    else:
        print('incorrect!')
        print('The correct answer is Central Processing Unit :)')
    
    question2 = input("Q2: What does PSU stand for? ")
    if question2.capitalize() == "Power Supply".capitalize():
        print('correct!')
        score += 1
    else:
        print('incorrect!')
        print('The correct answer is Power Supply :)')
    
    question3 = input("Q3: What does ROM stand for? ")
    if question3.capitalize() == "Read Only Memory".capitalize():
        print('correct!')
        score += 1
    else:
        print('incorrect!')
        print('The correct answer is Read Only Memory :)')
    
    question4 = input("Q4: What does RAM stand for? ")
    if question4.capitalize() == "Random Access Memory".capitalize():
        print('correct!')
        score += 1
    else:
        print('incorrect!')
        print("The correct answer is Random Access Memory :)")
    
    question5 = input("Q5: What does GPU stand for? ")
    if question5.capitalize() == "Graphics Processing Unit".capitalize():
        print('correct!')
        score += 1
    else:
        print('incorrect!')
        print('The correct answer is Graphics Processing Unit :)')
        
    sleep(4)
     
    print("Congratulations for completing the quiz!") 
    sleep(2)  
    print("You got " + str(score) + " questions correct!")
    print("You scored " + str((score / 5) * 100) + "%.")
    sleep(1)
    if score >= 4:
        print("You are a genius")
    elif 3 < score < 4:
        print("You did great")
    elif 2 < score < 3:
        print('Satisfactory')
    else:
        print('Try again')
