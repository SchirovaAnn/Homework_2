celebrities = ['Мэрилин Монро', 'Криштиану Роналду', 'Пушкин', 'Колумб', 'Наполеон']
year = [1926, 1985, 1799, 1451, 1769]

yes_no = True

while yes_no:
    answers = []
    for i in range(len(year)):
        q_tmp = int(input(f'Назовите год рождения {celebrities[i]}?'))
        if q_tmp == year[i]:
            answers.append(1)
        else:
            answers.append(0)

    print(f'Количество правильных ответов: {sum(answers)}')
    print(f'Количество неправильных ответов: {len(answers)-sum(answers)}')
    print(f'Процент правильных ответов: {sum(answers)*100/len(answers)}')
    print(f'Процент неправильных ответов: {(len(answers)-sum(answers))*100/len(answers)}')

    con = input('Вы хотите продолжить игру (Введите Да или Нет)?')
    if con=='Да':
        continue
    else:
        break

