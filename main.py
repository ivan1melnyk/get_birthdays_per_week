import calendar
from datetime import date, datetime, timedelta


def get_start_and_end_of_week(date):
    day_of_week = date.weekday()
    start_of_week = date - timedelta(days=day_of_week)
    end_of_week = start_of_week + timedelta(days=6)
    return start_of_week, end_of_week


def is_in_date_interval(start_of_interval, date, end_of_interval, should_print=False):
    result = start_of_interval <= date and date <= end_of_interval
    if should_print:
        print('\n', start_of_interval, date, end_of_interval, '===>', result)
    return result


def add_user(user, user_birthday, result):
    user_name = user['name'].split(" ")[0]
    day_of_week = calendar.day_name[user_birthday.weekday()]
    if day_of_week == 'Saturday' or day_of_week == 'Sunday':
        day_of_week = 'Monday'
    result[day_of_week].append(user_name)


def clear_empty_days(obj):
    new_obj = {}
    for day in obj:
        if obj[day]:
            new_obj[day] = obj[day]
    return new_obj


def get_birthdays_per_week(users, today=datetime(2023, 12, 26).date()):
    result = {
        "Sunday": [],
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": []
    }

    start_of_week, end_of_week = get_start_and_end_of_week(today)
    end_of_week += timedelta(days=1)

    for user in users:
        user_birthday = user['birthday'].replace(year=today.year)
        is_birthday_this_week = is_in_date_interval(
            start_of_week, user_birthday, end_of_week)

        if not is_birthday_this_week:
            user_birthday = user['birthday'].replace(year=today.year + 1)
            is_birthday_this_week = is_in_date_interval(
                start_of_week, user_birthday, end_of_week)

        if is_birthday_this_week:
            add_user(user, user_birthday, result)

    return clear_empty_days(result)


# ---------------------------------------------------------- MAIN CODE ----------------------------------------------------------

if __name__ == "__main__":
    users = [{"name": "Roll Jefriy", "birthday": datetime(1988, 11, 1).date()},
             {"name": "Myron Tor", "birthday": datetime(1955, 11, 1).date()},
             {"name": "Bill Gates", "birthday": datetime(1955, 11, 2).date()},
             {"name": "Andrey Brown", "birthday": datetime(
                 1955, 11, 3).date()},
             {"name": "Saimon Bricx", "birthday": datetime(
                 1955, 11, 4).date()},
             {"name": "Bull Gates", "birthday": datetime(1955, 11, 4).date()},
             {"name": "Bqll Gates", "birthday": datetime(1955, 11, 5).date()},
             {"name": "Bill Gates", "birthday": datetime(1955, 11, 6).date()},
             {"name": "Bill Gates", "birthday": datetime(1955, 11, 7).date()},
             {"name": "Bell Reackt", "birthday": datetime(1955, 11, 8).date()},
             {"name": "KOKI Jefriy", "birthday": datetime(
                 1988, 10, 31).date()},
             {"name": "Roky Jefriy", "birthday": datetime(1988, 11, 10).date()},]

    test_today = datetime(2023, 12, 26)
    result = get_birthdays_per_week(users)
    print('result', result)
