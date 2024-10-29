import xml_python
voroodi_file = input("Lotfan Location file ro vared konid : ")
joda = voroodi_file.split(".")
if joda[-1] == "xml":
    try:
        with open(voroodi_file, "r") as xml_file:
            xml_file = xml_python.parse(voroodi_file)
            root_xml = xml_file.getroot()
            print("-" * 40)
            print("dar matn zir vared konid : [ all ], [ anjam shode ya completed ], [ dar entezar ya pending ]")
            print("-" * 40)
            khorooji = input("kodam kar ha ro behet neshoon bedam? ")
            for child in root_xml.findall("kar"):

                title = child.find("Title").text
                Date = child.find("Date").text
                Olaviat = child.find("Olaviat").text
                vaziat = child.find("vaziat").text

                if khorooji.lower() == "all":
                    print("=-" * 10)
                    print(f"Title: {title}\n"
                          f"Date: {Date}\n"
                          f"Olaviat: {Olaviat}\n"
                          f"Vaziat: {vaziat}")

                elif khorooji.lower() == "anjam shode" or khorooji.lower() == "completed":
                    if vaziat == "anjam shode" or vaziat == "completed":
                        print("=-" * 10)
                        print(f"Title: {title}")
                        print(f"Date: {Date}")
                        print(f"Olaviat: {Olaviat}")
                        print(f"Vaziat: {vaziat}")

                elif khorooji.lower() == "dar entezar" or khorooji.lower() == "pending":
                    if vaziat == "dar entezar" or vaziat == "pending":
                        print("=-" * 10)
                        print(f"Title: {title}")
                        print(f"Date: {Date}")
                        print(f"Olaviat: {Olaviat}")
                        print(f"Vaziat: {vaziat}")
                else:
                    print("lotfan yeki az gozine ha ro entakhab kon!, [ Please Try Again ]")
                    break
    except FileNotFoundError:
        print("-" * 40)
        print("Error!\nFile peyda nashod!, [ Please Try Again ]")
        print("-" * 40)

else:
    print("-" * 30)
    print("Error!\nlotfan file [xml] vared konid!, [ Please Try Again ]")
    print("-" * 30)