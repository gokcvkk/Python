import tkinter as tk
from tkinter import messagebox

# Hesap makinesi fonksiyonları
def toplama():
    try:
        result = float(entry1.get()) + float(entry2.get())
        label_sonuc.config(text=f"Sonuç: {result}")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayılar girin.")

def cikarma():
    try:
        result = float(entry1.get()) - float(entry2.get())
        label_sonuc.config(text=f"Sonuç: {result}")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayılar girin.")

def carpma():
    try:
        result = float(entry1.get()) * float(entry2.get())
        label_sonuc.config(text=f"Sonuç: {result}")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayılar girin.")

def bolme():
    try:
        if float(entry2.get()) == 0:
            messagebox.showerror("Hata", "Bir sayıyı sıfıra bölemezsiniz.")
        else:
            result = float(entry1.get()) / float(entry2.get())
            label_sonuc.config(text=f"Sonuç: {result}")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayılar girin.")

# Ana pencere
root = tk.Tk()
root.title("Hesap Makinesi")

# Girdiler için etiketler ve giriş kutuları
label1 = tk.Label(root, text="Birinci Sayı:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="İkinci Sayı:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# İşlem butonları
button_topla = tk.Button(root, text="Toplama", command=toplama)
button_topla.grid(row=2, column=0)

button_cikar = tk.Button(root, text="Çıkarma", command=cikarma)
button_cikar.grid(row=2, column=1)

button_carp = tk.Button(root, text="Çarpma", command=carpma)
button_carp.grid(row=3, column=0)

button_bol = tk.Button(root, text="Bölme", command=bolme)
button_bol.grid(row=3, column=1)

# Sonuç etiketi
label_sonuc = tk.Label(root, text="Sonuç:")
label_sonuc.grid(row=4, column=0, columnspan=2)

# Ana döngü
root.mainloop()
