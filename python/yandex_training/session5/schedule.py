months_with_days = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31,
}

months = list(months_with_days.keys())

days = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
]


def run():
    real_input = True
    if real_input:
        holiday_count = int(input())
        year = int(input())
        holidays = []
        for _ in range(holiday_count):
            i = input().split()
            holidays.append([int(i[0]), i[1]])
        first_day_year = days.index(input())
    else:
        year = 2013
        holidays = [
            [6, 'February'],
            [13, 'February'],
            [20, 'February'],
        ]
        first_day_year = days.index('Tuesday')

    # 1
    leap = False
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        leap = True
        months_with_days['February'] += 1

    # 2
    work_days = {
        0: 52,
        1: 52,
        2: 52,
        3: 52,
        4: 52,
        5: 52,
        6: 52,
    }

    work_days[first_day_year] += 1
    if leap:
        work_days[(first_day_year+1)%7] += 1

    # print(work_days)

    # 3
    count = first_day_year
    day_for_month = []
    for month in months:
        day_for_month.append(count)
        count += months_with_days[month]

    # print(day_for_month)

    for holiday in holidays:
        first_day_month = day_for_month[months.index(holiday[1])]
        first_day_month += holiday[0] - 1
        # print(first_day_month)
        first_day_month %= 7
        # print(first_day_month)
        work_days[first_day_month] -= 1

    # print(work_days)

    min_num = min(work_days.values())
    max_num = max(work_days.values())
    for day in work_days.keys():
        if work_days[day] == min_num:
            min_day = day
        if work_days[day] == max_num:
            max_day = day

    print(days[max_day])
    print(days[min_day])


if __name__ == '__main__':
    run()
