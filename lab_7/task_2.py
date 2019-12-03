import numpy as np


def calculate_neighbours(board):
    """
    Returns number of neighbours of board cells.
    Funkcja zwraca tablicę która w polu [R, C] zwraca liczbę sąsiadów którą
    ma komórka board[R, C].
    Obowiązuje sąsiedztwo Moore'a tzn. za sąsiada uznajemy żywą komórkę
    stykającą się bokiem bokach lub na ukos od danej komórki,
    więc maksymalna ilość sąsiadów danej komórki wynosi 8.
    Funkcja ta powinna być zwektoryzowana, tzn. liczba operacji w bytecodzie
    Pythona nie powinna zależeć od rozmiaru macierzy.
    (1 pkt.)
    Podpowiedź: Czy jest możliwe obliczenie ilości np. lewych sąsiadów
    których ma każda z komórek w macierzy, następnie liczby prawych sąsiadów
    itp.
    Podpowiedź II: Proszę uważać na komówki na bokach i rogach planszy.
    :param board: 2D array of agents states.
    :type board: np.ndarray
    :param periodic
    """
    cell_neighbour = np.zeros(board.shape, int)
    cell_neighbour[1:, 1:] += board[:-1, :-1]# lewy górny
    cell_neighbour[:, 1:] += board[:, :-1] #lewy
    cell_neighbour[:-1, 1:] += board[1:, :-1] #lewy dolny
    cell_neighbour[1:, :-1] += board[:-1, 1:] #prawy górny
    cell_neighbour[:, :-1] += board[:, 1:] #prawy
    cell_neighbour[:-1, :-1] += board[1:, 1:] #prawy dolny
    cell_neighbour[1:] += board[:-1] #górny
    cell_neighbour[:-1] += board[1:] #dolny

    return cell_neighbour



def iterate(board):
    """
    Returns next iteration step of given board.
    Funkcja pobiera planszę game of life i zwraca jej następną iterację.
    Zasady Game of life są takie:
    1. Komórka może być albo żywa (True) albo martwa (False).
    2. Jeśli komórka jest martwa i ma trzech sąsiadów to ożywa.
    3. Jeśli komórka jest żywa i ma mniej niż dwóch sąsiadów to umiera,
       jeśli ma więcej niż trzech sąsiadów również umiera.
       W przeciwnym wypadku (dwóch lub trzech sąsiadów) to żyje dalej.
    (1 pkt.)
    :param board: 2D array of agents states.
    :type board: np.ndarray
    :return: next board state
    :rtype: np.ndarray
    """
    cell_neighbours = calculate_neighbours(board)
    new = np.zeros_like(board) #the same sahpe and type
    new[board] = np.logical_or(cell_neighbours[board] == 2, cell_neighbours[board] == 3) #smierc gdy żyła miała coś innego lub 2/3
    new[np.logical_not(board)] = cell_neighbours[np.logical_not(board)] == 3 # wskrzeszenie gdy ma 3
    return new


if __name__ == '__main__':
    _board = np.array([
        [False, False, False,  True, False,  True],
        [ True, False,  True, False, False,  True],
        [ True,  True, False,  True,  True,  True],
        [False,  True,  True, False, False,  True],
        [False, False, False,  True, False, False],
        [False,  True,  True,  True, False,  True]
    ])
    assert (calculate_neighbours(_board) == np.array([
        [1, 2, 2, 1, 3, 1,],
        [2, 4, 3, 4, 6, 3,],
        [3, 5, 5, 3, 4, 3,],
        [3, 3, 4, 4, 5, 2,],
        [2, 4, 6, 3, 4, 2,],
        [1, 1, 3, 2, 3, 0,],
    ])).all()
    assert (iterate(_board) == np.array([
        [False, False, False, False, True, False],
        [ True, False,  True, False, False,  True],
        [ True, False, False,  True, False,  True],
        [True,  True, False, False, False,  True],
        [False, False, False,  True, False, False],
        [False, False,  True,  True, True, False],
    ])).all()

