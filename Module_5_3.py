class House:
    def __init__(self, Name, Num_of_floors):
        self.name = Name
        self.num_of_floors = Num_of_floors

    def go_to(self, Floor):
        if Floor < 1 or Floor > self.num_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1,Floor+1):
                print(i)

    def __len__(self):
        return self.num_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.num_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.num_of_floors == other.num_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.num_of_floors < other.num_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.num_of_floors <= other.num_of_floors

    def  __gt__(self, other):
        if isinstance(other, House):
            return self.num_of_floors > other.num_of_floors

    def  __ge__(self, other):
        if isinstance(other, House):
            return self.num_of_floors >= other.num_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.num_of_floors != other.num_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.num_of_floors += value
            return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.num_of_floors += value
            return self

    def __radd__(self, value):
        if isinstance(value, int):
            self.num_of_floors += value
            return self

new_house = House('ЖК Эльбрус', 30)
new_house1 = House('ЖК Горский', 18)
new_house2 = House('Домик в деревне', 2)
new_house1.go_to(5)
new_house2.go_to(10)

# __str__
print(new_house1)
print(new_house2)

# __len__
print(len(new_house1))
print(len(new_house2))

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__