# '''
# sonlar = [44,57,,42,23,29,75,89,95,58,47] .Berilgan sonlarni kvadratlarini yig'indisini topuvchi rekursiv funksiya
# yarating.Hosil bo'lgan natijani ekranga chiqaring.
# '''
# # sonlar = [44,57,42,23,29,75,89,95,58,47]
# sonlar = [1, 2, 3]
# def kvadratlar_yigindisi(sonlar):
#     if not sonlar:
#         return 0
#     else:
#         return sonlar[0]**2 + kvadratlar_yigindisi(sonlar[1:])

# natija = kvadratlar_yigindisi(sonlar)
# print(natija)

class Tugun:
    def __init__(self, yangi_qiymat):
        self.qiymat = yangi_qiymat
        self.oldingi = None
        self.keyingi = None

class IkkiTomonlamaRoyhat:
    def __init__(self):
        self.bosh = None
        self.oxir = None

    def boshiga_qoshish(self, yangi_qiymat):
        yangi_tugun = Tugun(yangi_qiymat)
        if self.bosh is None:
            self.bosh = self.oxir = yangi_tugun
        else:
            yangi_tugun.keyingi = self.bosh
            self.bosh.oldingi = yangi_tugun
            self.bosh = yangi_tugun

    def oxiriga_qoshish(self, yangi_qiymat):
        yangi_tugun = Tugun(yangi_qiymat)
        if self.oxir is None:
            self.bosh = self.oxir = yangi_tugun
        else:
            yangi_tugun.oldingi = self.oxir
            self.oxir.keyingi = yangi_tugun
            self.oxir = yangi_tugun

    def royhatni_chop_etish(self):
        joriy = self.bosh
        while joriy is not None:
            print(joriy.qiymat, end=' <-> ')
            joriy = joriy.keyingi
        print()

# Sonlar massivini ikki tomonlama bog'langan ro'yhatga o'tkazish
sonlar = [35, 41, 27, 52, 34, 94, 92, 47, 3, 98]
royhat = IkkiTomonlamaRoyhat()

for son in sonlar:
    royhat.oxiriga_qoshish(son)

# Ro'yhatni ekranga chiqarish
royhat.royhatni_chop_etish()

# Kiritilgan massiv
sonlar2 = [35, 41, 27, 52, 34, 94, 92, 47, 3, 98]

# Node sinfi - bog'langan ro'yhatning tuguni
class Node:
    def __init__(self, data):
        self.data = data  # Tugunning qiymati
        self.next = None  # Keyingi tugunga ko'rsatma

# LinkedList sinfi - bog'langan ro'yhat
class LinkedList:
    def __init__(self):
        self.head = None  # Bog'langan ro'yhatning boshlang'ich tuguni

    # Ro'yhatning oxiriga yangi tugun qo'shish funksiyasi
    def append(self, data):
        new_node = Node(data)  # Yangi tugun yaratish
        if not self.head:  # Agar ro'yhat bo'sh bo'lsa
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  # Oxirgi tugunni topish
            last_node = last_node.next
        last_node.next = new_node  # Yangi tugunni oxiriga qo'shish

    # Ro'yhatdagi elementlarni chiqarish funksiyasi
    def display(self):
        current_node = self.head
        while current_node:  # Hammasini chiqarish
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Bog'langan ro'yhatni yaratish
ll = LinkedList()

# Massiv elementlarini bog'langan ro'yhatga qo'shish
for son in sonlar2:
    ll.append(son)

# Ro'yhatni ko'rsatish
ll.display()
