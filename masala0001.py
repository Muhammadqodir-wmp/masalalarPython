def is_leap(yil):
    if yil % 4 == 0:
        if yil % 100 == 0 and  yil % 400 == 0 :           
            return True
        elif yil % 4 == 0 and yil % 100!=0:
            return True
        else:
            return False
    else:
        return False


year = int(input())
print(is_leap(year))