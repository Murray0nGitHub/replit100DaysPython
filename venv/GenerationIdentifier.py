print("Generation Identifier")
print("=====================")
print()
year = int(input("What year were you born in?"))
if year >= 1883 and year <= 1900:
  print("You are a soul of a 'Lost Generation'")
elif year >= 1901 and year <= 1927:
  print("You are apparently the 'Greatest Generation'")
elif year >= 1928 and year <= 1945:
  print("You are from the 'Silent Generation'")
elif year >= 1946 and year <= 1964:
  print("You are a 'Baby Boomer'")
elif year >= 1965 and year <= 1980:
  print("Ahh.. 'Generation X'")
elif year >= 1981 and year <= 1996:
  print("'Millenial'.. just like me!")
elif year >= 1997 and year <= 2012:
  print("You are 'Gen Z'")
else:
  print("You are either really old and are a time traveler or you are 'Generation Alpha'")