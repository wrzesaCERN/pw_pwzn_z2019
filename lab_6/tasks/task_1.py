"""
Jesteś informatykiem w firmie Noe's Animals Redistribution Center.
Firma ta zajmuje się międzykontynentalnym przewozem zwierząt.
---------
Celem zadania jest przygotowanie funkcji pozwalającej na przetworzenie
pliku wejściowego zawierającego listę zwierząt do trasnportu.
Funkcja ma na celu wybranie par (samiec i samica) z każdego gatunku,
tak by łączny ładunek był jak najlżeszy (najmniejsza masa osobnika
rozpatrywana jest względem gatunku i płci).
---------
Na 1 pkt.
Funkcja ma tworzyć plik wyjściowy zwierający listę wybranych zwierząt
w formacie wejścia (takim samym jak w pliku wejściowym).
Wyjście ma być posortowane alfabetycznie względem gatunku,
a następnie względem nazwy zwierzęcia.
---------
Na +1 pkt.
Funkcja ma opcję zmiany formatu wejścia na:
"<id>_<gender>_<mass>"
(paramter "compressed") gdzie:
- "id" jest kodem zwierzęcia (uuid),
- "gender" to jedna litera (F/M)
- "mass" zapisana jest w kilogramach w notacji wykładniczej
z dokładnością do trzech miejsc po przecinku np. osobnik ważący 456 gramów
ma mieć masę zapisaną w postaci "4.560e-01"
---------
Na +1 pkt.
* Ilość pamięci zajmowanej przez program musi być stałą względem
liczby zwierząt.
* Ilość pamięci może rosnąć liniowo z ilością gatunków.
---------
UWAGA: Możliwe jest wykonanie tylko jednej opcji +1 pkt.
Otrzymuje się wtedy 2 pkt.
UWAGA 2: Wszystkie jednoski masy występują w przykładzie.
"""
from pathlib import Path
import csv
from collections import OrderedDict

def select_animals(input_path, output_path, compressed=False):
    with open(input_path, 'r') as _file:
        reader = csv.reader(_file, delimiter=',')
        header = next(reader, None)
        reader_dict = csv.DictReader(_file, delimiter=',', fieldnames=header)
        gatunki = set()
        plcie = ('male', 'female')
        units_dict = {'mg': 1e-6, 'g': 1e-3, 'kg': 1, 'Mg': 1e3}
        gender_dict = {'male': 'M', 'female': 'F'}

        for row in reader_dict:
            gatunki.add(row['genus'])

        wybrancy = []
        for gatunek in gatunki:
            for plec in plcie:
                _file.seek(0)
                selekcja = []
                dir_masy = {}
                for row in reader_dict:
                    if row['gender'] == plec:
                        if row['genus'] == gatunek:
                            value = float(row['mass'].split(' ')[0])*units_dict[row['mass'].split(' ')[1]]
                            dir_masy.update({value:row['mass']})
                            row['mass'] = value #na chwilę do sortowania...
                            selekcja.append(row)
                selekcja = sorted(selekcja, key=lambda i: i['mass'])
                selekcja[0]['mass'] = dir_masy[selekcja[0]['mass']] #wracamy do starego...
                wybrancy.append(selekcja[0])
        wybrancy = sorted(wybrancy, key=lambda iter: (iter['genus'], iter['name']))

    with open(output_path,'w') as _file:
        if compressed == False:
            writer = csv.DictWriter(_file, fieldnames=header)
            writer.writeheader()
            writer.writerows(wybrancy)
        elif compressed == True:
            writer = csv.writer(_file, delimiter=',', quotechar="*")
            writer.writerow(['uuid_gender_mass'])
            for element in wybrancy:
                el1 = element['id']
                el2 = gender_dict[element['gender']]
                el3 = float(element['mass'].split(' ')[0])*units_dict[element['mass'].split(' ')[1]]
                linia = '_'.join([el1,el2, '%.3e' % el3])
                _file.write(linia+'\n')

if __name__ == '__main__':
    input_path = Path('s_animals.txt')
    output_path = Path('s_animals_s.txt')
    select_animals(input_path, output_path)
    with open(output_path) as generated:
        with open('s_animals_se.txt') as expected:
            assert generated.read() == expected.read()

    output_path = Path('s_animals_sc.txt')
    select_animals(input_path, output_path, True)
    with open(output_path) as generated:
        with open('s_animals_sce.txt') as expected:
            assert generated.read() == expected.read()
