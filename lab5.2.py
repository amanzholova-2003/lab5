spisok = {
    "Assel": ( 90,85,70,88),
    "Merey": (95,100,100,82),
    "Maira": (73,84,65,86),
    "Balzhan": (95,76,77,81),
    "Aizhan": (88,79,100,80),
    "Zhadyra":(87,76,97,98)}
spi = sorted(spisok.items(), key=lambda spisok: spisok[0])
print(spi)

name = str(input("Name: "))
for key in spisok:
    if key == name:
        print(spisok[key])