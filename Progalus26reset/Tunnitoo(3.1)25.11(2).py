import random

while True:
    print("\nVali:")
    valik = input("Ülesanded 1-13, 0 - Väljumiseks: ")
    if valik == "0":
        print("Programm lõpetab töö. Head aega!")
        break
    # Ülesanne 1
    elif valik == "1":
        print("Valisid 1. Sisestatakse 15 arvu. Määrata, mitu neist on täisarvud.")
        taisarvud = 0
        for i in range(15):
            while True:
                try:
                    arv = float(input(f"Sisesta {i+1}. arv: "))
                    if arv.is_integer():
                        taisarvud += 1
                    break
                except ValueError:
                    print("Palun sisesta korrektne arv!")
        print(f"Täisarve on kokku: {taisarvud}")
    # Ülesanne 2
    elif valik == "2":
        print("Valisid 2. Küsi kasutajalt arv A ja leia kõigi naturaalarvude summa vahemikus 1 kuni A.")
        summa = 0
        while True:
            try:
                A = int(input("Sisesta naturaalarv A: "))
                if A < 1:
                    print("Vale sisend! Palun sisesta naturaalarv (A >= 1).")
                else:
                    break
            except ValueError:
                print("Vale sisend! Palun sisesta täisarv.")
        for i in range(1, A + 1):
            summa += i
        print(f"Naturaalarvude summa vahemikus 1 kuni {A} on: {summa}")
    # Ülesanne 3
    elif valik == "3":
        print("Valisid 3. Sisestatakse 8 arvu, leia positiivsete arvude korrutis.")
        korrutis = 1
        positiivseid_leiti = False
        for i in range(8):
            arv = float(input(f"Sisesta {i + 1}. arv: "))
            if arv > 0:
                korrutis *= arv
                positiivseid_leiti = True
        if positiivseid_leiti:
            print("Positiivsete arvude korrutis on:", korrutis)
        else:
            print("Positiivseid arve ei sisestatud.")
    # Ülesanne 4
    elif valik == "4":
        print("Valisid 4. Väljasta arvude 10 kuni 20 ruudud.")
        for arv in range(10, 21):
            ruut = arv ** 2
            print(f"Arvu {arv} ruut on {ruut}")
    # Ülesanne 5
    elif valik == "5":
        print("Valisid 5. Sisestatakse N arvu, leia negatiivsete arvude summa.")
        n = int(input("Mitu arvu soovid sisestada? "))
        summa = 0
        loendur = 0
        while loendur < n:
            arv = int(input("Sisesta arv: "))
            if arv < 0:
                summa = summa + arv
            loendur = loendur + 1
        print("Negatiivsete arvude summa on:", summa)
    # Ülesanne 6
    elif valik == "6":
        print("Valisid 6.")
        print("Klaviatuurilt sisestatakse N arvu. Koosta programm, mis määrab sisestatud arvude seast: negatiivsete arvude arvu, positiivsete arvude arvu, nullide arvu (N väärtus sisestatakse klaviatuurilt).")
        n = int(input("Mitu arvu soovid sisestada (N)? "))
        negatiivsed = 0
        positiivsed = 0
        nullid = 0
        for i in range(n):
            arv = float(input(f"Sisesta {i + 1}. arv: "))
            if arv < 0:
                negatiivsed += 1
            elif arv > 0:
                positiivsed += 1
            else:
                nullid += 1
        print("\nTulemused:")
        print(f"Negatiivseid arve: {negatiivsed}")
        print(f"Positiivseid arve: {positiivsed}")
        print(f"Nulle: {nullid}")
    # Ülesanne 7
    elif valik == "7":
        print("Valisid 7. Väljasta ekraanile arvud, mis on K-ga jaguvad vahemikust [A, B]")
        a = int(input("Sisesta vahemiku algus (A): "))
        b = int(input("Sisesta vahemiku lõpp (B): "))
        k = int(input("Sisesta jagaja (K): "))
        print(f"Arvud vahemikus [{a}, {b}], mis jaguvad arvuga {k}:")
        for arv in range(a, b + 1):
            if arv % k == 0:
                print(arv)
    # Ülesanne 8
    elif valik == "8":
        print("Valisid 8. Tollide ja sentimeetrite teisendustabel (1 kuni 20 tolli).")
        for toll in range(1, 21):
            cm = toll * 2.5
            print(f"{toll} tolli = {cm} cm")
    # Ülesanne 9
    elif valik == "9":
        print("Valisid 9. Panka pandi S eurot 3% intressiga. Leia summa N aasta järel.")
        s = float(input("Sisesta algsumma (S eurot): "))
        n = int(input("Sisesta aastate arv (N): "))
        for aasta in range(1, n + 1):
            s = s * 1.03
        print(f"Summa {n} aasta järel on: {round(s, 2)} eurot")
    # Ülesanne 10
    elif valik == "10":
        print("Valisid 10. Võrdle 10 arvupaari ja väljasta suurem.")
        for i in range(1, 11):
            arv1 = float(input(f"Sisesta {i}. paari esimene arv: "))
            arv2 = float(input(f"Sisesta {i}. paari teine arv: "))
            if arv1 > arv2:
                print(f"Suurem arv on {arv1}")
            elif arv2 > arv1:
                print(f"Suurem arv on {arv2}")
            else:
                print("Arvud on võrdsed")
    # Ülesanne 11
    elif valik == "11":
        print("Valisid 11. Leia kahekohaliste paaritute arvude korrutis, mis on jaguvad juhuslikult genereeritud arvuga.")
        jagaja = random.randint(1, 99)
        print(f"Juhuslikult genereeritud arv on: {jagaja}")
        korrutis = 1
        leiti = False
        for arv in range(11, 100, 2):
            if arv % jagaja == 0:
                korrutis *= arv
                leiti = True
        if leiti:
            print(f"Kahekohaliste paaritute arvude korrutis, mis jaguvad arvuga {jagaja}, on: {korrutis}")
        else:
            print(f"Selliseid kahekohalisi paarituid arve ei leidu, mis jaguksid arvuga {jagaja}.")
    # Ülesanne 12
    elif valik == "12":
        print("Valisid 12. Heina niitmise brigaadi kogu tööaeg.")
        n = int(input("Sisesta niidukite arv (N): "))
        m = float(input("Sisesta esimese niiduki tööaeg tundides (m): "))
        koguaeg = 0
        praegune_aeg = m
        for i in range(n):
            koguaeg += praegune_aeg
            praegune_aeg += 10 / 60
        print(f"Kogu brigaad töötas kokku {round(koguaeg, 2)} tundi.")
    # Ülesanne 13
    elif valik == "13":
        print("Valisid 13. Naturaalarvud 100-st kuni 1000-ni, mis jaguvad 7-ga.")
        arvude_kogus = 0
        summa = 0
        for arv in range(100, 1001):
            if arv % 7 == 0:
                print(arv)
                arvude_kogus += 1
                summa += arv
        print(f"7-ga jaguvaid arve on kokku: {arvude_kogus}")
        print(f"Nende arvude summa on: {summa}")
    else:
        print("Tundmatu valik! Palun sisesta number vahemikus 0 kuni 13.")