#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    def __init__(self, radius):
        self.radius = radius
        # self.diameter = radius * 2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2

    @property
    def area(self):
        return self._radius ** 2 * math.pi

    @area.setter
    def area(self, value):
        raise AttributeError
        self._radius = math.sqrt(value / math.pi)

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)
