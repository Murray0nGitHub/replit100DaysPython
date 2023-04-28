print("One-Million-To-One")
print("##################")
print()

myNumber = 200000
attempt = 1

while True:
  guessNumber = int(input("What is your guess?: "))
  if guessNumber < 0:
    print("Now we'll never know what the answer is ...")
    exit()
  if guessNumber < myNumber:
    print("Too Low .. try again!")
    attempt += 1
  elif guessNumber > myNumber:
    print("Too High .. try agian!")
    attempt += 1
    continue
  elif guessNumber == myNumber:
    print("Winner! Congratulations!")
    break
  else:
    print("That is not a number I recognize.. sorry.")
print("It took you", attempt, "attempt(s) to get the correct answer.")