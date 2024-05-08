#write a program to find highest value from the dictionary
n=5
d={}
for i in range(5):
    player_name=input("enter player name:")
    runs=int(input("enter the runs:"))
    d[player_name]=runs
print(d)
runs=d.values()
for value in d.values():
    highest=value
    break
for value in d.values():
    if(value>highest):
        highest=value
print(highest)     

