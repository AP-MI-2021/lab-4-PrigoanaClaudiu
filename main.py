def cit_lista():
    l=[]
    gstring=input("Dati lista de numere, despartite prin virgula: ")
    nrasstring=gstring.split(",")
    for x in nrasstring:
        l.append(float(x))
    return l


def nrintregi(l):
    '''

    :param l:
    :return:
    '''
    rezultat=[]
    for x in l:
        if x.is_integer():
            rezultat.append(x)
    return rezultat


def test_nrintregi():
    assert nrintregi([5.0,6.2,7.9]) == [5.0]
    assert nrintregi([3.2,2.7,8.9]) == []
    assert nrintregi([6.9,5.0,3.1,7.0]) == [5.0,7.0]


def maxnr(l,k):
    '''

    :param l:
    :param k:
    :return:
    '''
    maxi=None
    for x in l:
        if x % k == 0 and (maxi == None or x > maxi):
            maxi=x
    return maxi


def test_maxnr():
    assert maxnr([5.2,6.3,8.2,14],2) == 14
    assert maxnr([6.3, 9.1, 4.0, 12.1, 12], 3) == 12


def partefracpalindrom(l):
    '''

    :param l:
    :return:
    '''
    rez=[]
    for x in l:
        xStr=str(x)
        pf=xStr.split(".")[1]
        if pf == pf[::-1]:
            rez.append(x)
    return rez


def test_partefracpalindrom():
    assert partefracpalindrom([2.11,3.99,2.0,3.2]) == [2.11,3.99,2.0,3.2]
    assert partefracpalindrom([2.12,3.89,2.1,3.21]) == []


def prim(k:int):
    '''

    :param k:
    :return:
    '''
    ok=True
    if k < 2:
        ok=False
    else:
        for i in range(2,k//2+1):
            if k%i == 0:
                ok=False
    return ok


def procesarelista(l):
    '''

    :param l:
    :return:
    '''
    rez=[]
    for x in l:
        radical=x**0.5
        pi=int(radical)
        if prim(pi) == True:
            rez.append(str(x)[::-1])
        else:
            rez.append(x)
    return rez


def test_procesarelista():
    assert procesarelista([10.0, 100.0, 12.45, 50.0, 101.2]) == ['0.01', 100.0, '54.21', '0.05', 101.2]


def toatenrpozimparedescresc(l):
    '''

    :param l:
    :return:
    '''
    nrpoz=l[1::2]
    for i in range(len(nrpoz)-1):
        if nrpoz[i] < nrpoz[i+1]:
            return False
    return True


def nrcifre(l):
    '''

    :param l:
    :return:
    '''
    rez= []
    for x in l:
        rez.append(x)
        a=len(str(x))-1
        rez.append(a)
    return rez


def main():
    test_nrintregi()
    test_maxnr()
    test_procesarelista()
    l=[]
    while True:
        print("1. Citirea listei.")
        print("2. Afisarea numerelor intregi.")
        print("3. Afisarea celui mai mare nr dvz cu un numar dat.")
        print("4. Afisarea nr ale caror p. fractionara e palindrom.")
        print("5. Afișarea listei obținute din lista inițială în care float-urile cu partea întreagă a radicalului număr prim sunt puse ca string-uri cu caracterele în ordine inversă.")
        print("6. Sa se det daca nr de pe poz impare sunt descrescatoare.")
        print("7. Inserarea nr de cifre dupa fiecare numar.")
        print("a. Afisarea listei.")
        print("x. Iesire")

        optiune=input("Dati optiunea: ")
        if optiune == "x":
            break
        elif optiune == "1":
            l=cit_lista()
        elif optiune == "2":
            print(nrintregi(l))
        elif optiune == "3":
            k=int(input("Dati numaru: "))
            print(maxnr(l,k))
        elif optiune == "4":
            print(partefracpalindrom(l))
        elif optiune == "5":
            print(procesarelista(l))
        elif optiune == "6":
            if(nrpozimpare(l)):
                print("Da.")
            else:
                print("Nu.")
        elif optiune == "7":
            print(nrcifre(l))
        elif optiune == "a":
            print(l)
        else:
            input("Optiune invalida. Reincercati.")

main()

