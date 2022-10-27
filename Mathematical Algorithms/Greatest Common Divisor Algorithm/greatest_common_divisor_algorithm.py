number1 = int(input("input a number for gcd calculation: "))
number2 = int(input("input a more one number for gcd calculation: "))

bigest_number = number1 if number1 > number2 else number2

for i in range(bigest_number, 0, -1):
    if number1 % i == 0 and number2 % i == 0:
        print(i)
        break
