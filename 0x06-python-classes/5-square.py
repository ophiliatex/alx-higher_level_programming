#!/usr/bin/python3
"""Defines a square module."""

class Square:
 """Defines a sqaure."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Dimension of the square.

        """
        self.__size = size

    @property
    def size(self):
        """Property for the dimension of the sqaure.
        Raises:
            TpeError: If sizee is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Property for the dimension of the sqaure.
        Raises:
            TpeError: If sizee is not an integer.
            ValueError: If size is less than 0.
        """
	if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of the square.
        Returns:
            The size the squared.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square."""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
