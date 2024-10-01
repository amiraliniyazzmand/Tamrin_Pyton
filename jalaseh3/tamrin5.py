print("salam dr ainja ak rabth riazi dr list ast adad ba adad badi jam misheh adad svm(3) ra misazd:)")



def fibonachi(adad):
    if adad == 1 or adad == 2:
        return 1
    else:
        return fibonachi(adad - 1) + fibonachi(adad -2)
if __name__ == "__main__":
    while True:
        try:
            inputnumber = int(input("tedad list khod ra bnvisid: "))
            if inputnumber < 1:
                print("lotfan y; adad bala 1 bnvisid.")
                continue
            fibonachilist = []
            for i in range(1, inputnumber + 1):
                fibonachilist.append(fibonachi(i))
            print(" , ".join(map(str, fibonachilist)))
            break
        except ValueError:
            print("lotfan adad sahih bnvisid.")