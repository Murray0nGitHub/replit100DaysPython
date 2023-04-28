print("Welcome to my number list generator!")
print("####################################")
print()
print("You are goin going to give me a starting number, an ending number, and a number that tells me how to increment the list.")
print()

start = int(input("List a starting number: "))
end = int(input("List a number to end with: "))
increment = int(input("List a number to increment the list by: "))

for i in range(start, end, increment):
  print(i)