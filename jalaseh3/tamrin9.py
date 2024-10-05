print("ltfan 2 list joda bdahid list bala ta payin jam mishavad :)")


jam = lambda vorodi1  , vorodi2: vorodi1 + vorodi2


if __name__ == "__main__":


    while True:
        try:
            list1 = list(map(int, input("adaad list aval ra ba faselh joda knid : ").split()))


            list2 = list(map(int, input("adad list dovm ra ba faselh joda knid : ").split()))
        except ValueError:
            print("lotfan adad vared knid")
            continue
        if len(list1) == len(list2):
            majmo = list(map(jam  , list1, list2))

            print(f"list jam = {majmo}")
        else:
            print("lotfan list ha ro andaze benvisid!")
            continue
            print("payan")