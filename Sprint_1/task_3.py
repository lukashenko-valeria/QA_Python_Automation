world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}
world_champions[2022] = 'Аргентина'

for key, value in world_champions.items():
    print(key, '-', value)

country = 'Италия'
found = False
for value in world_champions.values():
    if country == value:
        found = True
        print('Италия cтановилась чемпионом мира по футболу в 21 веке!')
        break

if not found:
    print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')
