class Animal:
    name = None
    alive = True
    fed = False

    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')


class Plant:
    name = None
    edible = False


class Mammal(Animal):
    def __init__(self, name):
        self.name = name


class Predator(Animal):
    def __init__(self, name):
        self.name = name


class Flower(Plant):
    def __init__(self, name):
        self.name = name


class Fruit(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = True


predator = Predator('Волк с Уолл-Стрит')
mammal = Mammal('Хатико')
flower = Flower('Цветик семицветик')
fruit = Fruit('Заводной апельсин')

print(predator.name)
print(flower.name)

print(predator.alive)
print(mammal.fed)
predator.eat(flower)
mammal.eat(fruit)
print(predator.alive)
print(mammal.fed)
