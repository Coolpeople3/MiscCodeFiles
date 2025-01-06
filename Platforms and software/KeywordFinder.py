keywords = []
score = 0

print("How many keywords would you like to input?")
numOfKeywords = int(input())
print("\nPlease input them below:")
for i in range(numOfKeywords):
    option3 = input("").lower()
    keywords.append(option3)

print("\nGreat!\nNow please input the student's answer")
option4 = str(input("-->  ")).lower()

for i in keywords:
    if i in option4:
        print(f"Keyword Detected: {i}")
        score += 1

print("\nFinal results:")
print(f"Your student had {score} keywords in the response.")
print(f"Your Student's percentage score was {round((score/numOfKeywords)*100, 2)}%")
