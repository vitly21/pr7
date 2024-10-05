def to_base_13_recursive(number):
    digits = "0123456789ABC"

    if number < 13:
        return digits[number]
    return to_base_13_recursive(number // 13) + digits[number % 13]

try:
    decimal_number = int(input("Введите десятичное число: "))

    base_13_result = to_base_13_recursive(decimal_number)

    print(f"Число в тринадцатиричной системе: {base_13_result}")
except ValueError:
    print("Ошибка! Введите целое число.")
