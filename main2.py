from abc import ABC, abstractmethod
class absclass(ABC):
    def print(self, x):
        print("passed value:", x)
    @abstractmethod
    def task(self):
        print("we are in absclass")
class test_class(absclass):
    def task(self):
        print("we are in test_class task")
test_ob = test_class()
test_ob.task()
