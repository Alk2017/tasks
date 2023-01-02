from datetime import datetime, timedelta

WEEK = 'WEEK'
MONTH = 'MONTH'
QUARTER = 'QUARTER'
YEAR = 'YEAR'
REVIEW = 'REVIEW'

DATE_FRMT = '%Y-%m-%d'


def next_sun(date):
    week_day = date.weekday()
    return date + timedelta(days=(6 - week_day))


def last_of_period(date, period):
    if period == WEEK:
        week_day = date.weekday()
        return date + timedelta(days=(6 - week_day))
    elif period == MONTH:
        return date.replace(
            year=(date.year + 1) if date.month == 12 else date.year,
            month=(date.month + 1) % 12,
            day=1
        ) - timedelta(days=1)
    elif period == QUARTER:
        month = date.month
        if month < 4:
            return date.replace(month=4, day=1) - timedelta(days=1)
        elif month < 7:
            return date.replace(month=7, day=1) - timedelta(days=1)
        elif month < 10:
            return date.replace(month=10, day=1) - timedelta(days=1)
        else:
            return date.replace(year=date.year + 1, month=1,
                                day=1) - timedelta(days=1)
    elif period == YEAR:
        return date.replace(year=date.year + 1, month=1, day=1) - timedelta(
            days=1)
    elif period == REVIEW:
        month = date.month
        if 9 < month or month < 4:
            return date.replace(year=date.year + 1, month=3, day=31)
        else:
            return date.replace(month=9, day=30)
    else:
        print('Wrong period')


def run():
    # per = input()
    # dates = input().split()
    per = WEEK
    dates = '2016-12-31 2017-01-29'.split()
    date1 = datetime.strptime(dates[0], DATE_FRMT).date()
    date2 = datetime.strptime(dates[1], DATE_FRMT).date()
    count = 0
    res = []
    first = date1
    last = last_of_period(date1, per)
    while last < date2:
        count += 1
        res.append(f'{first} {last}')
        first = last + timedelta(days=1)
        last = last_of_period(first, per)
    else:
        count += 1
        res.append(f'{first} {date2}')
    print(count)
    print('\n'.join(res))


if __name__ == '__main__':
    run()
