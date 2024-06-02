name = input("Напишіть ваше ім'я:\n")
print(f'Hello {name}')

while True:
    you = input('Ти любиш сам себе? так/ні\n')
    if you == 'так':
        print('Молодець')
        break
    if you == 'ні':
        print('ЩО ТІЛЬКИ Я САМ СЕБЕ ЛЮБЛЮ??')
        break
    else:
        print('І як мені це розуміти?')