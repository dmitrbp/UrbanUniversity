team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score1 + score2  #82
time_avg = round((team1_time + team2_time) / tasks_total, 1)  # 45.2
# challenge_result = 'Победа команды Волшебники данных!'
challenge_result = f'{
    f'победа команды {team1_name}' if score1 > score2
    else f'победа команды {team2_name}' if score2 > score1
    else 'Ничья'
}'

print('В команде Мастера кода участников: %s !' % team1_num)
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))
print('Команда Волшебники данных решила задач: {} !'.format(score2))
print('Волшебники данных решили задачи за {} с !'.format(team2_time))
print(f'Команды решили {score1} и {score2} задач.')
print(f'Результат битвы: {challenge_result} !')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')
