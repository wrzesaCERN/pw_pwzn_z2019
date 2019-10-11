def unique(values):
    """
    Funkcja zwraca listę unikatowych wartości.
    Utrudnienie: Funkcja zwraca unikatowe wartości w kolejności wystąpienia.

    :param values: List of values to check.
    :type values: list
    :return: Unique values in order of appear.
    :rtype: list
    """
    wynik = []
    for elem in values:
        print(elem)

        iter = 0
        if iter > 0:
            for ii in range(iter):
                if elem ==  unique[iter]:
                    continue
        wynik.append(elem)
        print(elem)

        iter+=1
        return wynik


if __name__ == "__main__":
    assert [1, 5, 3, 6, 7, 2, 4] == unique([1, 5, 3, 5, 6, 7, 2, 1, 4, 1, 5])
