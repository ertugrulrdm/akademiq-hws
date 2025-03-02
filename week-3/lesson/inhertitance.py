class Vehicle():
    def __init__(self,model):
        self.model = model
    def start(self):
        print(f"{self.model} aracı başlatılıyor...")

class Car(Vehicle):
    def __init__(self, model):
        super().__init__(model)

    def start(self):
        print(f"{self.model} arabası başlatılıyor...")

class Truck(Vehicle):
    def __init__(self, model):
        super().__init__(model)
    
    def start(self):
        print(f"{self.model} kamyoneti başlatılıyor...")

car1 = Car("Honda")
truck1= Truck("Ford")

car1.start()
truck1.start()