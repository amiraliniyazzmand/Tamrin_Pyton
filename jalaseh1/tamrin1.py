try:
    age1 = int(input("sen khod ra vard knid :"))
    if age1 >=18:
        print("mitvani ray bdi")
    if age1 <=1:
        print("payyn ast")
    else:
        print("nmitvani ray bdi")
except ValueError:
    print("add shih vard knid")
print("payan")