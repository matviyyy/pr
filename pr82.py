n = int(input('Введіть кількість рядків:'))

result_lines = []
lines = []

for i in range(n):
    s = (input('Введіть рядок:'))
    if len(s) % 2 == 0:
        lines.append(s)
    else:
        print("Рядок не парної довжини і буде проігнорований.")


for line in lines:
    middle_index = len(line) // 2 -1
    modified_line = line[:middle_index]+ line[middle_index].upper() + line[middle_index+1].upper() + line[middle_index +2:]
    result_lines.append(modified_line)

print("Результат:")
for line in result_lines:
    print(line)
