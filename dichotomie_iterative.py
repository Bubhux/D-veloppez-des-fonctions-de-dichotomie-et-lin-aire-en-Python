"""Recherches d'un élément dans une liste.
   dichotomique, itérative
"""
from typing import List

number_value_intput = input("Choice as number :\n> ")
number_value_intput = int(number_value_intput)

def dichotomie_iterative(liste: List[int], number_value: int) -> int:
    """Recherche dichotomique et iérative de la valeur val dans la liste triée liste_sorted.
    Retourne l'indice de number_value dans la liste ou not found si number_value ne fait pas partie de la liste.
    """
    indice_left = 0
    indice_right = len(liste) -1
    find = False

    while indice_left <= indice_right and not find:
        mid_list = (indice_left + indice_right)//2

        if liste[mid_list] == number_value:
            find = True
            print(f"{(number_value)} is found")
            return print(f"Its index of value is {(mid_list)}")

        elif liste[mid_list] > number_value:
            indice_right = mid_list -1
        else:
            indice_left = mid_list +1

    if find:
        return mid_list
    else:
        return print(f"{(number_value)} is not found")


if __name__ == "__main__":
    liste_sorted = [1, 3, 4, 18, 20, 36, 38]
    number_value = number_value_intput
    indice_left = 0
    indice_right = len(liste_sorted) -1

    dichotomie_iterative(liste_sorted, number_value)
