num = int(input("Enter a number \n"))
sqr = num*num #square of num
sumOfDigit = 0

while sqr>0:
    sumOfDigit =sumOfDigit + sqr%10
    sqr = sqr//10

if (num == sumOfDigit):
    print("Neon Number \n")
else:
    print("Not a Neon Number \n")
