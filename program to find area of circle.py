32.#program to find area of circle
def cal_area(radius,pi=3.14):
    area=pi*radius*radius
    return area
r=int(input())
print(cal_area(r))
