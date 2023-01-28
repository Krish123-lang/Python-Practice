### To check the number is odd or even ###

def evodd(a):
  if a % 2 == 0:
    return "Even"
  else:
    return "Odd"


inp = int(input("Enter the number to be checked: "))
number = evodd(inp)
print(number)
