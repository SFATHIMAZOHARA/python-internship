n=int(input())
def fun_name(n):
    if(n>1):
        return '1/' + str(n) + "+" + fun_name(n-1)
    elif(n==1):
        return '1' + fun_name(n-1)
    return' '
ans=fun_name(n)
print(ans)
