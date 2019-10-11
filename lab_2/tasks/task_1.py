def counting_sort(values, _max, _min=0):
    wynik=[]
    for iter in range(_min, _max):
        for elem in values:
            index = 0
            if elem == iter:
                index+=1;
            for gupie in range(index):
                wynik.append(iter)
    return wynik

if __name__ == '__main__':
    assert counting_sort(
        [99, 4, 33, 2, 2, 1, 65, 3, 97, 53],
        100,
    ) == [1, 2, 2, 3, 4, 33, 53, 65, 97, 99]
