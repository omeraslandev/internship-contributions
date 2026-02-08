import sqlite3
import random
import tkinter as tk
from tkinter import ttk

# Telefon modelleri
telefon_modelleri = [
    "M7U",
    "MT6",
    "M8B",
    "MA7",
    "UT8",
    "Z8Y",
    "N10",
    "NOT1",
    "M8TA",
    "Y16"
]

def veritabani_olustur():
    try:
        conn = sqlite3.connect('telefon_barkod.db')
        cursor = conn.cursor()

        # Telefon modelleri ve geçiş sayısı bilgisini tutacak tabloyu oluştur
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS telefonlar (
                barkod TEXT PRIMARY KEY,
                model TEXT,
                tekrar INTEGER DEFAULT 0
            )
        ''')

        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("SQLite hatası:", e)

def telefonlari_kontrol_et_ve_kaydet():
    try:
        conn = sqlite3.connect('telefon_barkod.db')
        cursor = conn.cursor()

        # Veritabanında herhangi bir telefon kaydı var mı kontrol et
        cursor.execute("SELECT COUNT(*) FROM telefonlar")
        kayit_sayisi = cursor.fetchone()[0]

        if kayit_sayisi == 0:
            # Veritabanında hiç telefon kaydı yoksa, telefonları kaydet
            for model in telefon_modelleri:
                rastgele_id = ''.join(random.choice('0123456789') for _ in range(10))
                cursor.execute("INSERT INTO telefonlar (barkod, model) VALUES (?, ?)", (rastgele_id, model))

            conn.commit()
            print("Telefonlar başarıyla kaydedildi.")
        else:
            print("Telefonlar zaten kayıtlı.")

        conn.close()
    except sqlite3.Error as e:
        print("SQLite hatası:", e)

def telefon_gecildi(barkod):
    try:
        conn = sqlite3.connect('telefon_barkod.db')
        cursor = conn.cursor()

        # Telefonun mevcut "tekrar" değerini al
        cursor.execute("SELECT tekrar FROM telefonlar WHERE barkod=?", (barkod,))
        tekrar = cursor.fetchone()

        if tekrar is None:
            # Barkod veritabanında bulunamadı, hata mesajı ver
            print("Barkod veritabanında bulunamadı.")
        else:
            # "tekrar" değerini bir artır ve güncelle
            yeni_tekrar = tekrar[0] + 1
            cursor.execute("UPDATE telefonlar SET tekrar=? WHERE barkod=?", (yeni_tekrar, barkod))
            conn.commit()
            print(f"{barkod} barkodu geçildi. Yeni tekrar sayısı: {yeni_tekrar}")

        conn.close()
    except sqlite3.Error as e:
        print("SQLite hatası:", e)

def barkod_okut():
    barkod = barkod_entry.get().strip()
    if barkod:
        telefon_gecildi(barkod)
        guncelle_liste()

def telefonlari_getir():
    conn = sqlite3.connect('telefon_barkod.db')
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT model, barkod, tekrar FROM telefonlar")
            telefonlar = cursor.fetchall()
            conn.close()
            return telefonlar
        except sqlite3.Error as e:
            print("SQLite hatası:", e)
            return []

def guncelle_liste():
    telefon_listesi.delete(*telefon_listesi.get_children())
    telefonlar = telefonlari_getir()
    for telefon in telefonlar:
        telefon_listesi.insert("", "end", values=telefon)
    telefon_listesi.update()  # Görünümü güncelle

# Veritabanını oluştur veya telefonları kontrol et ve kaydet
veritabani_olustur()
telefonlari_kontrol_et_ve_kaydet()

# Tkinter penceresini oluştur
root = tk.Tk()
root.title("Telefon Barkod Programı")

# Pencere arka plan rengini siyah yap
root.configure(bg='black')

# Barkod girişi
barkod_label = ttk.Label(root, text="Barkodu Okutun:", background='black', foreground='white')
barkod_label.pack()

barkod_entry = ttk.Entry(root)
barkod_entry.pack()

okut_button = ttk.Button(root, text="Okut", command=barkod_okut)
okut_button.pack()

# Telefon listesi
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill="both", expand=True)

telefon_listesi = ttk.Treeview(frame, columns=("Model", "Barkod", "Tekrar"))
telefon_listesi.heading("Model", text="Model")
telefon_listesi.heading("Barkod", text="Barkod")
telefon_listesi.heading("Tekrar", text="Tekrar")

telefon_listesi.pack(fill="both", expand=True)

# Veritabanındaki telefonları görüntüle
guncelle_liste()

# Çıkış butonu
cikis_button = ttk.Button(root, text="Çıkış", command=root.quit)
cikis_button.pack(pady=10)

root.mainloop()
