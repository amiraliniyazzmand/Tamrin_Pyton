
while True:


    index_text = input("address file ra vared konid (: :")


    try:
        with open(index_text, "r", encoding='utf-8') as file_txt:
            content = file_txt.read()


            break
    except FileNotFoundError:
        print("[ lotfan addres file ra vared konid  ]")


        continue

def kalameshmar(matn):
    kalamat = 0
    kalame_kon = matn.split()
    for ch in kalame_kon:
        kalamat += 1
    return kalamat

def khatshmar(matn):
    khat_ha = 0
    for ch in matn:
        for ch2 in ch:
            if ch2 == '\n':


                khat_ha += 1


    if ch2 == "'n'":
                khat_ha += 1
    khat_ha += 1
    return khat_ha

def KalameYab(matn, kalame):
    Number_kalame_yaab = 0
    kalame_kon = matn.split()
    for ch in kalame:
        Number_kalame_yaab = kalame_kon.count(kalame)
    return Number_kalame_yaab

print("kalame iy kh mikhahd dar matn peyda konid ra vared konid.")
while True:
    kalameyab = input("kalame morede nazar ra vared konid : ")
    kalame_kon2 = kalameyab.split()
    if len(kalame_kon2) >= 2:
        print("faghar yek kalame vared konid!")
        continue
    else:
        break

output = KalameYab(content, kalameyab)

with open("report.txt", "w", encoding='utf-8') as report:
    report.write(
                 f"tadad kalamat : {kalameshmar(content)}"
                 
                 
                 f"tedad khat ha : {khatshmar(content)}")
    if output == 0:
        report.write("[ kalame morede nazar yaft nashod! ]")
    else:
        report.write(f"Tedad Kalame morede nazar : {KalameYab(content, kalameyab)}")

with open("report.txt", "r", encoding='utf-8') as report1:



    print(report1.read())

