print("Math Game!")
print("==========")
print()

multiples = int(input("Name your multiples: "))
print()

score = 0
for i in range (1,11):
  correctAnswer = i * multiples
  print(i, "x", multiples)
  answer = int(input("> "))
  if answer == correctAnswer:
    print("You got it right!")
    score += 1
  else:
    print("The answer should of been", correctAnswer)

if score == 10:
  print("Wow! A perfect score!")
else:
  print("You got", score, "out of 10 correct.")