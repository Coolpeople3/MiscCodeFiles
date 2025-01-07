import random

words=["apple","banana","carrot","computer","haha"]
userWords=[]

score=0

while True:
    randomWord=random.choice(words)
    print(f"The computer has chosen the word, {randomWord}")
    userInput=input("What is your word? --> ")
    if userInput[1]==randomWord[-1]:
        score+=1
        print("Good, keep going!\n")
