print("Tip Calculator")
print("==============")
print()

myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = int(input("What % would you like to tip?: 15, 20, or 25 percent? "))

billWithTip = tip / 100 * myBill + myBill
billPerPerson = billWithTip / numberOfPeople
finalAmount = round(billPerPerson, 2)

print("You all owe", finalAmount)