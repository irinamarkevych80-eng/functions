votes = [1, 3, 2, 2, 2, 5, -1, 1, 2, 2, 4, 2, 3, 5, 5, 2, -1, 4, 1, 2]  # приклад

party_names = {
    1: "Партія №1",
    2: "Партія №2",
    3: "Партія №3",
    4: "Партія №4",
    5: "Партія №5"
}

# Підрахунок голосів за партії
from collections import Counter

counter = Counter(v for v in votes if v != -1)
total_valid = sum(counter.values())

# Формування підсумків
results = []
for party_num, party_name in party_names.items():
    count = counter.get(party_num, 0)
    percent = (count / total_valid * 100) if total_valid > 0 else 0
    results.append((party_num, party_name, count, percent))

# Сортування за кількістю голосів
results.sort(key=lambda x: x[2], reverse=True)

# Вивід
for idx, (party_num, party_name, count, percent) in enumerate(results, 1):
    print(f"{idx}. {party_name} | {count} | {percent:.2f}%")