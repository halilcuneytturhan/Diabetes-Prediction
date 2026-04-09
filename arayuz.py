import tkinter as tk
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier 
from tkinter import messagebox
import os
import joblib



df = pd.read_csv(r"C:\Users\cavus\Desktop\jupyter\diabetes.csv")



model_dosyasi = "diyabet_modeli.pkl"

if(os.path.exists(model_dosyasi)):
    model = joblib.load(model_dosyasi)
    print("Eğitilmiş model dosyadan jet hızıyla yüklendi!")
    
else:
    print("Model ilk kez eğitiliyor... Bu biraz zaman alabilir...")
    df = pd.read_csv("diabetes.csv")
    
    cols = ["Glucose", "BMI", "BloodPressure", "Insulin", "SkinThickness"]
    df[cols] = df[cols].replace(0,np.nan)
    df.fillna(df.median(), inplace=True)

    X = df[['Glucose', 'BMI', 'Age', 'BloodPressure', 'Insulin', 'SkinThickness']]
    y = df['Outcome'] 


    model = RandomForestClassifier(n_estimators=295,random_state=42)
    model.fit(X,y)
    
    joblib.dump(model,model_dosyasi)

pencere = tk.Tk()

pencere.title("İlk app")
pencere.geometry("400x450")

baslik = tk.Label(pencere,text="Hasta Değerlerini giriniz.",font=("Helvetica",15,"bold"))
baslik.pack(pady=15)



def kutu_ekle(yazi):
    satir = tk.Frame(pencere)
    satir.pack(pady=5)
    
    tk.Label(satir,text=yazi,width=18,anchor="w",font=("Helvetica",10)).pack(side="left")
    kutu= tk.Entry(satir,font=("Helvetica",10))
    kutu.pack(side="right")
    
    return kutu



glikoze = kutu_ekle("Glikoz Seviyesi: ")
bmie = kutu_ekle("Vücut Kitle Endeksi: ")
yase = kutu_ekle("Yaş: ")
tansiyone = kutu_ekle("Tansiyon: ")
insuline = kutu_ekle("İnsulin Seviyesi: ")
cilte = kutu_ekle("Cilt Kalınlığı: ")


def teshis_koy():
    try:
        g = float(glikoze.get())
        b = float(bmie.get())
        y_yas = float(yase.get())
        t = float(tansiyone.get())
        i = float(insuline.get())
        c = float(cilte.get())
        
        hasta_degerleri = [[g,b,y_yas,t,i,c]]
        
        sonuc = model.predict(hasta_degerleri)
        
        if(sonuc[0] == 1):
            sonuc_yazisi.config(text="DİKKAT : Diyabet riski YÜKSEK!!!",fg="red")
        else:
            sonuc_yazisi.config(text="Diyabet seviyesi normal gözüküyor",fg="green")
            
        
    except ValueError:
        from tkinter import messagebox
        messagebox.showerror("Hata","Lütfen tüm kutucuklara sadece RAKAM giriniz!!!")
        

buton = tk.Button(pencere,text="Yapay Zekaya SOR",bg="LightBlue",font=("Helvetica",15,"bold"),command=teshis_koy)
buton.pack(pady=25)

sonuc_yazisi = tk.Label(pencere,text="Sonuç burada gözükecek",font=("Helvetica",13,"italic"))
sonuc_yazisi.pack(pady=15)

pencere.mainloop()

