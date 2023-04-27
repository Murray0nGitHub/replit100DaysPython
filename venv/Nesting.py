print("👀 Fake Fan Finder 👀")
print(" -------------------- ")
print()
console = input("What is your favorite console?: Xbox, Playstation, or Switch? ")
if console == "Xbox":
  print("Oh really?")
  manufacturer = input("Who makes Xbox?")
  if manufacturer == "Microsoft":
    print("Okay, that was too easy!")
    cost = input("How much is the most expensive Xbox?")
    if cost == "500":
      print("You are a true fan!")
elif console == "Playstation":
  print("Oh really?")
  manufacturer = input("Who makes Playstation?")
  if manufacturer == "Sony":
    print("Okay, that was too easy!")
    cost = input("How much is the most expensive Playstation?")
    if cost == "500":
      print("You are a true fan!")
elif console == "Switch":
  print("Oh really?")
  manufacturer = input("Who makes the Switch?")
  if manufacturer == "Nintendo":
    print("Okay, that was too easy!")
    cost = input("How much is a Switch OLED?")
    if cost == "350":
        print("You are a true fan!")
else:
  print("I guess you don't like Video Games...")