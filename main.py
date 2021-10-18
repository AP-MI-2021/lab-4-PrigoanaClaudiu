def citLista():
    l=[]
    gstring=input("Dati lista de numere intregi, despartite prin virgula: ")
    nrasstring=gstring.split(",")
    for x in nrasstring:
        l.append(int(x))
    return l


def nrprim(x):
    '''
    Functie ce returneaza True daca un numar este prim, sau False in caz contrar
    :param x: numarul intreg
    :return: True daca este prim, False daca nu este prim
    '''
    if x<2:
        return False
    else:
        for i in range(2,x//2+1):
            if x%i == 0:
                return False
    return True


def lFaraNrPrim(l):
    '''
    Functie ce afiseaza lista dupa eliminarea tuturor elementelor prime.
    :param l: lista de numere intregi
    :return: rez, lista dupa eliminarea elementelor
    '''
    rez=[]
    for i in l:
        if nrprim(i) == False:
            rez.append(i)
    return rez


def test_lFaraNrPrim():
    assert lFaraNrPrim([8, 19, 17, 25]) == [8,25]
    assert lFaraNrPrim([6,18,7,9]) == [6,18,9]
    assert lFaraNrPrim([7,9,11]) == [9]


def medArt(l,n):
    '''
    Fucntie ce returneaza True daca media art. a numerelor din lista este mai mare decat numarul n dat, sau False in caz contrar.
    :param l: lista de nuemre intregi
    :param n: numarul n dat
    :return: True daca ma. este mai mare ca n sau False in caz contrar.
    '''
    s=0
    nr=0
    for x in l:
        s=s+x
        nr=nr+1
    if s/nr > n:
        return True
    else:
        return False


def test_medArt():
    assert medArt([10, -3, 25, -1, 3, 25, 18],10) is True
    assert medArt([5,10,2,4],5) is False


def nrDvzProp(x):
    '''
    Functie ce returneaza numarul de divizori proprii a lui x.
    :param x: numarul intreg
    :return: numarul de divizori proprii
    '''
    nr=0
    for i in range(2,x//2+1):
        if x%i == 0:
            nr=nr+1
    return 0



def main():
    test_lFaraNrPrim()
    test_medArt()
    l=[]
    while True:
        print("1. Citirea listei.")
        print("2. Lista dupa eliminarea numerelor prime.")
        print("3. Să se afișeze dacă media aritmetică a numerelor este mai mare decât un număr n dat.")
        print("4. Afișarea listei obținută prin adăugarea după fiecare element numărul de divizori proprii ai elementului.")
        print("a. Afisarea listei.")
        print("x. Iesire.")
        optiune=input("Dati optiunea:")
        if optiune == "x":
            break
        elif optiune == "1":
            l=citLista()
        elif optiune == "2":
            print(lFaraNrPrim(l))
        elif optiune == "3":
            n=int(input("Dati numarul n: "))
            if medArt(l,n):
                print("DA.")
            else:
                print("NU.")
        elif optiune == "4":
            print(lAdgNrDvz(l))
        elif optiune == "a":
            print(l)
        else:
            input("Optiune invalida.")

main()