'''
sonlar = [44,57,,42,23,29,75,89,95,58,47] .Berilgan sonlarni kvadratlarini yig'indisini topuvchi rekursiv funksiya
yarating.Hosil bo'lgan natijani ekranga chiqaring.
'''
sonlar = [44,57,42,23,29,75,89,95,58,47]

def kvadratlar_yigindisi(sonlar):
    if not sonlar:
        return 0
    else:
        return sonlar[0]**2 + kvadratlar_yigindisi(sonlar[1:])

natija = kvadratlar_yigindisi(sonlar)
print(natija)
