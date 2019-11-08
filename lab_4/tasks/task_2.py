"""
Częśćć 1 (1 pkt): Uzupełnij klasę Vector tak by reprezentowała wielowymiarowy wektor.
Klasa posiada przeładowane operatory równości, dodawania, odejmowania,
mnożenia (przez liczbę i skalarnego), długości
oraz nieedytowalny (własność) wymiar.
Wszystkie operacje sprawdzają wymiar.
Część 2 (1 pkt): Klasa ma statyczną metodę wylicznia wektora z dwóch punktów
oraz metodę fabryki korzystającą z metody statycznej tworzącej nowy wektor
z dwóch punktów.
Wszystkie metody sprawdzają wymiar.
"""


class Vector:
    dim = None  # Wymiar vectora
    def __init__(self, *args):
        if len(args)==0: self.values =(0,0)
        else:
            self.values = args
            dim = len(args)

    def __add__(self,other):
        if isinstance(other,Vector):
            if self.dim == other.dim:
                added = tuple( a+b for a,b in zip(self.values, other.values))
                return Vector(*added)
            else:
                raise ValueError("Proszę odpocznij bo już dodajesz wektory o innych wymiarach...")
        else:
            raise ValueError("Proszę odpocznij bo już próbujesz dodawać nie takgo same typu rzeczy...")



    def __sub__(self,other):
        if isinstance(other,Vector):
            if self.dim == other.dim:
                subed = tuple( a-b for a,b in zip(self.values, other.values))
                return Vector(*subed)
            else:
                raise ValueError("Proszę odpocznij bo już odejmujesz wektory o innych wymiarach...")
        else:
            raise ValueError("Proszę odpocznij bo już próbujesz odejmoać nie takgo same typu rzeczy...")

    def __mul__(self,other):
        if isinstance(other,Vector):
            if self.dim == other.dim:
                muled = sum( a*b for a,b in zip(self.values, other.values))
                return muled
            else:
                raise ValueError("Proszę odpocznij bo już mnożysz wektory o innych wymiarach...")
        else:
            muled = tuple(a*other for a in self.values)
            return Vector(*muled)

    def __eq__(self, other):
        if isinstance(other,Vector):
            if self.dim == other.dim:
                return self.values == other.values
            else:
                raise ValueError("Proszę odpocznij bo już porównujesz wektory o innych wymiarach...")
        else:
            raise ValueError("Proszę odpocznij bo już próbujesz porównywać nie takgo same typu rzeczy...")

    def __len__(self):
        tmp= tuple(a**2 for a in self.values)
        length=sum(tmp)**0.5
        return int(length)


    @staticmethod
    def calculate_vector(beg, end):
        """
        Calculate vector from given points
        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: Calculated vector
        :rtype: tuple
        """
        v_beg=Vector(*beg)
        v_end=Vector(*end)

        if v_beg.dim == v_end.dim:
            v_new = v_end-v_beg
            wynik =tuple(v_new.values)
            return wynik
        else:
            raise ValueError("Proszę odpocznij bo już wektory z różnych wymiaraów...")

    @classmethod
    def from_points(cls, beg, end):
        """"""
        """
        Generate vector from given points.
        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: New vector
        :rtype: tuple
        """
        v_beg=Vector(*beg)
        v_end=Vector(*end)

        if v_beg.dim == v_end.dim:
            return v_end-v_beg
        else:
            raise ValueError("Proszę odpocznij bo już wektory z różnych wymiaraów...")


if __name__ == '__main__':
    v1 = Vector(1,2,3)
    v2 = Vector(1,2,3)
    assert v1 + v2 == Vector(2,4,6)
    assert v1 - v2 == Vector(0,0,0)
    assert v1 * 2 == Vector(2,4,6)
    assert v1 * v2 == 14
    assert len(Vector(3,4)) == 5.0
    assert Vector.calculate_vector([0, 0, 0], [1,2,3]) == (1,2,3)
    assert Vector.from_points([0, 0, 0], [1,2,3]) == Vector(1,2,3)
