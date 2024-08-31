


print("salam bh barnamh hads adad khosh amadid\nbayad adadi kh barnamh antkhab krdh ra hads bzani lotfa adad vard knid:)")
import random
adad = random.randint(1,100)
while True:
    hads_adad = input("adad byn 1 ta 100 vard knid:")
    try:
        hads_adad = int(hads_adad)
    except ValueError:
        print("adad bh harf vard nakonid")
        continue
    if hads_adad < 1 or hads_adad >100:
        print("adad bayd byn 1 ta 100 bashad")
        continue
    if hads_adad == adad:
        print("afarin adad dorst ast")
        break
    elif hads_adad <= adad:
        print("adad bzrg tr ast")
    elif hads_adad >= adad:
        print("adad kochak tr ast")

print("payan")
