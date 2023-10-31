#!/usr/bin/python3
""" class Rectangle """


class Rectangle():

    number_of_instances = 0

    """" Represent a rectangle """
    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ("")

        star = []
        for i in range(self.__height):
            for j in range(self.__width):
                star.append('#')
            if i != self.__height - 1:
                star.append("\n")
        return "".join(star)

    def __repr__(self):
        star = "Rectangle(" + str(self.__width)
        star += ", " + str(self.__height) + ")"
        return star

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
