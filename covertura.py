# Lab 04 | Actividad 03
def stats(lst):
    min = None
    max = None
    freq = {}
    for i in lst:
        if min is None or i < min:
            min = i
        if max is None or i > max:
            max = i
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    lst_sorted = sorted(lst)
    if len(lst_sorted) % 2 == 0:
        middle = int(len(lst_sorted) / 2)
        median = (lst_sorted[middle] + lst_sorted[middle - 1]) / 2
    else:
        median = lst_sorted[int(len(lst_sorted) / 2)]

    mode_times = None
    for i in freq.values():
        if mode_times is None or i > mode_times:
            mode_times = i

    mode = []
    for (num, count) in freq.items():
        if count == mode_times:
            mode.append(num)

    print("list = " + str(lst))
    print("min = " + str(min))
    print("max = " + str(max))
    print("median = " + str(median))
    print("mode(s) = " + str(mode))


def test():
    # Lista impar con valores unicos
    stats([3, 1, 4])
    # Lista par con 2 modos
    stats([1, 2, 2, 3, 3, 4])
    # Lista con un solo valor
    stats([5])
    # Lista con 1 modo unico
    stats([1, 2, 2, 3, 4])
    # Lista con todos los valores iguales
    stats([7, 7, 7, 7])
    # Lista con numeros consecutivos
    stats([1, 2, 3, 4, 5])
    # Lista con frecuencia variable
    stats([1, 1, 2, 3, 3, 3, 4, 5])
    # Actividad 04
    # Lista vacia (detecta error)
    stats([])
test()
