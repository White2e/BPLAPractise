import pdb

def error_code():
    numerator = 10
    denominator = 0
    pdb.set_trace()  # Устанавливаем точку останова перед потенциально опасным кодом

    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
    else:
        print(f"Результат: {result}")
    finally:
        print("Этот код выполнится в любом случае.")

error_code()
print("Программа продолжает работу.")
