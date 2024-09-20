# '''
# Python dasturlash tilida “Ikkiga bo’lib qidirish” algoritmi juda samarali va tez ishlaydi.
#  Bu algoritmi quyidagi tarzda tushuntirish mumkin:

# Ro’yxatni o’rtasidan boshlab, qidirayotgan element bilan solishtiriladi.
# Agar element ro’yxatning o’rtasidagi elementdan kichik bo’lsa, qidiruv jarayoni ro’yxatning chap tomonida davom etadi.
# Agar element ro’yxatning o’rtasidagi elementdan katta bo’lsa, qidiruv jarayoni ro’yxatning o’ng tomonida davom etadi.
# Bu jarayon element topilganicha yoki qidiruv maydoni bo’sh qolganicha takrorlanadi.


# #Ro'yxat tartiblangan bo'lishi kerak!
# '''

# def qidirish(royxat, qidiruv_elementi):
#     boshlangich_indeks = 0
#     oxirgi_indeks = len(royxat) - 1

#     while boshlangich_indeks <= oxirgi_indeks:
#         orta_indeks = (boshlangich_indeks + oxirgi_indeks) // 2
#         orta_element = royxat[orta_indeks]

#         if orta_element == qidiruv_elementi:
#             return orta_indeks
#         elif orta_element < qidiruv_elementi:
#             boshlangich_indeks = orta_indeks + 1
#         else:
#             oxirgi_indeks = orta_indeks - 1

#     return None

# royxat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# son = 7

# natija = qidirish(royxat, son)

# if natija is not None:
#     print(f"Ushbu son: {son} \nro'yxatning {natija}-indeksida joylashgan.")
# else:
#     print("Bunday element ro'yxatda mavjud emas.")

#     '''
    
    
#     '''
# def chiziqli_qidiruv(royxat, element):
#     """
#     Berilgan ro'yxatda elementni qidiruv algoritmi.
    
#     Args:
#         ro'yxat (list): Qidiruvni amalga oshirish uchun ro'yxat.
#         element: Qidiriladigan element.
    
#     Returns:
#         int: Element indeksi (agar topilsa), aks holda -1.
#     """
#     for indeks in range(len(royxat)):
#         if royxat[indeks] == element:
#             return indeks
#     return -1

# # Misol
# mehmonlar = ["Ali", "Vali", "Hasan", "Husan", "Olim"]
# qidiriladigan_mehmon = "Hasan"
# natija = chiziqli_qidiruv(mehmonlar, qidiriladigan_mehmon)
# if natija != -1:
#     print(f"{qidiriladigan_mehmon} ro'yxatda {natija} indeksda.")
# else:
#     print(f"{qidiriladigan_mehmon} ro'yxatda topilmadi.")



def pufakcha(self, royxat):
        n = len(royxat)
        for i in range(n):
            # Elementlar almashishi sodir bo'ladigan ichki aylanish
            for j in range(0, n-i-1):
                # Agar qo'shni elementlar noto'g'ri tartibda bo'lsa, ularni almashtiramiz
                if royxat[j] > royxat[j+1]:
                    oraliq = royxat[j]
                    royxat[j] = royxat[j+1]
                    royxat[j+1] = oraliq

# Misol:

