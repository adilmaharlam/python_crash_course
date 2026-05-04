qonaqlar = ['Elon Musk', 'Alexander Wang', 'Mark Zuckerberg', 'Larry Elisson']

gele_bilmir = qonaqlar.pop(1)
print(f"{gele_bilmir} şam yeməyinə gələ bilməyəcək.")

qonaqlar.insert(1, 'Bill Gates')

print("\nYeni qonaqlar siyahısı:")

message_1 = f"{qonaqlar[0]} səni şam yeməyinə dəvət edirəm."
message_2 = f"{qonaqlar[1]} səni şam yeməyinə dəvət edirəm."
message_3 = f"{qonaqlar[2]} səni şam yeməyinə dəvət edirəm."
message_4 = f"{qonaqlar[3]} səni şam yeməyinə dəvət edirəm."

print(message_1)
print(message_2)
print(message_3)
print(message_4)