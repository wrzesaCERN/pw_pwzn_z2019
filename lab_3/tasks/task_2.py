def check_frequency(input):
    """

    Zrobiłam tak jak rozumiem treść zadania, a rozumeim tak:
    1 - nieoczywiste : to zliczenie to dodanie? inaczej nie stworzymy naszego zbioru 
    2 - oczywiste: to usunięcie ze zbioru jednej takiej liczby
    3 - oczywiste: ile razy jest coś w środku


    Perform counting based on input queries and return queries result.
    Na wejściu otrzymujemy parę liczb całkowitych - operacja, wartość.
    Możliwe operacje:
    1, x: zlicz x
    2, x: usuń jedno zliczenie x jeżeli występuje w zbiorze danych
    3, x: wypisz liczbę zliczeń x (0 jeżeli nei występuje)
    Do parsowania wejścia wykorzystaj funkcję parse_input.
    Po wejściu (już jakoliście) iterujemy tylko raz (jedna pętla).
    Zbiór danych zrealizuj za pomocą struktury z collections.

    """

    import modul
    lista_kwerend=modul.parse_input(input)
    lista_output_pol3=[]
    zbior_danych = []
    for elem in lista_kwerend:
        if elem[0] == 1:
            zbior_danych.append(elem[1])
        elif elem[0] == 2:
            if zbior_danych.count(elem[1]) > 0:
                zbior_danych.remove(elem[1])
        elif elem[0] == 3:
            lista_output_pol3.append(zbior_danych.count(elem[1]))
    return lista_output_pol3


_input = """
1 5
1 6
2 1
3 2
1 10
1 10
1 6
2 5
3 2
"""
if __name__ == '__main__':
    assert check_frequency(_input) == [0, 0] #było [0,1] ale
    # nawet jak się patrzy na argumety to nie dodaje sie nigdzie "2",
    # więc nie ma prawa nigdzie być 2 za drugim razem.
    
    
#chyba że jest całkowicie inna koncepcja zadania a ja nie umiem przetłumaczyć 
#polecenia "zlicz" tak by jednocześnie jakośc powstał zbiór
