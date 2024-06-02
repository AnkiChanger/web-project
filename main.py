name = input("Напишіть ваше ім'я:\n")
print(f'Hello {name}')

while True:
    you = input(f'{name}, Ти любиш сам себе? так/ні\n')
    if you == 'так':
        print(f'Молодець {name}')
        break
    if you == 'ні':
        print('ЩО ТІЛЬКИ Я САМ СЕБЕ ЛЮБЛЮ??')
        break
    else:
        print('І як мені це розуміти?')