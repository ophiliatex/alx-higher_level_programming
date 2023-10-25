#!/usr/bin/python3
"""Defines a square class."""

class Square:
 """Defines a sqaure."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Dimension for the size of the square.

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
        """A setter for the dimension of the sqaure.
        Raises:
            TpeError: If sizee is not an integer.
            ValueError: Size must be greater than or equal to 0.
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
