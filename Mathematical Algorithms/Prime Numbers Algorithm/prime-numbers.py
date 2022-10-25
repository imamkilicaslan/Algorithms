number = int(input("input a number: \n"))
print("---------")
# if number < 0:
# print("cannot be a negative prime number")
for i in range(2, (number+1)):
    if i >= 0:
        # print("is not a prime number")
        # else:
        # if (number-1) % i == 0:
        #     print(number, " is not a prime number")
        # else:
        #     print(number, " is a prime number")
        print(i)
