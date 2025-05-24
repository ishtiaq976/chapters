class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine} food.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

r = Restaurant("Spice House", "Indian")
print(r.name)
print(r.cuisine)
r.describe_restaurant()
r.open_restaurant()
