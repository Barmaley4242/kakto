from random import shuffle
spisok_omg = []

triks = input('Введи ингридиент (стоп слово"хорош")')
while triks != 'хорош':
    if triks in spisok_omg:
        print('Это уже есть')
    else:
        spisok_omg.append(triks)

    triks = input('Введи ингридиент (стоп слово "хорош")')

spisok_blender = []
nume = int(input("сколько надо ингридиентов"))
for i in range(nume):
    shuffle(spisok_omg)
    spisok_blender.append(spisok_omg[0])
    spisok_omg.remove(spisok_omg[0])

print('приготовить что нибудь')
for i in range(nume):
    print(spisok_blender[i])