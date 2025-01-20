import math

class Gosc:

    def __init__(self, imie, nazwisko, wiek):
        assert type(imie) == str
        assert type(nazwisko) == str
        assert type(wiek) == int
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
    
    def __str__(self):
        return (f"{self.imie} {self.nazwisko}, lat {self.wiek}")
    
def wczytaj_gosci(filename):
    f = open(filename, "r")
    a = []
    for line in f:
        #x = line
        #x = x.strip()
        x = line.strip().split(",")
        a.append(Gosc(x[0], x[1], int(x[2])))
    f.close()
    assert type(a) == list
    return a
    


def main():
    lista_gosci = wczytaj_gosci('lista_gosci.csv')
    print(wczytaj_gosci("lista_gosci.csv"))
    #print(lista_gosci[1])

if __name__ == "__main__":
    main()