# Імпорт бібліотеки pandas під іменем pd
import pandas as pd

# Введення користувача: кількість бетонних плит для кожного місяця
months = ('Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень')
production_data = []

# Цикл для отримання введених користувачем даних
for month in months:
    try:
        # Введення кількості бетонних плит для кожного місяця
        quantity = int(input(f"Введіть кількість бетонних плит для місяця {month}: "))
        production_data.append(quantity)  # Додавання кількості до списку production_data
    except ValueError:
        print("Будь ласка, введіть ціле число.")

# Створення об'єкта Series з введеними даними і назвами місяців як індексами
production_series = pd.Series(production_data, index=months)

# Збереження даних у файл beton.json
production_series.to_json('beton.json')

# Виведення повідомлення про успішне збереження даних
print("Дані збережено у файл beton.json.")
