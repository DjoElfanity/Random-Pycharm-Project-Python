def sum_odd_and_even(lst):
    somme_odd =0
    somme_even= 0
    for i in range(len(lst)):

        if lst[i] %2 == 0:
            somme_even += lst[i]

        else:
            somme_odd += lst[i]
    liste_final = [somme_even,somme_odd]

    return liste_final




print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))