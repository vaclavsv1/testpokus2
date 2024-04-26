print("--------------------------------------------------------------")
print("Vítejte v našem obchodě")
print("--------------------------------------------------------------")
print("Vybírat můžete podle názvu produktu")
print("--------------------------------------------------------------")
print("Program ukončít pomocí čísla 9")
print("--------------------------------------------------------------")


zbozi = ["Klávesnice","Herní myš","Podložka","Monitor","Sluchátka"]
kosik = []

while True:
    for x in range(len(zbozi)):
        print(f"Zboží s číslem {x + 1}: {zbozi[x]}")

    def vypis_pole(prvek):
        for x in range(len(prvek)):
            print(f"Zboží s číslem {x + 1}: {prvek[x]}")

    print("--------------------------------------------------------------")
    prvek_minus = input("Co chcete vložit do košíku? ")
    zbozi.remove(prvek_minus)

    kosik.append(prvek_minus)

    print("--------------------------------------------------------------")
    print("Stav vašeho košíku")
    print(kosik)
    print("--------------------------------------------------------------")

    print("Co dalšího si chcete vložit do košíku?")
    print("--------------------------------------------------------------")

    if len(zbozi) == 9:
       break