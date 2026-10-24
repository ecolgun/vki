import time

kilo=float(input("kilonuzu girin"))
boy=float(input("boyunuzu girin(metre cinsinden)"))
vki=kilo/(boy*boy)
print("Hesaplanıyor lütfen bekleyiniz")
time.sleep(2)
print("vücut kütle indeksiniz",vki)

if vki<=18.5:
    print("zayıfsınız")
elif 18.5<vki<=24.9:
    print("normalsiniz")
elif 24.9<vki<=29.9:
    print("fazla kilolusunuz")
elif 29.9<vki<=35:
    print("1.derece obezite")
elif 35<vki<=40:
    print("2.derece obezite")
elif 40<vki<=50:
    print("3.derece obezite")
else:
    print("Süper Obezite")