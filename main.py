import tkinter as tk
from tkinter import ttk, messagebox
import tk_modul

class ReceptMeretezoTK:
    def __init__(self, root):
        self.root = root
        self.root.title("Recept-Méretező")
        self.root.geometry("450x550")
        
        self.recept_nev = "Palacsinta"
        self.alap_adag = 4
        self.hozzavalok = {
            "Finomliszt (g)": 200,
            "Tej (ml)": 300,
            "Tojas (db)": 2,
            "So (csipet)": 1,
            "Etolaj (ek)": 2
        }
        
        self.felulet_felepitese_tk()

    def felulet_felepitese_tk(self):
        ttk.Label(self.root, text=self.recept_nev, font=("Arial", 16)).pack(pady=10)
        
        self.uj_adag_var = tk.StringVar(value="6")
        ttk.Entry(self.root, textvariable=self.uj_adag_var, width=10).pack(pady=5)
        
        ttk.Button(self.root, text="Szamol es Ment", command=self.szamol_es_ment_tk).pack(pady=10)
        
        self.eredmeny_szoveg = tk.Text(self.root, height=12, width=40)
        self.eredmeny_szoveg.pack(pady=10)

    def szamol_es_ment_tk(self):
        try:
            uj_adag = int(self.uj_adag_var.get())
            if uj_adag <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Hiba", "Hibas adat!")
            return
        
        szorzo = tk_modul.szorzo_kalkulator_tk(self.alap_adag, uj_adag)
        aktualis_hozzavalok, kiiras = tk_modul.adat_formatum_tk(self.hozzavalok, szorzo)
        
        self.eredmeny_szoveg.delete("1.0", tk.END)
        self.eredmeny_szoveg.insert(tk.END, kiiras)
        
        tk_modul.mentes_sqlite_tk("recept.db", uj_adag, aktualis_hozzavalok)
        messagebox.showinfo("Siker", "Adatbazisba mentve!")

if __name__ == "__main__":
    ablak = tk.Tk()
    app = ReceptMeretezoTK(ablak)
    ablak.mainloop()
    tk_modul.adatbazis_kiolvasas_tk("recept.db")