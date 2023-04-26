"""Recherches d'un élément dans une liste.
   dichotomique, récursive
"""
from typing import List

number_value_intput = input("Choice as number :\n> ")
number_value_intput = int(number_value_intput)

def dichotomie_recursive(liste: List[int], number_value: int, indice_left: int, indice_right: int) -> int:
    """Recherche dichotomique et récursive de la valeur number_value dans la liste liste_sorted.
    Retourne l'indice de number_value dans la liste ou not found si number_value ne fait pas partie de la liste.
    indice_left (gauche) et indice_right(droite) sont les indices servant de bornes lors de la recherche.
    """
    if indice_right < indice_left:
        print(f"{(number_value)} is not found")
        return False

    else:
        middle_list = (indice_left + indice_right)//2

        if liste[middle_list] == number_value:
            print(f"{(number_value)} is found")
            return print(f"Its index of value is {(middle_list)}")

        elif liste[middle_list] < number_value:
            return dichotomie_recursive(liste, number_value, middle_list +1, indice_right)

        else:
            return dichotomie_recursive(liste, number_value, indice_left, middle_list -1)


if __name__ == "__main__":
    liste_sorted = [1, 3, 4, 18, 20, 36, 38]
    number_value = number_value_intput
    indice_left = 0
    indice_right = len(liste_sorted) -1

    dichotomie_recursive(liste_sorted, number_value, indice_left, indice_right)
