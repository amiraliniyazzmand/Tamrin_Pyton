print("agar mikhahi tavan nshan dahad print kn (tavan)")
try:
    list_adad = []
    tavan= lambda adad : adad ** 2
    while True :
        adad = input("adad hayy kh makhahi bh tvan 2 briseh bnvis :")
        if  adad == "tavan":
            break


        else:
            adad= int(adad)

            list_adad.append(adad)

            tavan(adad)
            payani = map (tavan,list_adad)
        payani=list(payani)
    print(f"avab tavan 2: {payani}")
except ValueError :
    print("adad sahih vard konid")
