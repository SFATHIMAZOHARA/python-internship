#program using function 
n=int(input())
def fun_name(n):
    if(n>0):
        return fun_name(n-1) + 1/n
    return 0
ans=fun_name(n)
print(ans)
