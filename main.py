import random

#1
adatok = []
darabszam = 100
for db in range(darabszam):
    adatok.append(random.randint(50, 150))
print(adatok)


#összegzés tétele
#sum - határozza meg az adatok lista elemeinek összegét
sum = 0
for item in adatok:
    sum += item

print(f"sum(lista) - {sum}")


#átlag - az adatok lista elemeinek átlagának meghatározása

sum = 0
for item in adatok:
    sum += item
atlag = sum / len(adatok)

print(f"átlag(lista) - {atlag}")


#prod - az adatok lista elemeinek szorzatának meghatározása

prod = 1
for item in adatok:
    prod *= item

print(f"prod(lista) - {prod}")


#min-max tétel 
#min - határozza meg az adatok lista legkisebb elemét

min = adatok[0]
for item in adatok:
    if item < min:
        min = item

print(f"min(lista) - {min}")


#max - határozza meg az adatok lista legnagyobb elemét

max = adatok[0]
for item in adatok:
    if item > max:
        max = item

print(f"max(lista) - {max}")


#megszámlálás tétele
#határozza meg a 120nál nagyobb elemek darabszámát

db1 = 0
for item in adatok:
    if item > 120:
        db1 += 1

print(f"db1(lista) - {db1}")


#határozzátok meg hogy az adatok lista hány darab százas elemet tartalmaz

db2 = 0
for item in adatok:
    if item == 100:
        db2 += 1

print(f"db2(lista) - {db2}")


#eldöntés tétele
#legalább egy elem teljesíti a feltételt
#döntse el hogy az adatok lista elemei között van-e 50-es értékű elem

vanE_50 = False
for item in adatok:
    if item == 50:
        vanE_50 = True
        break

if vanE_50:
    print("A lista tartalmaz legalább egy olyan elemet, amely értéke 50") 
else:
    print("A lista nem tartalmaz 50-es értékű elemet") 


#minden elem teljesíti
#döntse el hogy az adatok lista mindem eleme kisebb, mint 150

mindenE_kisebb150 = True
for item in adatok:
    if not (item < 150):
        mindenE_kisebb150 = False
        break

if mindenE_kisebb150:
    print("A lista összes eleme kisebb, mint 150") 
else:
    print("A lista nem összes eleme kisebb, mint 150") 


#kiválasztás tétele
#!!!!!!!!!!!!!!! ELŐFORDUL HOGY AMIT SZERETNÉNK KIVÁLASZTANI, OLYAN NINCS IS  
#határozza meg a lista 50-es értékének első előfordulását

elem50 = None
for item in adatok:
    if item == 50:
        elem50 = item
        break

if elem50 != None:
    print(f"Van megfelelő elem, amely értéke: {elem50}")
else:
    print("Nincs megfelelő elem")


#keresés tétele
#!!!!!!!!! HA NINCS MEGFELELŐ ELEM, AKKOR NINCS IS INDEXE
#határozza meg az adatok listában a 100-as értékű elem helyét (előfordulásának helyét)

index100 = None
for i in range(len(adatok)):
    if adatok[i] == 100:
        index100 = i
        break

if index100 != None:
    print(f"Van megfelelő elem (100-as értékű), amely indexe: {index100}")
else:
    print("Nincs megfelelő elem. (100-as értékű)")


#buborékos rendezés
#rendezzük az adatok listát növekvő sorrendbe
for i in range(len(adatok)-1, 0, -1):
    for j in range(i):
        if adatok[j] > adatok[j+1]:
            adatok[j], adatok[j+1] = adatok[j+1], adatok[j]

print(adatok)