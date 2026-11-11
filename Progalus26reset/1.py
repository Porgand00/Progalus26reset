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
    temperatuur=float(input ("Sisesta toatemperatuur kraadides: "))
    if tmeperatuur > 18:
        print("Toatemperatuur on 18 kraddid või madalam")
except ValueError:
 print("Palun sisesta temperatuur numbrina")