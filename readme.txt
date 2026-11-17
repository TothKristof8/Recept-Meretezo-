# Hallgató neve: Tóth Kristóf
# Neptun-kód: QUF1ND

## Feladat leírása
A program egy Recept-Méretező alkalmazás, amely egy alaprecept hozzávalóit (esetünkben palacsinta) képes felszorozni vagy leosztani a felhasználó által megadott adagszám alapján. Az eredményt a grafikus felületen megjeleníti, majd automatikusan elmenti egy SQLite adatbázisba (`recept.db`), az ablak bezárásakor pedig kilistázza a mentett adatokat a konzolra.
A program használatához csak a Python és a beépített Tkinter, illetve sqlite3 modulok szükségesek, külső csomag telepítése nem kell. Indítása a `main.py` fájl futtatásával történik.

## Felépítés
- **Modul**: `tk_modul.py` (Külső adatbázis-kezelést és számolást végző saját modul)
- **Függvények**:
  - `szorzo_kalkulator_tk`: Kiszámolja a régi és új adagok hányadosát.
  - `adat_formatum_tk`: Kiszámolja és formázza a hozzávalókat.
  - `mentes_sqlite_tk`: Létrehozza az SQLite táblát és beszúrja a kiszámolt adatokat.
  - `adatbazis_kiolvasas_tk`: Kiolvassa és a konzolra írja az SQLite adatbázisban tárolt sorokat.
- **Osztályok**: `ReceptMeretezoTK` (A grafikus felületet és az eseménykezelést megvalósító saját osztály a main.py-ban)