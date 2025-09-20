def power_iterative(base, exp):
    """Звичайна ітеративна функція для піднесення до степеня."""
    result = 1
    for _ in range(abs(exp)):
        result *= base
    if exp < 0:
        return 1 / result
    return result

def power_recursive(base, exp):
    """Рекурсивна функція для піднесення до степеня."""
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / power_recursive(base, -exp)
    else:
        return base * power_recursive(base, exp - 1)

# Приклади використання:
print(power_iterative(2, 3))   # 8
print(power_iterative(2, -3))  # 0.125
print(power_recursive(2, 3))   # 8
print(power_recursive(2, -3))  # 0.125