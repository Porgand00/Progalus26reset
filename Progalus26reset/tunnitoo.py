print("Tere, maailm!")
print("Õpin Pythonit.")


print("Ma õpin",1,"kursusel")#print väljastab info ekraanile
print("Aasta on",2026)

kursus=1 #int
aasta=2026 #int

print("Ma õpin",1,"kursusel")#print väljastab info ekraanile
print("Aasta on",2026)

print("aastal",aasta,"olen juba",kursus+1, "kursusel")

print("2026","10","01",sep="/") #sep=" " määrab, mis eralab väljastavatavaid väärtusi
print("Sama",end="") # end="/n" määrab, mis pannakse lõppu ,vaiikimisi on see reavahetus.
print("rida")

#sisendamine
nimi=input("sistesta oma nimi: ") #funktsioon ,mis võimaldab kastujala sisestada väärtust
print("Tere",nimi,"!") #print väjastab info ekraanile

#Teised andmetüübid
a = input("Esimene arv: ") #str 2->"2"
b = input("Teine arv: ") #str
print(a + b)

a = int(input("Esimene arv: ")) #int("1")->1, float 1.0->1.0
b = int(input("Teine arv: "))
print(a + b)

#Põhioperatsioonid
print("Liitmine: ")
a = float(input("Esimene arv: "))
b = float(input("teine arv: "))
print (a,"+",b,"=", a + b)

print("Lahutamine : ")
a = float(input("Esimene arv: "))
b = float(input("teine arv: "))
print (a,"-",b,"=", a - b)

#tõevarsus
p = True
q = False
print(not p, p and q, p or q)
print(5 > 3 and 2 > 4)#-> True
print(5 > 3 and 2 > 4)#-> False

#Formatimine
nimi = "Mari"
punktid = 87
print(f"{nimi} sai {punktid} punkti. ")

hind = 19.9
kogus = 3
print(f"Kokku: {hind * kogus:.2f}eurot") #ümardub kahe komakohani

#Matemaatilised funktsioonud
import math

print("Pii väärtus:", math.pi) # pii väärtus
print("√16 =", math.sqrt(16)) # Ruutelement 
print("sin(π/2) =", math.sin(math.pi / 2)) # Sinus
print("sin(30°) =", round(math.sin(math.radians(30)), 2)) # Sinus
print("5! =", math.factorial(5)) # Faktoriall 1*2*3*4*5=120