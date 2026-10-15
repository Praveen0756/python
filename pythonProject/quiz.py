# Quiz game

questions = ("What is the capital of India?",
             "Which language is used to style web pages?",
             "What is 5 + 5?",
             "What does CPU stand for?",
             "Which planet is known as the Red Planet?")

options = (("A. New Delhi", "B. Mumbai", "C. Chennai", "D. Kolkata"),
           ("A. HTML", "B. CSS", "C. Python", "D. Java"),
           ("A. 8", "B. 10", "C. 12", "D. 15"),
           ("A. Central Processing Unit", "B. Computer Personal Unit", "C. Central Program Utility", "D. Control Processing Unit"),
           ("A. Earth", "B. Venus", "C. Mars", "D. Jupiter"))

answers = ("A", "B", "B", "A", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
  print("-------------------------")
  print(question)
  for option in options[question_num]:
    print(option)

  guess = input("Enter (A, B, C, D): ").upper()
  guesses.append(guess)
  if guess == answers[question_num]:
    score += 1
    print("CORRECT")
  else:
    print("INCORRECT")
    print(f"{answers[question_num]} is the correct ans")
  question_num += 1


print("------------------------")
print("          RESULTS       ")
print("------------------------")

print("answers: ", end="")
for answer in answers:
  print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
  print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}")