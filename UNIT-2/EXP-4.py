class Transport:
    def action(self):
        print("The vehicle is moving")


class CarType(Transport):
    def action(self):
        print("Driving on the road")


class Cycle(Transport):
    def action(self):
        print("Pedaling on the road")


def show_movement(obj):
    obj.action()


c1 = CarType()
c2 = Cycle()

print("Car Movement:")
show_movement(c1)

print("\nBicycle Movement:")
show_movement(c2)