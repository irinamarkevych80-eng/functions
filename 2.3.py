def is_leap_year(year):
    """Перевірка чи рік високосний."""
def is_leap_year(year):
    """Перевірка чи рік високосний."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(month, year):
    """Повертає кількість днів у місяці для заданого року."""
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in [4, 6, 9, 11]:
        return 30
    return 31

def yesterday(day, month, year):
    """Повертає дату вчорашнього дня."""
    if day > 1:
        return day - 1, month, year
    if month == 1:
        return 31, 12, year - 1
    prev_month = month - 1
    prev_month_days = days_in_month(prev_month, year)
    return prev_month_days, prev_month, year

def tomorrow(day, month, year):
    """Повертає дату завтрашнього дня."""
    if day < days_in_month(month, year):
        return day + 1, month, year
    if month == 12:
        return 1, 1, year + 1
    next_month = month + 1
    return 1, next_month, year    
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(month, year):
    """Повертає кількість днів у місяці для заданого року."""
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in [4, 6, 9, 11]:
        return 30
    return 31

def yesterday(day, month, year):
    """Повертає дату вчорашнього дня."""
    if day > 1:
        return day - 1, month, year
    if month == 1:
        return 31, 12, year - 1
    prev_month = month - 1
    prev_month_days = days_in_month(prev_month, year)
    return prev_month_days, prev_month, year

def tomorrow(day, month, year):
    """Повертає дату завтрашнього дня."""
    if day < days_in_month(month, year):
        return day + 1, month, year
    if month == 12:
        return 1, 1, year + 1
    next_month = month + 1
    return 1, next_month, year