print("Exam Grade Calculator")
print("=====================")
print()
print()

nameOfExam = input("What is the name of your exam?: ")
maxScore = int(input("What was the max score for this exam?: "))
yourScore = int(input("What was your score?: "))

numberScore = float(yourScore / maxScore)
finalNumber = round(numberScore,2)
finalPerc = round(float(yourScore / maxScore) * 100,2)

print("You got", finalPerc,"%")

if finalNumber >= .90:
  print("You got an A+ on your ", nameOfExam, "exam.")
elif finalNumber >= .80 and finalNumber <= .89:
  print("You got an A on your", nameOfExam, "exam.")
elif finalNumber >= .70 and finalNumber <= .79:
  print("You got a B on your", nameOfExam, "exam.")
elif finalNumber >= .60 and finalNumber <= .69:
  print("You got a C on your", nameOfExam, "exam.")
elif finalNumber >= .50 and finalNumber <= .59:
  print("You got a D on your", nameOfExam, "exam.")
elif finalNumber <= .49:
  print("You got a U on your", nameOfExam, "exam.")
else:
  print("Try again!")