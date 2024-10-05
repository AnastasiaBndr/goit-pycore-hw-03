from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.4"},
    {"name": "Jane Smith", "birthday": "1990.01.5"},
    {"name": "Christin Dae", "birthday": "1976.03.6"},
    {"name": "Erik Colson", "birthday": "1945.10.7"},
]


def get_upcoming_birthdays(users):
    current_date = datetime.today().date()
    users_birthday = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = datetime(
            year=current_date.year, day=birthday.day, month=birthday.month).date()
        time_difference = birthday_this_year - current_date

        if (0 <= time_difference.days < 7) or \
            (-366 <= time_difference.days < -359) or \
                (-365 <= time_difference.days < -358):
            if birthday_this_year.weekday() == 5:
                birthday_this_year += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:
                birthday_this_year += timedelta(days=1)

            users_birthday.append(
                {"name": user["name"], "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")})

    return users_birthday


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
