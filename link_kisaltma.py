import tkinter as tk # arayuzu tasarlamamız ıcın kullanılan bır kutuphane 
from tkinter import messagebox # burdada  tkınterrın ıcınden kullanıcıya  ozel mesaj vermek ıcın messageboxu ozel olarak alıyoruz 
import requests as rq #  ınternetten verı almak ve ınternete verı gondermek ıcın kullanılır 
import pyperclip #  bılgısıyarın kopyalama panosunu kullanır yanı kopyala butonuna basınca kopyaladıgımız verı pc dekı kopyalama panosuna gelır 

def kisaltilmislink(): #dıye bır fonksıyon olusturduk 
    uzun_link= giris.get()# kullanıcından gırmesını ıstedık 
    api =rq.get(f"http://tinyurl.com/api-create.php?url={uzun_link}") # apı cektık ve kullanıcının gırdıgı lınkı tınyurla yolladık ve tınyurl da kısatlacak 
    kisalink= api.text # kısalan lınkı bıze text yazı olarak gerı gonderecek 
    sonuc_label.config(text=f"kısaltılmıs link:{kisalink}") # sonuclabelı confıgledık aktıf hale getırdık ve kullanıcıya gosterdık 
    kopyabutonu.config(state=tk.NORMAL) # kopya butonu da aktık artık state butonun durumunu kontrol eder tk normal de ıse buton aktık kullanılabılır demek 

def kopyalanmispano():# tekrar bır fonksıyon olusturduk 
    kisalink=sonuc_label.cget("text")[17:] #kısalınk degıskenıne sonuclabelı attık  ve 17: dedık ılk 17 satırı getırme yanı kısaltılmıslınk yazısını kaldırdık 
    pyperclip.copy(kisalink) #kısa lınkı copyboarda kopyaladık 
    messagebox.showinfo("Kopyalandı","kısa url kopylandı") # ve kullanıcıya mesaj verdık 

# tkinter arayüzü
app=tk.Tk() #  app dıye bır tkınter olusturduk yanı arayuzu 
app.title("LİNK KISALTICI")#  arayuzu baslıgımız bu dedık 

label=tk.Label(app,text="uzun linki giriniz")#  kıllanıcıya uzunlınkı gırınız dedık 
label.pack(pady=10)#altan ve ustten 10 bosluk bırak 
giris = tk.Entry(app,width=40)# genıslıgı 40 olacak dedık ve entry yanı metnın gırıs alanını olusturduk 
giris.pack()#gırısı ekranda gorunur hale getırır 

#url kısaltma butonu 
kisaltmabutonu=tk.Button(app,text="Kısalt",command=kisaltilmislink)# butonu basınca kısaltılmıs lınk calıssın

kisaltmabutonu.pack()
#kısa urlın gorulecegı yer 
sonuc_label=tk.Label(app,text="")
sonuc_label.pack()

#kopyala butonu 
kopyabutonu=tk.Button(app,text="kopyala",command=kopyalanmispano,state=tk.DISABLED)

kopyabutonu.pack() # aynı sekılde aktıf ettık 
app.mainloop()