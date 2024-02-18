def average_non_negative(numbers):
    non_negative_numbers = [num for num in numbers if num >= 0]
    return sum(non_negative_numbers) / len(non_negative_numbers) if non_negative_numbers else "У списку немає невід'ємних чисел."

# Приклад використання:
numbers = [1, 2, 3, -4, 5, -6, 7, -8, 9]
print("Середнє арифметичне невід'ємних чисел у списку:", average_non_negative(numbers))
