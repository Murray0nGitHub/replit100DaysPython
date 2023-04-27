print("Seconds in a Year")
print("=================")
print()
daysThisYear = int(input("How many days are in this year?: "))
year = 365
leapYear = 366
hoursInDay = 24
minutesInHour = 60
secondsInMinute = 60

result = daysThisYear * hoursInDay * minutesInHour * secondsInMinute

leapYearResult = leapYear * hoursInDay * minutesInHour * secondsInMinute

if daysThisYear == 366:
  print("Number of seconds in a leap year are", leapYearResult)
else:
  print("Number of seconds in a year are", result)