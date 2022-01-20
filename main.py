inputN = input("عدد مورد نظر را وارد کنید: ")
result = ""

if "-" in inputN:
    inputN = inputN.replace("-", "")
    result += "منفی "
elif "+" in inputN:
    inputN = inputN.replace("+", "")

inputN = inputN.zfill(61)
intN = int(inputN)

if intN > 10**61:
    print("خطا: عدد مورد نظر شما خارج از محدوده مشخص شده برای این برنامه میباشد.")
    quit()

yekan = ["", "یک", "دو", "سه", "چهار", "پنج", "شش", "هفت", "هشت", "نه"]
dahha = ["ده", "یازده", "دوازده", "سیزده", "چهارده", "پانزده", "شانزده", "هفده", "هجده", "نوزده"]
tabist = yekan + dahha
dahgan = ["", "ده", "بیست", "سی", "چهل", "پنجاه", "شصت", "هفتاد", "هشتاد", "نود"]
sadgan = ["", "صد", "دویست", "سیصد", "چهارصد", "پانصد", "ششصد", "هفتصد", "هشتصد", "نهصد"]
adadbozorg = {3: "هزار", 6: "میلیون", 9: "میلیارد", 12: "تریلیون",
              15: "کوآدریلیون", 18: "کوینتیلیون", 21: "سکستیلیون", 24: "سپتیلیون",
              27: "اکتیلیون", 30: "نانیلیون", 33: "دسیلیون", 36: "آندسیلیون",
              39: "دیودسیلیون", 42: "تریدسیلیون", 45: "کواتیوردسیلیون", 48: "کویندسیلیون",
              51: "سکسدسیلیون", 54: "سپتدسیلیون", 57: "اکتودسیلیون", 60: "نومدسیلیون"}

va = " و "
space = " "
empty = ""

listN = []
for i in inputN:
    listN.append(i)

def tahezar(number):
    if number > 0 and number < 10:
        return yekan[number]
    elif number % 10 == 0 and number < 100:
        return dahgan[number//10]
    elif number > 10 and number < 20:
        return dahha[number-10]
    elif number > 20 and number < 100:
        dahganNumberTahezar, yekanNumberTahezar = divmod(number, 10)
        word = str(dahgan[dahganNumberTahezar]) + \
            va + str(yekan[yekanNumberTahezar])
        return word
    elif number % 100 == 0 and number < 1000:
        return sadgan[number//100]
    elif number > 100 and number < 120:
        word = sadgan[1] + va + tabist[number-100]
        return word
    elif number >= 120 and number < 200 and (number-100) % 10 == 0:
        word = sadgan[1] + va + dahgan[(number - 100)//10]
        return word
    elif number > 200 and number < 220:
        word = sadgan[2] + va + tabist[number - 200]
        return word
    elif number >= 220 and number < 300 and (number - 200) % 10 == 0:
        word = sadgan[2] + va + dahgan[(number - 200) // 10]
        return word
    elif number > 300 and number < 320:
        word = sadgan[3] + va + tabist[number - 300]
        return word
    elif number >= 320 and number < 400 and (number - 300) % 10 == 0:
        word = sadgan[3] + va + dahgan[(number - 300) // 10]
        return word
    elif number > 400 and number < 420:
        word = sadgan[4] + va + tabist[number - 400]
        return word
    elif number >= 420 and number < 500 and (number - 400) % 10 == 0:
        word = sadgan[4] + va + dahgan[(number - 400) // 10]
        return word
    elif number > 500 and number < 520:
        word = sadgan[5] + va + tabist[number - 500]
        return word
    elif number >= 520 and number < 600 and (number - 500) % 10 == 0:
        word = sadgan[5] + va + dahgan[(number - 500) // 10]
        return word
    elif number > 600 and number < 620:
        word = sadgan[6] + va + tabist[number - 600]
        return word
    elif number >= 620 and number < 700 and (number - 600) % 10 == 0:
        word = sadgan[6] + va + dahgan[(number - 600) // 10]
        return word
    elif number > 700 and number < 720:
        word = sadgan[7] + va + tabist[number - 700]
        return word
    elif number >= 720 and number < 800 and (number - 700) % 10 == 0:
        word = sadgan[7] + va + dahgan[(number - 700) // 10]
        return word
    elif number > 800 and number < 820:
        word = sadgan[8] + va + tabist[number - 800]
        return word
    elif number >= 820 and number < 900 and (number - 800) % 10 == 0:
        word = sadgan[8] + va + dahgan[(number - 800) // 10]
        return word
    elif number > 900 and number < 920:
        word = sadgan[9] + va + tabist[number - 900]
        return word
    elif number >= 920 and number < 1000 and (number - 900) % 10 == 0:
        word = sadgan[9] + va + dahgan[(number - 900) // 10]
        return word
    else:
        sadganTahezar = number//100
        dahganTahezar = (number-sadganTahezar*100)//10
        yekanTahezar = (number-sadganTahezar*100-dahganTahezar*10)
        word = sadgan[sadganTahezar] + va + \
            dahgan[dahganTahezar] + va + yekan[yekanTahezar]
        return word

tahezarN = listN[58:]
hezarN = listN[55:58]
millionN = listN[52:55]
milliardN = listN[49:52]
trillionN = listN[46:49]
quadrillionN = listN[43:46]
quintillionN = listN[40:43]
sextillionN = listN[37:40]
septillionN = listN[34:37]
octillionN = listN[31:34]
nonillionN = listN[28:31]
decillionN = listN[25:28]
undecillionN = listN[22:25]
duodecillionN = listN[19:22]
tredecillion = listN[16:19]
quattuordecillonN = listN[13:16]
quindecillionN = listN[10:13]
sexdecillionN = listN[7:10]
septendecillionN = listN[4:7]
octodecillionN = listN[1:4]
novemdN = listN[0]

tahezarNs, tahezarNi = tahezar(int(empty.join(tahezarN))), int(empty.join(tahezarN))
hezarNs, hezarNi = tahezar(int(empty.join(hezarN))), int(empty.join(hezarN))
millionNs, millionNi = tahezar(int(empty.join(millionN))), int(empty.join(millionN))
milliardNs, milliardNi = tahezar(int(empty.join(milliardN))), int(empty.join(milliardN))
trillionNs, trillionNi = tahezar(int(empty.join(trillionN))), int(empty.join(trillionN))
quadrillionNs, quadrillionNi = tahezar(int(empty.join(quadrillionN))), int(empty.join(quadrillionN))
quintillionNs, quintillionNi = tahezar(int(empty.join(quintillionN))), int(empty.join(quintillionN))
sextillionNs, sextillionNi = tahezar(int(empty.join(sextillionN))), int(empty.join(sextillionN))
septillionNs, septillionNi = tahezar(int(empty.join(septillionN))), int(empty.join(septillionN))
octillionNs, octillionNi = tahezar(int(empty.join(octillionN))), int(empty.join(octillionN))
nonillionNs, nonillionNi = tahezar(int(empty.join(nonillionN))), int(empty.join(nonillionN))
decillionNs, decillionNi = tahezar(int(empty.join(decillionN))), int(empty.join(decillionN))
undecillionNs, undecillionNi = tahezar(int(empty.join(undecillionN))), int(empty.join(undecillionN))
duodecillionNs, duodecillionNi = tahezar(int(empty.join(duodecillionN))), int(empty.join(duodecillionN))
tredecillionNs, tredecillionNi = tahezar(int(empty.join(tredecillion))), int(empty.join(tredecillion))
quattuordecillionNs, quattuordecillionNi = tahezar(int(empty.join(quattuordecillonN))), int(empty.join(quattuordecillonN))
quindecillionNs, quindecillionNi = tahezar(int(empty.join(quindecillionN))), int(empty.join(quindecillionN))
sexdecillionNs, sexdecillionNi = tahezar(int(empty.join(sexdecillionN))), int(empty.join(sexdecillionN))
septendecillonNs, septendecillonNi = tahezar(int(empty.join(septendecillionN))), int(empty.join(septendecillionN))
octodecillionNs, octodecillionNi = tahezar(int(empty.join(octodecillionN))), int(empty.join(octodecillionN))
novemdNs, novemdNi = yekan[int(empty.join(novemdN))], int(empty.join(novemdN))

if intN == 0:
    result = "صفر"

if novemdNi > 0:
    result += novemdNs + space + adadbozorg[60]
    if intN % (10**60) != 0:
        result += va

if octodecillionNi > 0:
    result += octodecillionNs + space + adadbozorg[57]
    if intN % (10**57) != 0:
        result += va

if septendecillonNi > 0:
    result += septendecillonNs + space + adadbozorg[54]
    if intN % (10**54) != 0:
        result += va

if sexdecillionNi > 0:
    result += sexdecillionNs + space + adadbozorg[51]
    if intN % (10**51) != 0:
        result += va

if quindecillionNi > 0:
    result += quindecillionNs + space + adadbozorg[48]
    if intN % (10**48) != 0:
        result += va

if quattuordecillionNi > 0:
    result += quattuordecillionNs + space + adadbozorg[45]
    if intN % (10**45) != 0:
        result += va

if tredecillionNi > 0:
    result += tredecillionNs + space + adadbozorg[42]
    if intN % (10**42) != 0:
        result += va

if duodecillionNi > 0:
    result += duodecillionNs + space + adadbozorg[39]
    if intN % (10**39) != 0:
        result += va

if undecillionNi > 0:
    result += undecillionNs + space + adadbozorg[36]
    if intN % (10**36) != 0:
        result += va

if decillionNi > 0:
    result += decillionNs + space + adadbozorg[33]
    if intN % (10**33) != 0:
        result += va

if nonillionNi > 0:
    result += nonillionNs + space + adadbozorg[30]
    if intN % (10**30) != 0:
        result += va

if octillionNi > 0:
    result += octillionNs + space + adadbozorg[27]
    if intN % (10**27) != 0:
        result += va

if septillionNi > 0:
    result += septillionNs + space + adadbozorg[24]
    if intN % (10**24) != 0:
        result += va

if sextillionNi > 0:
    result += sextillionNs + space + adadbozorg[21]
    if intN % (10**21) != 0:
        result += va

if quintillionNi > 0:
    result += quintillionNs + space + adadbozorg[18]
    if intN % (10**18) != 0:
        result += va

if quadrillionNi > 0:
    result += quadrillionNs + space + adadbozorg[15]
    if intN % (10**15) != 0:
        result += va

if trillionNi > 0:
    result += trillionNs + space + adadbozorg[12]
    if intN % (10**12) != 0:
        result += va

if milliardNi > 0:
    result += milliardNs + space + adadbozorg[9]
    if intN % (10**9) != 0:
        result += va

if millionNi > 0:
    result += millionNs + space + adadbozorg[6]
    if intN % (10**6) != 0:
        result += va

if hezarNi > 0:
    result += hezarNs + space + adadbozorg[3]
    if intN % (10**3) != 0:
        result += va

if tahezarNi > 0:
    result += tahezarNs

print(result)

# https://github.com/shahnazi2002
# December 3, 2021