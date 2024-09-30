print("agar benvisid 'next' be marhale bad")
namekala = {}
def kharidvasilh():
    while True:
        try:
            kala = str(input("Kala ye Morede nazar khod ra vared konid : "))
            if kala. lower() == "end":
                break
            hazinh = input("hazine Kala chaghadr ast? ")
            hazinh = int(hazinh)
        except ValueError:
            print("adad sahih vared kn")
            continue
        if kala in namekala.keys():
            hazine_1 = namekala.get(kala) + hazinh
            namekala.update({kala: hazine_1})
        else:
            namekala.update({kala: hazinh})
    return namekala
list_Kala = kharidvasilh()
def majmoo_hazine():
    majmoo = 0
    for numbers in list_Kala.values():
        majmoo += numbers
    return majmoo
jam_kala = majmoo_hazine()
def boodje():
    while True:
        boodjekarbar = input("Boodje shoma cheghadr ast?")
        try:
            boodjekarbar = int(boodjekarbar)
            break
        except ValueError:
            print("adad sahih vared kon!, dobare emtehan kon.")
            continue
    baghimande = boodjekarbar - jam_kala
    if 0 > baghimande:
        print(f"Hazine kala ha : {jam_kala}")
        print("Hazine kala ha Bishtar az Boodje shoma hast !")
    else:
        print("shma mitavanid kharid knid")
        print(f"Hazine Kala ha ({jam_kala}) ast ,boodje shma ({boodjekarbar}) ast ")
        print(f"Hazine Baghi mandeh:{baghimande}")
    return
boodje()