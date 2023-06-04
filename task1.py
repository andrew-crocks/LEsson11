def find_unique_value():
    numbers = input("Введіть список чисел, розділені пробілом: ").split()
    numbers = list(map(float, numbers))  # перетворюємо введені значення на список чисел
    unique_values = set(numbers)
    for value in unique_values:
        if numbers.count(value) == 1:
            return value
    return None

unique_value = find_unique_value()
print(unique_value)