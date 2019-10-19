"""
Zadanie za 2 pkt.

strasznie dużo czasu spędziłam na próbę rozgryzienia czego wymaga zadanie
pierwsza część działa druga daje output jak w odpowiedzi ale nie działa ..

"""
import datetime

def sort_dates(date_str, date_format=''):
    """
    DZIAŁA!!! :D
    """

    # obróbka wejścia...
    import re
    lista_wersy=re.split("\n",date_str)
    lista_wersy_na_wydarzenia=list(map(lambda x: x.split(),lista_wersy))
    lista_wydarzen=list(filter(None,lista_wersy_na_wydarzenia)) # usunięcie pustych elementów tablicy ...
    dir_miesiace = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5,'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12} # do konwersji (uzywane w następnym  kroku)

    lista_wyjscie=[] # to będzie mój return...

    #lecimy po wydarzeniach i obrabiamy każde...
    iter_wyd=0
    for elem in lista_wydarzen:

        lista_czasu = lista_wydarzen[iter_wyd][4].split(":")

        #przejście na UTC ... na początku liczę ile musze odjąć/dodać potem tworze deltę czasową i zmienam czas
        dodaj_delte = False
        if int(lista_wydarzen[iter_wyd][5]) < 0:
            dodaj_delte = True
        delta_h = int(lista_wydarzen[iter_wyd][5][1] + lista_wydarzen[iter_wyd][5][2])
        delta_m = int(lista_wydarzen[iter_wyd][5][3] + lista_wydarzen[iter_wyd][5][4])
        from datetime import timedelta
        delta = timedelta(hours=delta_h, minutes=delta_m)

        from datetime import datetime
        datestr = f'{lista_wydarzen[iter_wyd][3]}-{dir_miesiace[lista_wydarzen[iter_wyd][2]]}-{lista_wydarzen[iter_wyd][1]} {lista_czasu[0]}:{lista_czasu[1]}:{lista_czasu[2]}'
        format = '%Y-%m-%d %H:%M:%S'
        if dodaj_delte:
            data = datetime.strptime(datestr, format) + delta
        else:
            data = datetime.strptime(datestr, format) - delta
        import datetime
        element_do_ostatecznej_listy = datetime.datetime(data.year,data.month,data.day,data.hour,data.minute,data.second,tzinfo=datetime.timezone.utc)
        lista_wyjscie.append(element_do_ostatecznej_listy)
        iter_wyd+=1

    return lista_wyjscie

def group_dates(dates):
    """
    Jeżeli o to chodzi to chyba działa...
    """
    #komentarz w parse_dates... tu tylko w kolejności ustawia
    from datetime import datetime
    sorted(dates,key=lambda date: datetime.strptime(str(date),'%Y-%m-%d %H:%M:%S+00:00'))

def format_day(day, events):
    """
    Jeżeli o to chodzi to chyba działa...
    """
    #zabawa z formatowaniem ...
    message = day
    if len(events)>1:
        for elem2 in events:
            message =message+'\n'+r'\t'+elem2
    elif len(events)==1:
        message = message +'\n'+ r'\t' + str(*events)
    return message


def parse_dates(date_str, date_format=''):
    """
    To jest dopiero ciekawa funkcja ... powinna działać ... ale nie działa mimo, że output jest taki identyczny z dokładnością do \t co odpowiedź z assert...
    """
    lista_z_datami=sort_dates(dates)
    group_dates(lista_z_datami)
    slownik = {} # uznałam, że z takim czymś będzie mi łatwiej ...
    #robię to grupowanie tutaj bo funkcja grupująca ma nic nie zrawcać więc nie mogę zrobić i zwrócić tego słownika z tamtej funcji, nie mogę też funkcją podrzędną uzupełnić jakiegoś słownika globalnego (a pzynajmniej nie umiem)
    for elem in lista_z_datami:
        day_jak_w_outpucie=str(elem.day)
        month_jak_w_outpucie=str(elem.month)
        if elem.day<10:
            day_jak_w_outpucie=f'0{elem.day}'
        if elem.month < 10:
            month_jak_w_outpucie=f'0{elem.month}'
        if str(elem.year) + '-' + month_jak_w_outpucie + '-' + day_jak_w_outpucie in slownik:
            slownik[str(elem.year) + '-' + month_jak_w_outpucie + '-' + day_jak_w_outpucie] = [*slownik[str(elem.year) + '-' + month_jak_w_outpucie + '-' + day_jak_w_outpucie],str(elem.hour) + ':' + str(elem.minute) + ':' + str(elem.second)]
        else:
            slownik[str(elem.year) + '-' + month_jak_w_outpucie + '-' + day_jak_w_outpucie] = [str(elem.hour) + ':' + str(elem.minute) + ':' + str(elem.second)]

    output=r'"""'
    iter2=0
    for elem in slownik:
        out=output
        if iter2>0:
            output = '\n'+f"{out}"+"\n----\n"
        output=f"{output}"+f"{format_day(elem,slownik[elem])}"

        iter2+=1

        if iter2 == (len(slownik)):
           output = f'{output}'+r'"""'
    print(output)
    return output

dates = """
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
"""

assert sort_dates(dates) == [
    datetime.datetime(2015, 5, 10, 20, 54, 36, tzinfo=datetime.timezone.utc),
    datetime.datetime(2015, 5, 10, 13, 54, 36, tzinfo=datetime.timezone.utc),
    datetime.datetime(2015, 5, 2, 14, 24, 36, tzinfo=datetime.timezone.utc),
    datetime.datetime(2015, 5, 1, 13, 54, 36, tzinfo=datetime.timezone.utc),
]

assert parse_dates(dates) == """2015-05-10
\t20:54:36
\t13:54:36
----
2015-05-02
\t14:24:36
----
2015-05-01
\t13:54:36"""

