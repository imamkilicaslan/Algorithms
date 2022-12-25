number=int(input("input a number \n: "))
if number<0:
    print("cannot be a negative prime number")
if number==0 or number==1:
    print("Smallest prime number is 2")
else:
    for i in range(number-1, 0,-1):
        if number%i==0 and i>1:
            print(number, " is not a prime number")
            break
        else:
            if i==1:
                print(number, " is a prime number")
    