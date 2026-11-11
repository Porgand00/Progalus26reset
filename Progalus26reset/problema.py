import calendar
from datetime import *

# ÜLESANNE 1
print("--- Ülesanne 1: Kuupäevad ja vanus ---")
try:
    print("Tere!")
    tana = date.today()
    print(f"Täna: {tana}\nFormaadid:")
    print(tana.strftime("%d/%m/%Y"), "|", tana.strftime("%B %d, %Y"))
    print(tana.strftime("%m/%d/%y"), "|", tana.strftime("%b-%d-%Y"))

    paevi_kuus = calendar.monthrange(tana.year, tana.month)[1]
    print(f"Kuu lõpuni: {paevi_kuus - tana.day} päeva")
    print(f"Aasta lõpuni: {(date(tana.year, 12, 31) - tana).days} päeva")

    s_aasta = int(input("Sünniaasta (AAAA): "))
    s_kuu = int(input("Sünnikuu (1-12): "))
    s_paev = int(input("Sünnipäev (1-31): "))
    synniaeg = date(s_aasta, s_kuu, s_paev)
    vanus_a = tana.year - s_aasta - ((tana.month, tana.day) < (s_kuu, s_paev))
    print(f"Vanus: {vanus_a} aastat. Kokku elatud: {(tana - synniaeg).days} päeva.\n")
except:
    print("Viga sisestuses või kuupäevas!\n")

# ÜLESANNE 2 
print("--- Ülesanne 2: Tehete järjekord ---")
v1 = 3 + 8 / (4 - 2) * 4  
v2 = 3 + 8 / 4 - 2 * 4  
v3 = (3 + 8) / (4 - 2) * 4  
print(f"1) 3 + 8 / (4 - 2) * 4 = {v1} (Sulgudes tehe tehakse esimesena)")
print(f"2) 3 + 8 / 4 - 2 * 4 = {v2} (Kõigepealt jagamine/korrutamine)")
print(f"3) (3 + 8) / (4 - 2) * 4 = {v3} (Mõlemad sulud enne)\n")

# ÜLESANNE 3 
print("--- Ülesanne 3: Ruut ja ring ---")
try:
    R = float(input("Sisesta ringi raadius R: "))
    PI = 3.14159
    a = 2 * R  
    print(f"Ruudu pindala: {round(a*a, 2)} | ümbermõõt: {round(4*a, 2)}")
    print(f"Ringi pindala: {round(PI*R*R, 2)} | ümbermõõt: {round(2*PI*R, 2)}\n")
except:
    print("Viga: Sisesta number!\n")

# ÜLESANNE 4 
print("--- Ülesanne 4: Maa ekvaator müntides ---")
R_KM = 6378  
MYNDI_MM = 25.75  
PI = 3.14159
ymbermoot_mm = 2 * PI * (R_KM * 1000 * 1000)  
myntide_arv = round(ymbermoot_mm / MYNDI_MM)  
print(f"Maa ümbermõõt: {round(ymbermoot_mm / 1000000, 2)} km.")
print(f"Vaja läheb umbes {myntide_arv:,} münti.\n")

# ÜLESANNE 5 
print("--- Ülesanne 5: kill-koll ---")
o1, o2 = "kill-koll", "killadi-koll"
rida1 = f"{o1} {o1} {o2} {o1} {o1} {o2} {o1} {o1} {o1}".title()
rida2 = o1.title()
print(rida1)
print(rida2, "\n")

# ÜLESANNE 6 
print("--- Ülesanne 6: Rongisõidu laul ---")
laul = """Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill."""
print(laul.upper(), "\n")

# ÜLESANNE 7 
print("--- Ülesanne 7: Ristküliku arvutused ---")
try:
    a = float(input("Külje pikkus A: "))
    b = float(input("Külje pikkus B: "))
    print(f"Ümbermõõt: {2 * (a + b)} | Pindala: {a * b}\n")
except:
    print("Viga: Palun sisesta numbrid!\n")

# ÜLESANNE 8 
print("--- Ülesanne 8: Kütusekulu ---")
try:
    L = float(input("Tangitud liitrid: "))
    KM = float(input("Läbitud kilomeetrid: "))
    print(f"Keskmine kulu 100km kohta: {round((L / KM) * 100, 2)} liitrit.\n")
except ZeroDivisionError:
    print("Kilomeetrid ei saa olla 0!\n")
except:
    print("Viga sisestuses!\n")

# ÜLESANNE 9 
print("--- Ülesanne 9: Rulluisutajad ---")
try:
    v = 29.9  
    m = float(input("Aeg minutites: "))
    print(f"Jõuab {m} minutiga {round(v * (m / 60), 2)} km kaugusele.\n")
except:
    print("Viga: Sisesta number!\n")

# ÜLESANNE 10 
print("--- Ülesanne 10: Ajateisendus ---")
try:
    minutid = int(input("Aeg minutites: "))
    print(f"Vastus {minutid // 60}:{minutid % 60:02d}\n")
except:
    print("Viga: Sisesta täisarv!\n")

print("Kõik ülesanded on täidetud!")