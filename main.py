from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("i can walk and run")
class snake(animal):
    def move(self):
        print("i can crawl")
class dog(animal):
    def move(self):
        print("i can run and walk")
class lion(animal):
    def move(self):
        print("i can roar")
a = human()
a.move()
b = snake()
b.move()
c = snake()
c.move()
d = dog()
d.move()
e = lion()
e.move()