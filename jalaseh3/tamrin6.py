
def khayam_pasgal(n):
    mosalas = [[1]]


    for i in range(1, n):
        radif = [1]


        for j in range(1, i):
            radif.append(mosalas [i-1][j-1] + mosalas[i-1][j])


        radif.append(1)
        mosalas.append(radif)



    for row in mosalas:
        print("".join(str(x) for x in row))


adad = int(input("adad ra vared konid : "))
khayam_pasgal(adad)