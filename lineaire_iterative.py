"""Recherches d'un élément dans une liste.
   linéaire, itérative
"""
from typing import List

number_value_intput = input("Choice as number :\n> ")
number_value_intput = int(number_value_intput)

def lineaire_iterative(liste: List[int], number_value: int) -> int:
    """Recherche linéaire et itérative de number_value dans la liste liste_sorted.
    Retourne le premier indice de number_value dans la liste ou not found si number_value ne fait pas partie de la liste.
    """
    find = False
    indice = 0
    while indice < len(liste) and not find:
        if liste[indice] == number_value:
            find = True
            print(f"{(number_value)} is found")
            return print(f"Its index of value is {(indice)}")

        else:
            indice += 1

    if find:
        return indice
    else:
        return print(f"{(number_value)} is not found")


if __name__ == "__main__":
    liste_sorted = [1, 3, 4, 18, 20, 36, 38]
    number_value = number_value_intput

    lineaire_iterative(liste_sorted, number_value)
