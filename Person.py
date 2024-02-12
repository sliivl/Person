class Person:
    def __init__(self, age, name, gender):
        self.age = age
        self.name = name
        self.gender = gender
        print(f"Создан аватар: {self.name}, {self.age}, {self.gender}")

    def learn(self):
        print(f"{self.name} пишет лекции...")

    def chill(self):
        print(f"{self.name} отдыхает...")

    def work(self):
        print(f"{self.name} работает...")

Person1 = Person(18, "Кирилл", "Мужчина")
Person1.learn()
Person1.chill()
Person1.work()