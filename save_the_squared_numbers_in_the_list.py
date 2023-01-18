# Print the square of the number from 1 to 10 and then store it in the list.

###########PREVIOUS CODE ################
# a = []                                #
# for i in range(1, 11):                #
#   a.append(i**2)                      #
# print(a)                              #
###########PREVIOUS CODE ################


a = []

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

for i in range(x, y+1):
  a.append(i**2)
print(a)
