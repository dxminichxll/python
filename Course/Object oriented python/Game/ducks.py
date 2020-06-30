class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work but im flying")
        else:
            print("I think i'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)
    #     When a class contains another object like this ^^,
    #     this is called composition

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Drowning")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("It is cold here")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin")

    def aviate(self):
        print("I won the lottery and bought a learjet")


class Mallard(Duck):
    pass


class Flock(object):

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        # ^^ This method takes duck as an argument. :Duck documents that the argument type should be a duck object.
        # It also documents that the method returns nothing
        # if type(duck) is Duck:
        #     # Checks that type of argument is Duck
        #     # This is bad because it only checks for the duck object, not any subclasses of duck
        #     # So the mallard is a duck but that will not be recognised in the if statement
        #     self.flock.append(duck)

        # if isinstance(duck, Duck):
        #     # When doing this type of checking, always use the isinstance function
        #     self.flock.append(duck)

        fly_method = getattr(duck, 'fly', 'none')
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError("Cannot add duck, are you sure it's not a " + str(type(duck).__name__))
        # This method checks to see if the object has an attribute of fly
        # This attribute is then tested to see if it is callable to see if it is a method
        # (int or string type attributes are not callable)

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                raise AttributeError("Testing exception handler in migrate") # TODO remove this from release
            except AttributeError as e:
                # A reference to the exception is stored in a variable
                problem = e
                print("One duck down")

        if problem:
            raise problem


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
