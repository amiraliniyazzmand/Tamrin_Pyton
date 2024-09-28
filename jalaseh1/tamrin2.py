

import random
adad = random.randint(1,100)
while True:
    hads_adad = input(" yk adad az 1 ta 100 antkhab knid : ")
    try:
         hads_adad = int(hads_adad)
    except ValueError:
        print("adad sahih vard knid")
        continue
    if hads_adad < 1 or hads_adad >100:
        print("adad az 1 ta 100 bashad")
        continue
    if hads_adad == adad:
        print("afarin drst peyda kardi")
        break
    elif hads_adad <= adad:
        print("adad bishtar")
    elif hads_adad >= adad:
        print("adad km tar")