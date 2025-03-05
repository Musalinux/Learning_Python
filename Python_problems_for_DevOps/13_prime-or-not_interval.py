def primeOrNot(FirstInterval, SeconInterval):
    for i in range (FirstInterval, SecondInterval +1):
        for j in range (2, i):
            if ((i % j) == 0):
                print (i,"is not a prime number")
                break 
        else:
            print (i, "is a prime number")

FirstInterval = int(input ("Enter the first interval: \n"))
SecondInterval = int(input ("Enter the second interval: \n"))

if (FirstInterval > 1 and SecondInterval >1) and FirstInterval < SecondInterval:
    primeOrNot(FirstInterval,SecondInterval)
else:
    print ("Enter a valid range!")
