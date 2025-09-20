def sum_of_digits(n):
    """Рекурсивно повертає суму цифр числа n."""
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

def count_digits(n):
    """Рекурсивно повертає кількість цифр у числі n."""
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

# Приклади використання:
number = 12345
print(f"Сума цифр: {sum_of_digits(number)}")       # 15
print(f"Кількість цифр: {count_digits(number)}")   # 5