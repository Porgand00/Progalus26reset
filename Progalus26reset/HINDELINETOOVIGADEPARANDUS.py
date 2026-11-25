
valik=input("Millise programmi valid (1/2/3) ")
if valik.lower()=="1":
    print("aastaeg") #Parandasin juttumärgid
    kuu=int(input("Sisesta kuu number (1-12) => "))
    if kuu<1 or kuu>12:
        print("Vigane kuu")
    elif kuu==12 or kuu<=2: #extra võrdusmärk
        print("Talv")
    elif 3<=kuu<=5: #muutsin else if elifiks
        print("Kevad")
    elif 6<=kuu<=8:
        print("Suvi")
    else:
        print("Sügis")
    print()

elif valik.lower()=="2":
    print("Kiiruse kontroll")
    lubatud=int(input("Sisesta lubatud kiirus (km/h) => "))
    kiirus=int(input("Sisesta tegelik kiirus (km/h) => "))
    yletus=kiirus-lubatud
    if yletus <=0:
        print("Kiirust ei ületatud")
    elif yletus>40:
        print("Juhiluba võetakse ära")
    elif yletus>20:
        print("Trahv")
    elif yletus>0:
        print("Hoiatus")
    print()

elif valik.lower()=="3":
    print("Taksosõit")
    km=float(input("Sisesta sõidu pikkus (km) => "))
    oo=input("Kas sõit on öösel (jah/ei)? => ")
    hind=3+km*0.8
    if oo=="jah" or oo=="JAH":
        hind=hind*1.2
    print("Sõidu hind:", round (hind,2))
else:
    print("Vigane valik.")
