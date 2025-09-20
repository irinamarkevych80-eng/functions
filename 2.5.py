# Приклад даних: вагон з 5 купе
wagon = [
    {1: None, 2: None, 3: None, 4: None},               # повністю вільне купе
    {1: 'ч', 2: None, 3: None, 4: None},                # частково зайняте
    {1: 'ж', 2: 'ж', 3: None, 4: None},                 # жіноча компанія
    {1: 'ч', 2: 'ч', 3: None, 4: None},                 # чоловіча компанія
    {1: 'ч', 2: 'ж', 3: None, 4: None},                 # змішана компанія
]

# 1. Список повністю вільних купе (індекси)
free_compartments = [i for i, c in enumerate(wagon) if all(v is None for v in c.values())]

# 2. Список вільних місць у вагоні (у форматі: [(купе, місце)])
free_seats = [(i, seat) for i, c in enumerate(wagon) for seat, v in c.items() if v is None]

# 3. Список вільних нижніх чи верхніх місць
free_lower = [(i, seat) for i, c in enumerate(wagon) for seat, v in c.items() if v is None and seat % 2 == 1]
free_upper = [(i, seat) for i, c in enumerate(wagon) for seat, v in c.items() if v is None and seat % 2 == 0]

# 4. Список вільних місць в купе з виключно чоловічою компанією
free_in_male_only = []
for i, c in enumerate(wagon):
    occupied = [v for v in c.values() if v is not None]
    if occupied and all(v == 'ч' for v in occupied):
        free_in_male_only.extend([(i, seat) for seat, v in c.items() if v is None])

# 5. Список вільних місць в купе з виключно жіночою компанією
free_in_female_only = []
for i, c in enumerate(wagon):
    occupied = [v for v in c.values() if v is not None]
    if occupied and all(v == 'ж' for v in occupied):
        free_in_female_only.extend([(i, seat) for seat, v in c.items() if v is None])

# Вивід результатів
print("Повністю вільні купе:", free_compartments)
print("Вільні місця у вагоні:", free_seats)
print("Вільні нижні місця:", free_lower)
print("Вільні верхні місця:", free_upper)
print("Вільні місця у купе з виключно чоловічою компанією:", free_in_male_only)
print("Вільні місця у купе з виключно жіночою компанією:", free_in_female_only)