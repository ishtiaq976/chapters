import random

# 9-1
class Restaurant:
    def _init_(self, name, cuisine):
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

# 9-2
r1 = Restaurant("Taco Town", "Mexican")
r2 = Restaurant("Sushi Bar", "Japanese")
r3 = Restaurant("Pasta Place", "Italian")
r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()

# 9-3
class User:
    def _init_(self, first, last, age, city):
        self.first = first
        self.last = last
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"{self.first} {self.last}, {self.age}, {self.city}")

    def greet_user(self):
        print(f"Hello {self.first}!")

u1 = User("Alice", "Smith", 30, "NY")
u2 = User("Bob", "Jones", 25, "LA")
u3 = User("Eve", "Wong", 28, "SF")
u1.describe_user()
u1.greet_user()
u2.describe_user()
u2.greet_user()
u3.describe_user()
u3.greet_user()

# 9-4
r = Restaurant("Curry Corner", "Indian")
r.number_served = 0
print(r.number_served)
r.number_served = 10
print(r.number_served)

def set_number_served(obj, number):
    obj.number_served = number

def increment_number_served(obj, number):
    obj.number_served += number

set_number_served(r, 25)
print(r.number_served)
increment_number_served(r, 40)
print(r.number_served)

# 9-5
class User:
    def _init_(self, first, last):
        self.first = first
        self.last = last
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

u = User("Test", "User")
for _ in range(3):
    u.increment_login_attempts()
print(u.login_attempts)
u.reset_login_attempts()
print(u.login_attempts)

# 9-6
class IceCreamStand(Restaurant):
    def _init_(self, name, cuisine="Ice Cream"):
        super()._init_(name, cuisine)
        self.flavors = ["vanilla", "chocolate", "mint"]

    def show_flavors(self):
        print("Flavors:", ", ".join(self.flavors))

ics = IceCreamStand("Frosty Treats")
ics.show_flavors()

# 9-7
class Admin(User):
    def _init_(self, first, last):
        super()._init_(first, last)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Privileges:", self.privileges)

admin = Admin("Super", "Admin")
admin.show_privileges()

# 9-8
class Privileges:
    def _init_(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Privileges:", self.privileges)

class Admin(User):
    def _init_(self, first, last):
        super()._init_(first, last)
        self.privileges = Privileges()

admin = Admin("Admin", "One")
admin.privileges.show_privileges()

# 9-9
class Battery:
    def _init_(self, size=75):
        self.size = size

    def get_range(self):
        if self.size == 75:
            print("Range: 260 miles")
        else:
            print("Range: 315 miles")

    def upgrade_battery(self):
        if self.size < 100:
            self.size = 100

class ElectricCar:
    def _init_(self):
        self.battery = Battery()

car = ElectricCar()
car.battery.get_range()
car.battery.upgrade_battery()
car.battery.get_range()

# 9-10
class Die:
    def _init_(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))

for sides in [6, 10, 20]:
    die = Die(sides)
    for _ in range(10):
        die.roll_die()

# 9-11
items = [1,2,3,4,5,6,7,8,9,10,'A','B','C','D','E']
winning = random.sample(items, 4)
print("Winning combination:", winning)

# 9-12
my_ticket = [1, 'B', 7, 'D']
count = 0
while True:
    draw = random.sample(items, 4)
    count += 1
    if sorted(draw) == sorted(my_ticket):
        break
print(f"Won after {count} tries!")