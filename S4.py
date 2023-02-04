from urllib.request import urlopen

#S4

# Verkefni 12
def shellRodun(listi):
    n = len(listi)
    bil = n // 2

    while bil > 0:
        bendill = 0

        while bendill + bil < n:
            # 
            if listi[bendill + bil] < listi[bendill]:
                temp = listi[bendill]
                listi[bendill] = listi[bendill + bil]
                listi[bendill + bil] = temp

            bendill += 1
        bil = bil // 2

listi1 = [8,3,2]
listi2 = [8,5,1,9,6,2,1,7,11,3]
listi3 = [256, 321, 286, 85, 188, 183, 409, 247, 87, 206, 33, 239]

print("Fyrir:", listi1)
shellRodun(listi1)
print("Eftir:", listi1)

print("Fyrir:", listi2)
shellRodun(listi2)
print("Eftir:", listi2)

print("Fyrir:", listi3)
shellRodun(listi3)
print("Eftir:", listi3)
#------------------------------------------------------------#

#Verkefni 13
#Liður 1
def islenskOrd(url):
    f = urlopen(url)
    ordin = []
    for line in f:
        ord = line.decode().strip()
        ordin.append(ord)
    return ordin

#Liður 2
def spegilord(s):
    s = s.lower()
    speglad = s[::-1]

    if s == speglad: return True
    else: return False

allt = islenskOrd("https://cs.hi.is/python/ord.txt")

for i in range(len(allt)):
    ord = allt[i]
    if i < 5:
        print(ord)
    elif len(ord) >= 30:
        print(ord)
    elif i % 10000 == 0:
        print(ord)

teljari = 1
for ord in allt:
    if spegilord(ord):
        if teljari % 10 == 0:
            print(ord)
        else:
            print(ord, end=", ")
    teljari += 1

#Liður 3
def margirSerhljodar(ord):
    serhljodar = ["a","á", "e", "é", "i", "í", "o", "ó", "u", "ú",
    "y", "ý", "æ", "ö"]
    serhljodarAuka = ["ei", "ey", "au"]
    teljari = 0

    for i in range(len(ord)):
        stafur = ord[i]
        if (stafur == "a" or stafur == "e") and i < (len(ord) - 1):
            temp = stafur + ord[i+1]
            if temp in serhljodar:
                teljari += 1
                i += 1        
            else:
                teljari += 1

        elif stafur in serhljodar:
            teljari += 1
    return teljari

hamarkSam = 0
seinasti = ""
serSam = []
for ord in allt:
    if len(ord) >= len(seinasti):
        for stafur in range(len(ord)):
            if margirSerhljodar(ord) > 1:
                break
            elif hamarkSam < (len(ord) - 1):
                serSam = []
                serSam.append(ord)
                hamarkSam = len(ord)
            elif hamarkSam == (len(ord) - 1):
                serSam.append(ord)

print(serSam)

#------------------------------------------------------------#

#Verkefni 15