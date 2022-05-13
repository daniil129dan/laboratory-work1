mas = ["a", "e","i","o","u"]
y = "y"

char = str(input('Введите букву латинского алфавита: '))
if len(char) == 1:
    if char in mas:
        print('Вы ввели гласную букву')
    elif char == y:
        print('Эта буква может быть как гласной, так и согласной')
    else:
        print('введена согласная буква')
else:
    while len(char) != 1:
        char = str(input('Введите букву латинского алфавита пожалуста: '))   
    if char in mas:
        print('Вы ввели гласную букву')
    elif char == y:
        print('Эта буква может быть как гласной, так и согласной')
