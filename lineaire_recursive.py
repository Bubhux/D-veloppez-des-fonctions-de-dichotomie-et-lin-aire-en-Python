"""Recherches d'un élément dans une liste.
   linéaire, récursive
"""
from typing import List

number_value_intput = input("Choice as number :\n> ")
number_value_intput = int(number_value_intput)

def lineaire_recursive(liste: List[int], number_value: int, indice_value: int) -> int:
    """Recherche linéaire et récursive de la valeur number_value dans la liste liste_sorted.
    indice_value est l'indice de recherche.
    Retourne le premier indice de number_value dans la liste ou not found si number_value ne fait pas partie de la liste.
    """
    if indice_value == len(liste):
        print(f"{(number_value)} is not found")
        return False

    elif liste[indice_value] == number_value:
        print(f"{(number_value)} is found")
        return print(f"Its index of value is {(indice_value)}")

    else:
        return lineaire_recursive(liste, number_value, indice_value +1)


if __name__ == "__main__":
    liste_sorted = [1, 3, 4, 18, 20, 36, 38]
    number_value = number_value_intput
    indice_value = 0

    lineaire_recursive(liste_sorted, number_value, indice_value)

