import tkinter as tk
from tkinter import *
from tkinter import messagebox
import instaloader


instagram = instaloader.Instaloader()


def böl3():
    try:
        profil = instaloader.Profile.from_username(instagram.context,tarama.get())
        takipciler = profil.get_followers()
        takipcilerListesi = list()
        takipEdilenlerListesi = list()
        dosya = open("C:\\Users\\ADMİN\\Desktop\\GtYapmayanlar.txt", "a")
        dosya.writelines("Taranan kullanıcı:" + profil.username + "\n")
        dosya.close()
        for i in takipciler:
            takipcilerListesi.append(i.username)

        takipEdilenler = profil.get_followees()

        for i in takipEdilenler:
            takipEdilenlerListesi.append(i.username)

        for i in takipEdilenlerListesi:
            if i not in takipcilerListesi:
                dosya = open("C:\\Users\\ADMİN\\Desktop\\GtYapmayanlar.txt", "a")
                dosya.writelines(i + "  Geri takip etmiyor..." + "\n")
                dosya.close()

        messagebox.showinfo("Gt Bot", "İşlem Tamamlandı")
    except:
        messagebox.showwarning("Gt Bot", "Bir Hata Oluştu İşlemlerinizi Gözden Geçiriniz")

def Giris():
    try:
        Ad = kulad.get()
        sifree = sifre.get()
        instagram.login(Ad, sifree)
        fs = tk.Button(text="Tara", bg="black", fg="white", command=böl3)
        fs.place(x="120", y="320")
        print("Tamam")
    except:
        messagebox.showerror("Gt Bot", "Hatalı Şifre Veya Kullanıcı Adı")

pen = tk.Tk()
pen.title("Gt Kontrol")
pen.geometry("350x570+500+100")
pen.resizable(width=False, height=False)

Botbaslik = tk.Label(text="İnstagram Gt Kontrol", font="Verdana 21 bold").pack()

img = PhotoImage(file="insta.png")
img = img.subsample(2,2)

insta = tk.Label(image=img).pack()

kulad = tk.Entry()
kulad.pack()

sifre = tk.Entry(show="*")
sifre.pack()

giris = tk.Button(text="Giris" ,command=Giris).pack()

tarama = tk.Entry()
tarama.pack()


pen.mainloop()