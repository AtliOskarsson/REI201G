#S4

# Verkefni 12
def shellrodun(listi):
    n = len(listi)
    bil = n // 2

    while bil > 0:
        bendill = 0
        while bendill+bil < n:
            # 
            if listi[bendill+bil] < listi[bendill]:
                temp = listi[bendill]
                listi[bendill] = listi[bendill+bil]
                listi[bendill+bil] = temp
            bendill += 1
        bil = bil // 2


listi2 = [12, 34, 54, 2, 3, 5, 7, 13, 51]
print("input array:",listi2)
  
shellrodun(listi2)
print("sorted array",listi2)