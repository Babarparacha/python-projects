daily_goal = int(input('What is your daily step goal: '))
step_run = int(input('How many steps have you taken today: '))

remain = daily_goal - step_run

if remain > 0:
    print(f'You need {remain} more steps to complete your goal.')
elif remain < 0:
    print('Great! You have done some extra steps.')
else:
    print('Congratulations! You have nailed it!')
