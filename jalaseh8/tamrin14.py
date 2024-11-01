import csv

addres = input("addres file ra vared konid : ")



joda = addres.split(".")


if joda[-1] == "csv":
    try:
        with open(addres, "r") as csv_file:
            majmoo = 0
            reader = csv.reader(csv_file)
            header = next(reader)
            print("gheymat ha :")


            for row in reader:
                print(f"\t+ {row[-1]}")


                row = float(row[-1])
                majmoo += row


            print(f"\t {majmoo}")
            print(f"majmoo ghaymat : {majmoo}")
    except FileNotFoundError:
        print("File peyda nashod !")
else:
    print("Lotfan file csv vared konid")