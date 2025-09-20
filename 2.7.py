def split_and_sort(*args):
    negatives = sorted([x for x in args if x < 0], reverse=True)
    non_negatives = sorted([x for x in args if x >= 0])
    return (negatives, non_negatives)

# Приклад використання:
result = split_and_sort(3, -1, 0, 7, -5, 2, -10)
print(result)  # ([-1, -5, -10], [0, 2, 3, 7])