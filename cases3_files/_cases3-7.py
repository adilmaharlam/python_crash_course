qonaqlar = ['Elon Musk', 'Alexander Wang', 'Mark Zuckerberg', 'Larry Elisson']
message_a = "\n\tTəəssüflər olsunki sadəcə 2 nəfəri şam yeməyinə dəvət edə bilərəm"
print(message_a)

x1 = qonaqlar.pop(0)
print(f"{x1} təəssüflər olsunki şam yeməyinə sizi dəvət edə bilməyəcəyəm.")

x2 = qonaqlar.pop(0)
print(f"{x2} təəssüflər olsunki şam yeməyinə sizi dəvət edə bilməyəcəyəm.")

print("\n\tYeni qonaqlar siyahısı:")

message_1 = f"{qonaqlar[0]} siz hələdə dəvətlisiniz."
message_2 = f"{qonaqlar[1]} siz hələdə dəvətlisiniz."

print(message_1)
print(message_2)

del qonaqlar[0]
del qonaqlar[0]

print("\n\tQonaqlar siyahısı tamamilə boşaldıldı:")
print(qonaqlar)