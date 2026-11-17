import sqlite3

def szorzo_kalkulator_tk(alap_adag, uj_adag):
    return uj_adag / alap_adag

def adat_formatum_tk(hozzavalok, szorzo):
    aktualis = {}
    szoveg = ""
    for nev, mennyiseg in hozzavalok.items():
        uj_mennyiseg = round(mennyiseg * szorzo, 1)
        if uj_mennyiseg.is_integer():
            uj_mennyiseg = int(uj_mennyiseg)
        aktualis[nev] = uj_mennyiseg
        szoveg += f"{nev}: {uj_mennyiseg}\n"
    return aktualis, szoveg

def mentes_sqlite_tk(db_nev, adag, adatok):
    conn = sqlite3.connect(db_nev)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS hozzavalok (id INTEGER PRIMARY KEY AUTOINCREMENT, adag INTEGER, nev TEXT, mennyiseg REAL)")
    for nev, mennyiseg in adatok.items():
        cursor.execute("INSERT INTO hozzavalok (adag, nev, mennyiseg) VALUES (?, ?, ?)", (adag, nev, mennyiseg))
    conn.commit()
    conn.close()

def adatbazis_kiolvasas_tk(db_nev):
    try:
        conn = sqlite3.connect(db_nev)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM hozzavalok")
        sorok = cursor.fetchall()
        conn.close()
        print("\n--- Mentett adatok az adatbázisból ---")
        for sor in sorok:
            print(f"ID: {sor[0]} | Adag: {sor[1]} | {sor[2]}: {sor[3]}")
    except sqlite3.OperationalError:
        print("\nMég nincs mentett adat az adatbázisban.")