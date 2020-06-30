class Kettle(object):

    power_source = "electricity"
    # ^ class attribute



    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


# Create first instance
kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

# Modify the object
kenwood.price = 12.75
print(kenwood.price)
# Create second instance
hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {}, {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
"""
# Modify object by stating object first
print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

# Modify object by stating class first then object as an argument
Kettle.switch_on(kenwood)
print(kenwood.on)

print("*" * 80)
# Create new attribute to the object
kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power)
# ^ Produces error because the object has no attribute 'power'

print("Switch to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)

print("Switch kenwood to gas")
kenwood.power_source = "gas"
print(kenwood.power_source)

print(hamilton.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)