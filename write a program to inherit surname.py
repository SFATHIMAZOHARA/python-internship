#write  a program to inherit surname
class GF:
    def __init__(self,surname):
        self.surname=surname
class father(GF):
    def __init__(self,name,surname):
        self.name=name
        super().__init__(surname)
my_father=father("father_name","syed")
print(my_father.surname)

