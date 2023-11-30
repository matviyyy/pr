import pandas as pd

# Читання даних з CSV-файлу та запис у DataFrame
df = pd.read_csv("your_input_file.csv")

# Виведення початкового DataFrame
print("Початковий DataFrame:")
print(df)

# Додавання стовпчиків з обсягами продаж за листопад і грудень
df['Обсяг продаж листопад'] = [100, 150, 200, 120]
df['Обсяг продаж грудень'] = [80, 90, 110, 130]

# Запис DataFrame у новий CSV-файл
df.to_csv("your_output_file.csv", index=False)

# Виведення оновленого DataFrame
print("\nОновлений DataFrame:")
print(df)
