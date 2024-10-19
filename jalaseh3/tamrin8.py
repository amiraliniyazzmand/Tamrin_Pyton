listtapel=[]

while True:
    adadtapel=input("mghdar tapel khod ra varid kond :")
    try:
        adadtapel = int(adadtapel)
        if adadtapel <= 0 :
            print("adad bishtar az 0 bashad ;)")
            continue
        break
    except ValueError:
        print("adad vard konid!!!!!!!!!!!!!!!")
        continue
for ch in range(adadtapel):

    while True :
        tapel_ha=input("tapel ra vard konid ba faslh :")

        tapellist=tapel_ha.split()


        if len(tapellist)< 2:
            print("bayad  2  bashad !!!!!!!")
            continue

        elif len(tapellist) > 2 :
            print("az 2 ozv nbayd bish tar bshh")
        else:
            tapel=tuple(tapellist)
            listtapel.append(tapel[1])
    print("list azae 2 hr tapel",listtapel)
