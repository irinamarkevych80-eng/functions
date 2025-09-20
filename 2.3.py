def tomorrow_data(data):
    """Функция принимает дату и возвращает завтрашнюю дату.
    Args:
        data (dict): Словарь с ключами "day", "month", "year".
    Returns:
        dict: Словарь с ключами "day", "month", "year".
    """
    data['day'] += 1
    if (data['day'] > 31 or data['day'] > 30):
        data['day'] = 1
        data['month'] += 1
        if (data['month'] > 12):
            data['month'] = 1
            data['year'] += 1
    return data

def yesterday_data(data):
    """Функция принимает дату и возвращает вчерашнюю дату.
    Args:
        data (dict): Словарь с ключами "day", "month", "year".
    Returns:
        dict: Словарь с ключами "day", "month", "year".
    """
    data['day'] -= 1
    if (data['day'] < 1):
        data['day'] = 30
        data['month'] -= 1
        if (data['month'] < 1):
            data['month'] = 12
            data['year'] -= 1
    return data

data = {"day":10, "month":1, "year":2023}
print(tomorrow_data(data))
print(yesterday_data(data))