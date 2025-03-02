class Car():
    __model = ""
    __year = 0

    def __init__(self,model,year=2025):
        self.__model = model
        self.__year = year

    def get_model(self):
        return self.__model
    
    def set_model(self,model):
        self.__model = model

    def start(self):
        print(f"{self.__model} arabası çalıştırılıyor...")

car1 = Car("Toyota",2020)
car1.start()
print(car1.get_model())
car1.set_model("Honda")
car1.start()