def priklad1(velikost, zacatek, znak):
    if not isinstance(velikost, int) or not isinstance(zacatek, int):
        print("ERROR") # ERROR bych spíš vracel, ale ze zadání je evidentní, že se má vypsat
        return
    if not isinstance(znak, str) or len(znak) != 1:
        print("ERROR")
        return
    if velikost < 3 or velikost > 10:
        print("ERROR")
        return
    if zacatek < 1 or zacatek > 10:
        print("ERROR")
        return
    

    for radek in range(velikost):
        spacing2 = velikost - 2
        if zacatek <= velikost and (radek == 0 or radek == velikost - 1):
            print(znak * (zacatek - 1) + velikost * znak)
        elif zacatek <= velikost:
            vnitrnivelikost = spacing2 - zacatek + 1
            if velikost == zacatek:
                special = 0
            else:
                special = 1
            print(znak + (zacatek - 2) * " " + znak + (vnitrnivelikost) * " " + special * znak + (zacatek - 2) * " " + znak)
        else:
            spacing = zacatek - velikost - 1
            if radek == 0 or radek == velikost - 1:
                print(znak * velikost + " " * spacing + znak * velikost)
            else:
                print(znak + " " * spacing2 + znak + " " * spacing + znak + " " * spacing2 + znak)

priklad1 (5, 5, 'X')

def priklad2(n, m, znak1, znak2):
    if not isinstance(n, int) or not isinstance(m, int) or not isinstance(znak1, str) or not isinstance(znak2, str):
        print("ERROR")
        return
    if n > 10 or m > 10 or n < 1 or m < 1:
        print("ERROR")
        return

    if znak1 == znak2:
        print("ERROR")
        return

    for i in range(m): 
        for j in range(n): 
            if (i + j) % 2 == 0:
                print(znak1, end='')
            else:
                print(znak2, end='')
        print()

priklad2 (10, 9, '#', 'o')

def priklad3(seznam, index):
    if not isinstance(seznam, list) or len(seznam) == 0:
        return (False, None)

    if not isinstance(index, int) or index < 0 or index >= len(seznam):
        return (False, None)

    for x in seznam:
        if not isinstance(x, (int, float)):
            return (False, None)

    hodnota = seznam[index]
    vyssi_cisla = []

    for i, cislo in enumerate(seznam):
        if cislo > hodnota:
            vyssi_cisla.append((abs(i - index), cislo, i))

    if not vyssi_cisla:
        return (False, None)

    vyssi_cisla.sort(key=lambda x: (x[0], x[1]))

    return (True, vyssi_cisla[0][1])

ret = priklad3 ([1, 2, 3, 5, 11, 6, 9, 7, 10, 5, 6], 6) 
print(ret)

