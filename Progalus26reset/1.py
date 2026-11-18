#Jukku
#Programm küsib eesnime.
# Kui nimi on Juku,
# kuvatakse „Lähme Jukuga kinno!“,
# muidu teatatakse, et täna kinno ei minda.

# Programm peab Juku ära tundma ka siis, kui nimi on kirjutatud suurtähtedega (JUKU) või väiketähtedega (juku).
# Kui nimi on kirjutatud ainult suurtähtedega, lisa märkus „Ära karju, Juku!“.

nimi = input("Sisesta eesnimi: ")

if nimi.lower() == "juku":
  print("Lähme Jukuga kinno!")
  if nimi.isupper():
    print("Ära karju, Juku!")
else:
  print("täna kinno ei minda.")

#Ülesanne 2 Pinginaaber
# Küsi kahe inimese nimed. Kontrolli, kas mõlemad nimed koosnevad ainult tähtedest.
# Kui jah, teata kasutajale, kas nad on täna pinginaabrid või mitte.
# Kui mõnes nimes on numbreid või muid märke, kuva veateade.
# Otsusta ise, kuidas „pinginaabrid“ määratakse,
#  näiteks juhuslikult või nimede algustähtede järgi.

nimi1 = input("Sisesta esimese inimese nimi: ")
nimi2 = input("Sisesta teise inimese nimi: ")

# Kontrollime, kas mõlemas nimes on ainult tähed
if nimi1.isalpha() and nimi2.isalpha():
    # Teeme esimese tähe suureks
    nimi1 = nimi1.capitalize()
    nimi2 = nimi2.capitalize()
    
    # Otsustame näiteks nimede pikkuse järgi, kas nad istuvad koos
    if len(nimi1) == len(nimi2):
        print(f"{nimi1} ja {nimi2} on täna pinginaabrid!")
    else:
        print(f"{nimi1} ja {nimi2} ei ole täna pinginaabrid.")
else:
    print("Viga! Nimed võivad sisaldada ainult tähti.")

    #Ülesanne 3 
    # Küsime toa mõõtmed ja arvutame pindala
pikkus = float(input("Sisesta toa pikkus meetrites: "))
laius = float(input("Sisesta toa laius meetrites: "))

pindala = pikkus * laius
print("Põranda pindala on:", round(pindala, 2), "m²")

# Küsime remondisoovi kohta
soov = input("Kas soovid remonti teha? (jah/ei): ").lower()

if soov == "jah":
    materjali_hind = float(input("Sisesta põrandamaterjali ruutmeetri hind (€): "))
    materjali_kulu = pindala * materjali_hind
    print("Põranda vahetamise materjalikulu on:", round(materjali_kulu, 2), "€")
    
    # Lisaküsimus töö teostaja kohta
    tegija = input("Kas teed remondi ise või kasutad professionaali abi? (ise/professionaal): ").lower()
    
    if tegija == "professionaal":
        too_hind = float(input("Sisesta töö hind ruutmeetri kohta (€): "))
        koguhind = materjali_kulu + (pindala * too_hind)
        print("Remondi koguhind koos tööga on:", round(koguhind, 2), "€")
    else:
        print("Ise tehes on remondi koguhind:", round(materjali_kulu, 2), "€")
else:
    print("Selge, remonti ei tehta.")

 #Ülesanne 4 
alghind = float(input("Sisesta toote alghind: "))
if alghind > 700:
    hind = alghind * 0.7
else:
    hind = alghind

print(f"Lõplik hind on: {hind:.2f} eurot")
#5. Temperatuur
try:
    temperatuur = float(input("Sisesta temperatuur: "))
    if temperatuur <= 18:
        print("Toatemperatuur on 18 kraadi või madalam")
    else:
        print("Toatemperatuur on üle 18 kraadi")
except ValueError:
    print("Palun sisesta temperatuur numbrina")

print()

#Pikkus

try:
    pikkus = float(input("Sisesta inimese pikkus sentimeetrites: "))
    if 30<=pikkus < 160:
        print("Inimene on lühike.")
    elif 160 <= pikkus <= 180:
        print("Inimene on keskmise pikkusega")
    elif 180<pikkus<=220:
        print("Inimene on pikk.")
    else:
        print("Arv ei sobi")
except ValueError:
    print("Viga: Pakun sisesta pikkus numbrina.")

    #Ülesanne 7 pikkus ja sugu


    sugu = input("Sugu: ")
    if sugu.isapha():
       if sugu.lower() == "m" or sugu.upper() == "MEES":
        if 30 <= pikkus < 170:
            print("Mees on lühike.")
        elif 170 <= pikkus <= 185:
            print("Mees on keskmise pikkusega.")
        elif 185 < pikkus <= 220:
            print("Mees on pikk.")
        else:
            print("Arv ei sobi")

    elif sugu.lower() == "n" or sugu.upper() == "NAINE":
        if 30 <= pikkus < 160:
            print("Naine on lühike.")
        elif 160 <= pikkus <= 175:
            print("Naine on keskmise pikkusega.")
        elif 175 < pikkus <= 220:
            print("Naine on pikk.")
        else:
            print("Arv ei sobi")

    else:
        print("Viga: Kirjuta tähtedega.")

#         8. Poes

# Küsi kasutajalt iga toote kohta eraldi, kas ta soovib seda osta: piim, sai, leib ja vähemalt kaks toodet veel.

#     Toodete hinnad loo juhuslikult moodulist random, näiteks round(random.uniform(0.5, 3), 2).
#     Kui kasutaja soovib toodet osta, küsi kogus. Kontrolli, et kogus on täisarv (isdigit()).
#     Lõpus kuva tšekk: iga ostetud toote nimi, kogus, hind ja summa ning kõige all kogusumma.
from random import *
summa=0
arve="toode    Kogus    Hind    kokku/n"
valik=input("Kas soovid osta piima? (jah/ei)")
if valik.lower()=="Jah":
    kogus=input("Mitu piima soovid osta (int)  ")
    if kogus.isdigit():
        kogus=int(kogus)
        p_hind=round(uniform(0.5,3.6),2)
        print (f"Piima hind on {p_hind}")
        summa+=(kogus*p_hind,2)
        print (f"Piima kogusumm on {summa}")
        arve+=f"piim    {kogus}    {p_hind}    {round(uniform(0.5,3.6),2)}/n"
    else:
        print("Viga: Vale number")
else:
    print("Selge: piima ei taha")
arve="toode    Kogus    Hind    kokku/n"
valik=input("Kas soovid osta Leiba? (jah/ei)")
if valik.lower()=="Jah":
    kogus=input("Mitu Leiba soovid osta (int)  ")
    if kogus.isdigit():
        kogus=int(kogus)
        p_hind=round(uniform(0.5,3.6),2)
        print (f"Leiva hind on {p_hind}")
        summa+=(kogus*p_hind,2)
        print (f"Leiva kogusumm on {summa}")
        arve+=f"Leib    {kogus}    {p_hind}    {round(uniform(0.5,3.6),2)}/n"
    else:
        print("Viga: Vale number")
else:
    print("Selge: Leiba ei taha")
arve="toode    Kogus    Hind    kokku/n"
valik=input("Kas soovid osta Vett? (jah/ei)")
if valik.lower()=="Jah":
    kogus=input("Mitu Vett soovid osta (int)  ")
    if kogus.isdigit():
        kogus=int(kogus)
        p_hind=round(uniform(0.5,3.6),2)
        print (f"Vee hind on {p_hind}")
        summa+=(kogus*p_hind,2)
        print (f"Vee kogusumm on {summa}")
        arve+=f"Vee    {kogus}    {p_hind}    {round(uniform(0.5,3.6),2)}/n"
    else:
        print("Viga: Vale number")
else:
    print("Selge: Vett ei taha")
print ("Arver Nr. 1203948576")
print (arve)