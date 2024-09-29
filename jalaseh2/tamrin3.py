while True:
    def MohitMasahat(tol,arz):
        print("mohit mostatil :", (tol + arz) * 2)
        print("msahat mostatil :", tol * arz)
    try:
        tol = int(input("tol ra bnvisid : "))
        arz = int(input("arz ra bnvisid : "))
        MohitMasahat(tol, arz)
    except ValueError:
        print("adad sahih vard knid")
