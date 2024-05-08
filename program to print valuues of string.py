#program to print valuues of string
str_1='acjbbabdcd'
d={'a':1}
for i in str_1:
    if(d.get(i)==None):
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)
for key,value in d.items():
    print(key+':'+str(value))