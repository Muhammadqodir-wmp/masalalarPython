'''
sonlar = [96,24,50,85,68,48,37,52,21,46] Berilgan sonlarni kamayish tartibida
saralang.Hosil bo'gan natijani ekranga chop etamiz.

 '''
# sonlar = [96,24,50,85,68,48,37,52,21,46]

def pufakcha(royxat):   
     olcham = len(royxat)

     for son in range(olcham-1):
         for yson in range(0, olcham-son-1):
             if royxat[yson] < royxat[yson+1]:
                 royxat[yson], royxat[yson+1] = royxat[yson+1], royxat[yson]
       
     return royxat

sonlar = [96,24,50,85,68,48,37,52,21,46]
print(pufakcha(sonlar))

