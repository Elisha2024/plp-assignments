class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self._storage = storage  # Encapsulated attribute

    def specs(self):
        print(f"{self.brand} {self.model} with {self._storage}GB storage.")

    def use(self):
        print(f"{self.model} is being used for calling and browsing.")

class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu_power):
        super().__init__(brand, model, storage)
        self.gpu_power = gpu_power

    def use(self):  # Polymorphism
        print(f"{self.model} is gaming with GPU level {self.gpu_power}!")
