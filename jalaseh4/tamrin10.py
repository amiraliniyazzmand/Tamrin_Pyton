
print("addi kh vardd mikonid ra adad hayh zoj ra joda mikond :)")
while True:
    try:
        def adad_zoj(num):
            return num%2==0

        adad=input("adad ra joda bnvisid :")

        adadha = list(map(int,adad.split()))
        filter_adad= list(filter(adad_zoj,adadha))
        print("adad zoj", filter_adad)
    except ValueError:
        print("adad sahih vardd  konid")

