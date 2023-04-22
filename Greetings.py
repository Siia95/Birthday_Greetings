from datetime import datetime, timedelta

users = [
    {'name': 'AliceTest', 'birthday': datetime(1990, 4, 16)},
    {'name': 'Alice', 'birthday': datetime(1990, 4, 19)},
    {'name': 'Bob', 'birthday': datetime(1995, 4, 18)},
    {'name': 'Bob2', 'birthday': datetime(1995, 4, 18)},
    {'name': 'Charlie', 'birthday': datetime(1985, 4, 19)},
    {'name': 'Dave', 'birthday': datetime(1980, 4, 20)},
    {'name': 'Eve', 'birthday': datetime(1998, 4, 21)},
    {'name': 'Vlad', 'birthday': datetime(1996, 4, 23)},
]

def get_birthdays_per_week(users):
    today = datetime.today().date()
    last_saturday_week = today - timedelta(days=today.weekday() + 2)
    last_friday_week = last_saturday_week + timedelta(days=6)
    birthdays_by_weekday = {}
    is_leap = datetime(int(today.strftime('%Y')), 1, 1).isocalendar()[1] == 1

    for user in users:
        if last_saturday_week.strftime('%-m%e') <= user['birthday'].date().strftime('%-m%e') <= last_friday_week.strftime('%-m%e'):
            birth_date = datetime(int(today.strftime('%Y')), int(today.strftime('%-m')), 28) if not is_leap and int(user['birthday'].date().strftime('%e')) == 29 and int(user['birthday'].date().strftime('%-m')) == 2 else datetime(int(today.strftime('%Y')), int(today.strftime('%-m')), int(user['birthday'].date().strftime('%e')))

            if birth_date.weekday() == 5 or birth_date.weekday() == 6:
                day = 'Monday'
            else:
                day = birth_date.strftime('%A')
            if day not in birthdays_by_weekday:
                birthdays_by_weekday[day] = []
            birthdays_by_weekday[day].append(user['name'])

    sorted_birthdays = dict(sorted(birthdays_by_weekday.items()))

    for day, names in sorted_birthdays.items():
        print(f'{day}: {", ".join(names)}')

get_birthdays_per_week(users)




