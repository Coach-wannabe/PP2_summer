"""
Name of the company
BIN number
For each item:
    Title —— (Натрия хлорид 0,9%, 200 мл, фл)
    Cout ——  (2)
    Unit price —— (154,00)
    Total price —— (308,00)
Date —— (18.04.2019 11:13:58)
Address —— (г. Нур-султан,Казахстан, Мангилик Ел,19, нп-5)
"""

import re 
import csv

file = open("raw.txt", "r", encoding = "utf-8")
z = file.read()

nameComPattern = r"\nФилиал.(?P<NameCom>.*)"
nameComTxt = re.search(nameComPattern, z).group("NameCom")

binPattern = r"\nБИН.(?P<BIN>\b\d*)"
binTxt = re.search(binPattern, z).group("BIN")

itemPattern = r"\n{1}(?P<Title>.*)\n{1}(?P<Count>.*)x(?P<UnitPrice>.*)\n{1}(?P<TotalPrice>.*)\n{1}Стоимость\n{1}.*"
item = re.compile(itemPattern)
# itemTxt = re.findall(itemPattern, z)

dateAddressPattern = r"\nВремя:.(?P<Date>.*)\n(?P<Address>.*)"
dateTxt = re.search(dateAddressPattern, z).group("Date")
addressTxt = re.search(dateAddressPattern, z).group("Address")

# print(nameComTxt)
# print(binTxt)
# print(dateTxt)
# print(addressTxt)
# print(itemTxt)

items = [["Название компании", "БИН", "Наименование товара", "Количество",
          "Цена за единицу", "Общая сумма", "Дата", "Аддресс"]]

for i in re.finditer(itemPattern, z):
    items.append([nameComTxt, binTxt, i.group("Title"), i.group("Count"), 
    i.group("UnitPrice"), i.group("TotalPrice"), dateTxt, addressTxt])

with open('file.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    writer.writerows(items)
