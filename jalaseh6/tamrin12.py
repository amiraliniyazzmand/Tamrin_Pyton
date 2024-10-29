import json
with open('apple.json', 'r') as json_file:


    dict_json = json.load(json_file)

    with open("report.txt", 'w', encoding="utf-8") as report:
        report.write("\n")
        for etelaat in dict_json:
            if etelaat == "sector":

                report.write("\n")

                report.write(f"sector: {dict_json[etelaat]}")

                report.write("\n")

            if etelaat == "fullTimeEmployees":

                report.write("\n")

                report.write(f"fullTimeEmployees: {dict_json[etelaat]}")

                report.write("\n")

            if etelaat == "longBusinessSummary":

                report.write("\n")

                list_etelaat = dict_json[etelaat].split(". ")

                report.write("longBusinessSummary:")

                report.write("\n")

                for ch in list_etelaat:
                    for ch2 in ch:
                        if ch2 == ".":
                            report.write(f"\t{ch}")

                            report.write("\n")
                            break
                    else:
                        report.write(f"\t{ch}.")
                        report.write("\n")

            if etelaat == "city":
                report.write("\n")
                report.write(f"city: {dict_json[etelaat]}")
                report.write("\n")

            if etelaat == "phone":
                report.write("\n")

                report.write(f"phone : {dict_json[etelaat]}")

                report.write("\n")

            if etelaat == "country":
                report.write("\n")

                report.write(f"country: {dict_json[etelaat]}")
                report.write("\n")
    with open("report.txt", "r") as Report:
        print(Report.read())
print("payan:")