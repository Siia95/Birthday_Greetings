import datetime

users = [
    {'name': 'Alice', 'birthday': datetime.datetime(1990, 4, 22)},
    {'name': 'Bob', 'birthday': datetime.datetime(1995, 4, 26)},
    {'name': 'Bob2', 'birthday': datetime.datetime(1995, 4, 27)},
    {'name': 'Charlie', 'birthday': datetime.datetime(1985, 4, 24)},
    {'name': 'Dave', 'birthday': datetime.datetime(1980, 4, 23)},
    {'name': 'Eve', 'birthday': datetime.datetime(1998, 4, 25)},
]

def get_birthdays_per_week(users):
    for user in users:
        date_user = user['birthday'].date()
        date_week = date_user.strftime('%A')

        if date_user.weekday() == 5 or date_user.weekday() == 6:
            print(f'Monday: {user["name"]}')
        else:
            print(f'{date_week}: {user["name"]}')


get_birthdays_per_week(users)




