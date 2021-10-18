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
    assert medArt([10, 2, 5], 6) is False


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
    return nr


def lAdgNrDvz(l):
    '''
    Functie ce returneaza lista dupa ce se adauga dupa fiecare numar, numarul sau de divizori proprii.
    :param l: lista cu numere intregi
    :return: rez, lista dupa ce se adauga numarul de divizori primi
    '''
    rez=[]
    for x in l:
        rez.append(x)
        rez.append(nrDvzProp(x))
    return rez


def test_lAdgNrDvz():
    assert lAdgNrDvz([19, 5, 24, 12, 9]) == [19, 0, 5, 0, 24, 6, 12, 4, 9, 1]
    assert lAdgNrDvz([17, 13, 11, 6, 9]) == [17, 0, 13, 0, 11, 0, 6, 2, 9, 1]


def nrAparitii(l,x):
    '''
    Functie ce returneaza nr de aparatii a lui x in lista l.
    :param l: lista
    :param x: numar intreg
    :return: numarul de aparitii
    '''
    nr=0
    for i in l:
        if i==x:
            nr=nr+1
    return nr


def lEfectuare(l):
    '''
    Functie ce returneaza lista dupa ce nr sunt inlocuite cu un tuplu.
    :param l: lsita cu nr intregi
    :return: lista schimba cu tuplu
    '''
    rez=[]
    for x in range(len(l)):
        rez.append((l[x],x,nrAparitii(l,l[x])))
    return rez


def test_lEfectuare():
    assert lEfectuare([25, 13, 26, 13]) == [(25, 0, 1), (13, 1, 2), (26, 2, 1), (13, 3, 2)]
    assert lEfectuare([5,3,5,9,3]) == [(5, 0, 2), (3, 1, 2), (5, 2, 2), (9, 3, 1), (3, 4, 2)]


def main():
    test_lFaraNrPrim()
    test_medArt()
    test_lAdgNrDvz()
    test_lEfectuare()

    l=[]
    while True:
        print("1. Citirea listei.")
        print("2. Lista dupa eliminarea numerelor prime.")
        print("3. Să se afișeze dacă media aritmetică a numerelor este mai mare decât un număr n dat.")
        print("4. Afișarea listei obținută prin adăugarea după fiecare element numărul de divizori proprii ai elementului.")
        print("5. Afisarea listei, dupa ce nr sunt inlocuite cu un tuplu.")
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
        elif optiune == "5":
            print(lEfectuare(l))
        elif optiune == "a":
            print(l)
        else:
            input("Optiune invalida. Reincercati")

main()