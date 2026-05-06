olkeler = ["türkiye", "Almanya", "Fransa", "İtalya", "İspanya"]
print(olkeler[0])
print(olkeler[0].title())
print(olkeler[-2])

olkeler[0] = "Azərbaycan"
print(olkeler)

olkeler.append("Portuqaliya")
print(olkeler)

olkeler.insert(1, "Rusiya")
print(olkeler)

del olkeler[2]
print(olkeler)

popped_olkeler = olkeler.pop()
print(popped_olkeler)
print(olkeler)

print(olkeler.pop(0))
print(olkeler)

print(olkeler)

olkeler.sort()
print(olkeler)

olkeler.sort(reverse=True)
print(olkeler)

olkeler.reverse()
print(olkeler)
print(len(olkeler))