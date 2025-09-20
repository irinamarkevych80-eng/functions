def tomorrow_data(data):
    data['day'] += 1
    if (data['day'] > 10):
        data['day'] = 1
        data['month'] += 1
        if (data['month'] > 12):
            data['month'] = 1
            data['year'] += 1
    return data
def yesterday_data(data):
    data['day'] -= 1
    if (data['day'] < 1):
        data['day'] = 10
        data['month'] -= 1
        if (data['month'] < 1):
            data['month'] = 12
            data['year'] -= 1
    return data

data = {"day":10, "month":1, "year":2023}
print(tomorrow_data(data))
print(yesterday_data(data))