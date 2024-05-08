#program to print a table
n=int(input())
i=1
def table(n,i):
    if(i<=10):
        print(n,'x',i,'=',9*i)
    else:
        return
    table(n,i+1)
table(n,i)
