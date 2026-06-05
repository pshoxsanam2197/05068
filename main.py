class Laptop:
    def __init__(self, brend):
        self.__brend = brend

    def get_brend(self):
        return self.__brend

    def set_brend(self, brend):
        self.__brend = brend

l = Laptop("HP")
print(l.get_brend())

l.set_brend("Lenovo")
print(l.get_brend())
