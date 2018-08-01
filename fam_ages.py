
#Key = student name; value = disney character
fam = {
"Lien" :19,
"Niara" :22,
"Aline" :27,
"Germaine" :16,
"Andrew" :15,
"Dad" :47,
"Mom" :46,
"Sydney" :15,
}
for key, value in (fam.items()):
    print(key, value)

avg = 0

for key, value in sorted(fam.items()):
    avg += value

avg = float(avg / len(fam))
print(avg)
