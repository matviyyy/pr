lista = str(input('Введіть текст:')).split()

print(len(lista))
print(max(lista, key=len))
