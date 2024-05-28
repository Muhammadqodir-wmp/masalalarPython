class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)  # Yangi tugun yaratish
        if self.head is None:  # Agar bog'langan ro'yxat bo'sh bo'lsa
            self.head = new_node  # Yangi tugunni ro'yxatning boshi (head) qilamiz
            return
        last = self.head  # Bo'sh bo'lmasa, boshidan boshlaymiz
        while last.next:  # Oxirgi tugungacha boramiz
            last = last.next  # Keyingi tugunga o'tamiz
        last.next = new_node  # Oxirgi tugunning keyingi elementi yangi tugun bo'ladi

    def display(self):
        current = self.head  # Ro'yxatning boshidan boshlaymiz
        while current:  # Ro'yxatning oxiriga yetguncha davom etamiz
            print(current.data, end=" -> ")  # Joriy tugun ma'lumotini chiqaramiz
            current = current.next  # Keyingi tugunga o'tamiz
        print("Tugadi")  # Ro'yxat oxiri

# Berilgan sonlar
sonlar = [54, 22, 86, 6, 72, 3, 31, 97, 56, 92]

# Bog'langan ro'yxat yaratish
linked_list = LinkedList()

# Bog'langan ro'yxatga sonlarni qo'shish
for son in sonlar:  # sonlar ro'yxatidagi har bir son uchun
    linked_list.append(son)  # append funksiyasi orqali bog'langan ro'yxatga qo'shamiz

# Foydalanuvchi tomonidan kiritilgan sonni qo'shish
foydalanuvchi_soni = int(input("Yangi son kiriting: "))
linked_list.append(foydalanuvchi_soni)  # Yangi sonni ham ro'yxatga qo'shamiz

# Natijani ekranga chiqarish
linked_list.display()  # Bog'langan ro'yxatni ekranga chiqarish
