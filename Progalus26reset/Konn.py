# 1.
# Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
# Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.

# Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:

# “Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”
print ("Tere, maailm!")
nimi=input("sistesta oma nimi: ") 
print(f"Tere, maailm! Tervitan sind {nimi}!") 
vanus=int(input("Sisesta oma vanus: ")) #int() teisendab stringi täisarvuks
print(f"Tere, maailm! Tervitan sind {nimi}! sa oled {vanus} aastat vana.")

# Ülesanne 2
# Mis tüüpi on järgnevad muutujad:

# a) vanus = 18
# b) eesnimi = "Jaak"
# c) pikkus = 16.5
# d) kas_käib_koolis = True
# Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
# Kirjuta kood tüüpide kontrollimiseks.

vanus=18 #int
eesnimi="jaak" #str
pikkus=16.5 #float
kas_käib_koolis=True #bool
print(f"Muutuja: {vanus}, tüüp: {type(vanus)}")
print(f"Muutuja: {eesnimi}, tüüp: {type(eesnimi)}")
print(f"Muutuja: {pikkus}, tüüp: {type(pikkus)}")
print(f"Muutuja: {kas_käib_koolis}, tüüp: {type(vanus)}")


# 3
# Kirjuta enda koodis laual olevate kommide arv muutujasse(kommide arv on juhuslik).
# Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
# Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta.
# Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile,
# kui palju komme laual nüüd on.
from random import * #randint
kommide_arv=randint(1,100) #kommide arv on juhuslik arv vahemikus 1-100)
print(f"Laual on {kommide_arv} kommi.")
try:
    kommid=int(input("Mitu kommi soovid laualt ära võtta? "))
    kommide_arv -= kommid #kommid_arv väheneb kommi võrra
    print(f"Laual on nüüd {kommide_arv} kommi.")
except:
    print("Sisesta arv")


# 4
# Puu läbimõõdu arvutamine
# Kirjuta programm,
# mis küsib kasutaja käest puu ümbermõõdu
# ning teatab selle peale puu läbimõõdu.
from math import * #pi, sqrt()
try:
    ümbermõõt=float(input("Sisesta puu ümbermõõt: ")) #Tesiednab stringi kuju komarvuks
    läbimõõt=ümbermõõt/pi
    print(f"Puu läbimõõt on {läbimõõt}.")
except:
    print("Sisesta mingi arv ")

# Ülesanne 5
# Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal,
# mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.
N=float(input("Sisesta risküliku 1. külje pikkus: "))
M=float(input("Sisesta risküliku 2. külje pikkus: "))
d=sqrt(N**2+M**2)
print(f"Rsiküliku diogonaal on {d}.")

# Ülesanne 6
# Leidke järgnevast näiteprogrammist loogiline viga:
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus/aeg

print("Sinu kiirus oli " + str(kiirus) + " km/h")

# Ülesanne 7
# Koostada programm, mis arvutab aritmeetilise keskmise
# suvalisest etteantud 5 täis arvust.
# Leia nende arvude summa, jagatuna kasutaja poolt sisestatud arvuga,
# täisarvuline osa ja jääk.
arv1=int(input("Sisesta 1. täisarv: "))
arv2=int(input("Sisesta 2. täisarv: "))
arv3=int(input("Sisesta 3. täisarv: "))

arv4=int(input("Sisesta 4. täisarv: "))
arv5=int(input("Sisesta 5. täisarv: "))
keskmine=(arv1+arv2+arv3+arv4+arv5)/5
Summa=arv1+arv2+arv3+arv4+arv5
print(f"Arvude summa on {Summa}. ")
print(f"Arvude keskmine on {keskmine}.")
täisosa=Summa//5
jääk=Summa%5
print(f"Täisosa on {täisosa}.")
print(f"Jääk on {jääk}.")


# Ülesanne 8
# Joonista samasugune konn
#    @..@
#    (----)
#   ( \__/ )
# ^^ "" ^^  
print("  @..@")
print("  (----)")
print(" ( \__/ )")
print("^^ "" ^^")

# Ülesanne 9
# Arvutame kolmnurga ümbermõõdu.
# Loo kolm täisarvulist muutujat a, b, c. Kasuta valem,
# mis arvutab kolmnurga ümbermõõdu (P=a+b+c)
a=int(input("Sisesta 1. täisarv: "))
b=int(input("Sisesta 2. täisarv: "))
c=int(input("Sisesta 3. täisarv: "))
P=a+b+c

# Ülesanne 10
# Pitsa
# Võtsite sõpradega (näiteks P inimest) suure pitsa, mille hind on 12,90 €.
# Jätate teenindajale 10% jootraha.
# Koosta programm, mis arvutab, kui palju igaüks peab maksma.

P = int(input("Mitu inimest pitsat sõid? ")) # Küsitakse inimeste arvu

pitsa_hind = 12.90 #pitsa hind
jootraha = pitsa_hind * 0.10 #Jootraha arvutamine
kokku = pitsa_hind + jootraha 
igaüks_maksab = kokku / P

# Tulemuse kuvamine (ümardatuna 2 komakohani)
print(f"Igaüks peab maksma: {round(igaüks_maksab, 2)} ")