#program to calculate league points
match_data=input()
match_data_list=match_data.split(',')
def cal_league_points(a):
    points=int(a[0])*4+int((a[1]))*2+int(a[2])*-1
    return points 
ans=cal_league_points(match_data_list)
print(ans)

