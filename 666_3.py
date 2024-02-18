def count_unique_characters(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

# Приклад використання:
input_string = input("Введіть рядок: ")
unique_char_count = count_unique_characters(input_string)
print("Унікальні символи та кількість їх входжень:")
for char, count in unique_char_count.items():
    print(f"'{char}': {count}")
