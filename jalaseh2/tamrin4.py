print("_-_-_" * 12)
print("hi :) agar mikhahi barnameh bh marhale bad bravad print kn (end)!!!")
print("_-_-_" * 12)

namvasile = {}


def kharid():


    while True:
        try:
            kala_ha = str(input("Kala khod ra vared konid : "))


            if kala_ha.lower() == "end":
                break
            else:
                hazineh = input("hazine Kala chaghadr ast? ")

                hazineh = int(hazineh)
        except ValueError:
            print("adad sahih vared kon!")
            continue
        if hazineh <= 0:
            print("hazine zir 0 nadarim!")
        else:
            if kala_ha in namvasile.keys():
                hazine_1 = namvasile.get(kala_ha) + hazineh
                namvasile.update({kala_ha: hazine_1})
            else:
                namvasile.update({kala_ha: hazineh})

    return namvasile

list_Kala = kharid()


def majmoo_hazineha():
    majmoo = 0
    for numbers in list_Kala.values():
        majmoo += numbers
    return majmoo


jam_kala = majmoo_hazineha()


def boodje():
    while True:
        try:
            boodje_karbar = int(input("Boodje shoma cheghadr ast?"))
            if boodje_karbar > 0:
                baghi_mande = boodje_karbar - jam_kala
                if 0 > baghi_mande:
                    print(f"Hazine kala ha : {jam_kala}")


                    print("Hazine kala ha Bishtar az Boodje shoma hast !")
                else:
                    print("shoma mitavanid pardakht konid. :)")



                    print(f"Hazine Kala ha ({jam_kala}) ast ,boodje shoma ({boodje_karbar}) ast ")


                    print(f"Hazine Baghi mandeh : {baghi_mande}")
            else:
                print("adad boodje zir 0 ast!")
                continue
            break
        except ValueError:
            print("adad sahih vared konid")
            continue
    return

boodje()