def parse_input(input):
    """
    Splits multiline string into list of lists with integers.
    Jeżeli o to chodzi to działa...
    """


    import re
    lista_wierszy=re.split("\n",input) #podział na wiersze
    lista_wierszy_filtrowana=list(filter(None,lista_wierszy)) #usunięcie pustych
    lista_cyfry=list(map(lambda x: x.split(),lista_wierszy_filtrowana)) #wyciągniećie cyfr z wierszy
    print(lista_cyfry)
    lista_cyfryint=list(map(lambda x: list(map(lambda y: int(y),x)),lista_cyfry)) # zamaiana na int 
    return lista_cyfryint

_input = """
1 5
1 6
3 2
1 10
1 10
1 6
2 5
3 2
"""
assert parse_input(_input) == [[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]
