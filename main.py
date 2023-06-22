import tkinter

#pencere
window = tkinter.Tk()
window.title("Vücut Kitle Endeksi Hesaplama")
window.minsize(width=500, height=400)


#başlık
label_baslik = tkinter.Label(text="Vücut kitle endeksini hesaplamak için boy (m) ve kilonuzu (kg) yazınız.")
label_baslik.place(x=0, y=0)

#labels
label_boy = tkinter.Label(text="Boy :")
label_boy.place(x=0, y=20)

label_kg = tkinter.Label(text="Kilo :")
label_kg.place(x=0, y=40)

label_endeks = tkinter.Label(text="endeks :")
label_endeks.place(x=0, y=95)

label_sonuc = tkinter.Label(text="sonuç :")
label_sonuc.place(x=0, y=115)

#entrys
entry_boy = tkinter.Entry()
entry_boy.place(x=60, y=20)

entry_kg = tkinter.Entry()
entry_kg.place(x=60, y=40)

entry_endeks = tkinter.Entry()
entry_endeks.place(x=60, y=95)

entry_sonuc = tkinter.Entry()
entry_sonuc.place(x=60, y=115)

#buton
#hesaplama fonksiyonu
def endeks_hesabı():
    try:
        kg = float(entry_kg.get())
        boy = float(entry_boy.get())
    except ValueError:
        entry_sonuc.delete(0, 100)
        entry_sonuc.insert(0, "LÜTFEN SAYI GİRİN")
    endeks_degeri = kg / boy**2
    print(endeks_degeri)
    entry_endeks.delete(0, 100)
    entry_endeks.insert(0, endeks_degeri)
    if endeks_degeri < 18.5:
        entry_sonuc.delete(0, 100)
        entry_sonuc.insert(0, "zayıf")
    if 18.5 < endeks_degeri < 24.9:
        entry_sonuc.delete(0, 100)
        entry_sonuc.insert(0, "normal")
    if 25 < endeks_degeri <29.9:
        entry_sonuc.delete(0, 100)
        entry_sonuc.insert(0, "kilolu")
    if 30 < endeks_degeri < 34.9:
        entry_sonuc.delete(0, 100)
        entry_sonuc.insert(0, "obez")
    if 35 < endeks_degeri:
        entry_sonuc.delete(0, 100)
        entry_sonuc.insert(0, "aşırı obez")


buton = tkinter.Button(text="Hesapla", command=endeks_hesabı)
buton.place(x=60, y=64)


window.mainloop()