try:
    x = int(input("Sisesta arv: "))
    if x > 0:
        print("Positiivne arv")
        print("See rida on ka if-i sees")
    print("See rida täidetakse alati")
except ValueError:
    print("Palun sisesta kehtiv täisarv.")

# if…else lause
try:
    x = int(input("Sisesta arv: "))
    if x == 1:
        print("Õige")
    else:
        print("Vale")
except ValueError:
    print("Palun sisesta kehtiv täisarv")

# tingimised
vastus = input("Kas soovid jätkata? (jah/ei)")
if vastus.lower() == "jah":
    print("Jätkame!")
else:
    print("Head aega!")

# if...elif...else lause
try:
    x = int(input("Sisesta arv -5 kuni 5: "))
    if x < -5:
        print("Vähe")
    elif -5 <= x <= 5:
        print("OK")
    else:
        print("Palju")
except ValueError:
    print("Palun sisesta täisarv.")

# Plokksüsttemid kood kontroll
try:
    summa = float(input("Sisesta summa:"))
    if summa > 2000:
        hind = summa * 0.8
    elif summa > 1000:
        hind = summa * 0.9
    else:
        hind = summa
    print("Hind:", hind)
except ValueError:
    print("Palun sisesta täisarv")