# Создайте класс Person, который имеет атрибуты name, age и метод introduce(), выводящий информацию о человеке. Создайте несколько объектов этого класса и вызовите метод introduce() для каждого из них.


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Имя: {self.name} \n Возраст: {self.age}")

person1 = Person("anton", 20)
person2 = Person("Jeck", 30)

person1.introduce()

person2.introduce()

