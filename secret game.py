n=25
condition=True
while(condition):
    n=int(input())
    if(n==25):
        print("congragulations you  guessed it right")
    elif(n>25):
        print("number is too large")
    elif(n<25):
        print("numberis too samll")
    elif(n == 0 or n <= 0):
        print("user wants to quit")