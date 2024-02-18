def is_palindrome(string):
    return string == string[::-1]

input_string = input("Введіть рядок: ")
if is_palindrome(input_string):
    print("Введений рядок - паліндром.")
else:
    print("Введений рядок - не паліндром.")
