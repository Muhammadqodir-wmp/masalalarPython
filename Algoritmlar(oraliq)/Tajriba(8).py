'''                     Tajriba(8).py               
       sonlar =[77,24,35,74,65,13,67,8,11,40]. Berilgan sonlardan binar daraxt yarating.
       Hosil bo'lgan natijani ekranga chop eting.     
                            '''


sonlar = [77, 24, 35, 74, 65, 13, 67, 8, 11, 40]

class Tugun:
    def __init__(self, kalit):
        self.ong = None
        self.chap = None
        self.qiymat = kalit

def kiritmoq(ildiz, kalit):
    if ildiz is None:
        return Tugun(kalit)
    else:
        if ildiz.qiymat < kalit:
            ildiz.ong = kiritmoq(ildiz.ong, kalit)
        else:
            ildiz.chap = kiritmoq(ildiz.chap, kalit)
    return ildiz

def otkazish(ildiz):
    if ildiz:
        otkazish(ildiz.chap)
        print(ildiz.qiymat, end=" ")
        otkazish(ildiz.ong)

ildiz = None
for son in sonlar:
    ildiz = kiritmoq(ildiz, son)

print("\nHosil bo'lgan daraxt (inorder traversalda):")
otkazish(ildiz)