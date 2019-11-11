"""
Na (1 pkt.):
- Zaimplementuj klasy: Rectangle, Square, Circle dziedziczące z klasy Figure
oraz definiujące jej metody:
    - Rectangle powinien mieć dwa atrybuty odpowiadające bokom (a i b)
    - Klasa Square powinna dziedziczyć z Rectangle.
    - Circle ma posiadać tylko atrybut r (radius).
- Przekształć metody we własności (properties).
---------
Na (2 pkt.):
- Zwiąż ze sobą boki a i b klasy Square (tzn. modyfikacja boku a lub boku b
powinna ustawiać tę samą wartość dla drugiego atrybutu).
- Zaimplementuj metody statyczne pozwalające na obliczenie pola
figury na podstawie podanych parametrów.
- Zaimplementuj classmethod "name" zwracającą nazwę klasy.
---------
Na (3 pkt.):
- Zaimplementuj klasę Diamond (romb) dziedziczącą z Figure,
po której będzie dziedziczyć Square,
tzn. Square dziediczy i z Diamond i Rectangle.
- Klasa wprowadza atrybuty przekątnych (e i f) oraz metody:
-- are_diagonals_equal: sprawdź równość przekątnych,
-- to_square: po sprawdzeniu równości przekątnych zwróci instancję
klasy Square o takich przekątnych.
- Zwiąż ze sobą atrybuty e i f (w klasie Diamond) oraz a, b, e i f
(w klasie Square)
"""

import math
from abc import ABC


class Figure:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    @classmethod
    def name(cls): return cls.__name__

    def __str__(self):
        return (
            f'{self.name()}: area={self.area:.3f}, '
            f'perimeter={self.perimeter:.3f}'
        )


class Circle(Figure):

    def __init__(self, r): self.r = r

    @property
    def r(self): return self.__r

    @r.setter
    def r(self, r): self.__r = r

    @staticmethod
    def get_area(r): return math.pi * r * r

    @property
    def area(self): return self.get_area(self.r)

    @staticmethod
    def get_perimeter(r): return math.pi * r * 2

    @property
    def perimeter(self): return self.get_perimeter(self.r)


class Rectangle(Figure):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def a(self): return self.__a

    @property
    def b(self): return self.__b

    @a.setter
    def a(self, a): self.__a = a

    @b.setter
    def b(self, b): self.__b = b

    @staticmethod
    def get_area(a, b): return a * b

    @property
    def area(self): return self.get_area(self.a, self.b)

    @staticmethod
    def get_perimeter(a, b): return 2 * a + 2 * b

    @property
    def perimeter(self): return self.get_perimeter(self.a, self.b)


class Diamond(Figure):

    def __init__(self, e, f):
        self.e = e
        self.f = f

    @property
    def e(self): return self.__e

    @property
    def f(self): return self.__f

    @e.setter
    def e(self, e): self.__e = e

    @f.setter
    def f(self, f): self.__f = f

    @staticmethod
    def _area(e, f): return 0.5 * e * f

    @property
    def area(self): return self._area(self.e, self.f)

    def are_diagonals_equal(self): return self.f == self.e

    def bok(self): return math.sqrt((self.e / 2) ** 2 + (self.f / 2) ** 2)

    @property
    def perimeter(self): return 4 * self.bok()

    def to_square(self):
        if self.are_diagonals_equal(): return Square(self.bok())
        else: raise RuntimeError("Przekątne nie są takiej samej długości")


class Square(Rectangle, Diamond):

    def __init__(self, a): super().__init__(a, a)

    def set_a(self, x):
        self.__a = x
        self.__b = x
        self.__e = math.sqrt(2 * x * x)
        self.__f = math.sqrt(2 * x * x)

    def get_a(self): return self.__a

    a = property(get_a, set_a)

    def set_b(self, y):
        self.__a = y
        self.__b = y
        self.__e = math.sqrt(2 * y * y)
        self.__f = math.sqrt(2 * y * y)

    def get_b(self): return self.__b

    b = property(get_b, set_b)

    def set_e(self, e):
        self.__a = math.sqrt(e * e / 2)
        self.__b = math.sqrt(e * e / 2)
        self.__e = e
        self.__f = e

    def get_e(self): return self.__e

    e = property(get_e, set_e)

    def set_f(self, f):
        self.__a = math.sqrt(f * f / 2)
        self.__b = math.sqrt(f * f / 2)
        self.__e = f
        self.__f = f

    def get_f(self): return self.__f

    f = property(get_f, set_f)


if __name__ == '__main__':
    kolo1 = Circle(1)
    assert str(kolo1) == 'Circle: area=3.142, perimeter=6.283'

    rec_1 = Rectangle(2, 4)
    assert str(rec_1) == 'Rectangle: area=8.000, perimeter=12.000'

    # print("Square")
    sqr_1 = Square(4)
    assert str(sqr_1) == 'Square: area=16.000, perimeter=16.000'

    diam_1 = Diamond(6, 8)
    assert str(diam_1) == 'Diamond: area=24.000, perimeter=20.000'

    diam_2 = Diamond(1, 1)
    assert str(diam_2) == 'Diamond: area=0.500, perimeter=2.828'

    sqr_3 = diam_2.to_square()
    assert str(sqr_3) == 'Square: area=0.500, perimeter=2.828'
