def parse_input(input):

    import re
    lista_1=re.split("\n",input)
    lista_2=list(filter(None,lista_1))
    lista_3=list(map(lambda x: x.split(),lista_2))
    lista_4=list(map(lambda x: list(map(lambda y: int(y),x)),lista_3))

    return lista_4

