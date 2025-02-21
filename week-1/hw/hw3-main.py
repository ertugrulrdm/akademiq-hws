class Human:
    name = "Ertugrul"
    def __init__(self,name):
        self.name = name
        print("A human instance has been created.")
    def __str__(self):
        return f"STR fonksiyonundan dönen değer: {self.name}"
    def talk(self, sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")

human1 = Human("Selim")
human1.talk("Merhaba")
human1.walk()
print(human1)

human2 = Human("Cem")
human2.talk("Selam")
human2.walk()
print(human2)

###