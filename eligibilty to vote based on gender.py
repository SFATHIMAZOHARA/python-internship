age=int(input())
gender=input()
if(age<18):
    print("you are not  eligible to vote")
elif(age>=18 and gender=='male'):
    print("you are eligible to vote")
    print("go to right side")
else:
    print("you are eligible")
    print("go to left side")
