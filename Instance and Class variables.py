class car:

    wheels=4

    def __init__(self):
        self.mil=4
        self.brand="BMW"


car1=car()
car2=car()

car1.mil=8
car.wheels=8

print(car1.brand,car1.mil,car1.wheels)
print(car2.brand,car2.mil,car2.wheels)
