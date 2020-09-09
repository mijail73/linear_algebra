class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError("The coordinates must be nonempty")
        except TypeError:
            raise TypeError("The coordinates must be an iterable")

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, value):
        return self.coordinates == value.coordinates

    def sameDimension(self, vector):
        if(self.dimension == vector.dimension):
            return True
        else:
            return False

    def addition(self, vector):
        try:
            if not self.sameDimension(vector):
                raise ValueError
            addition = Vector(
                tuple(map(sum, zip(self.coordinates, vector.coordinates))))
            return addition
        except ValueError:
            raise ValueError("The vectors should have the same dimension.")

    def subtraction(self, vector):
        try:
            if not self.sameDimension(vector):
                raise ValueError
            subtraction = Vector(
                tuple(a-b for a, b in zip(self.coordinates, vector.coordinates)))
            return subtraction
        except ValueError:
            raise ValueError("The vectors should have the same dimension.")

    def scalarMultiply(self, scalar):
        scalarM = tuple(scalar * a for a in self.coordinates)
        return scalarM


my_vector = Vector([8.218, -9.341])
my_vector2 = Vector([-1.129, 2.111])
my_vector3 = Vector([7.119, 8.215])
my_vector4 = Vector([-8.223, 0.878])
my_vector5 = Vector([1.671, -1.012, -0.318])
scalar = 7.41
print('Sum')
print(my_vector.addition(my_vector2))
print('Rest')
print(my_vector3.subtraction(my_vector4))
print('escalarMultiply')
print(my_vector5.scalarMultiply(scalar))
