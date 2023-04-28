total = 1000
apr = 0.05
for i in range (10):
  total += (total*apr)
  print("Year", i+1, "is", round(total,2))