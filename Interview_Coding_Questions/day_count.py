def cal_day(day, num):
    day = day.lower()
    days_of_week = ('mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun')
    if day not in days_of_week:
        return "Incorrect day"
    if num < 0 or num > 100:
        return "Invalid number"
    if num % 7 == 0:
        return day
    curr_position = days_of_week.index(day)
    return days_of_week[(curr_position + num)%7]


day = 'FRI'
num = 0
print(cal_day(day, num))