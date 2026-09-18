full = input("ФИО: ").split()
print(f'Инициалы: {full[0][0] + full[1][0] + full[2][0]}.')
print(f'Длина (символов): {2 + len(full[0]) + len(full[1]) + len(full[2])}')