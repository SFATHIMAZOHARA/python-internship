l1=[]
l2=[]
for i in range(5):
    num=int(input())
    l1=l1+[num]
for i in range(5):
    num=int(input())
    l2=l2+[num]
common_count=0
for i in l1:
    for each_num in l2:
        if(i==each_num):
            common_count=common_count+1
print(common_count)
        
