def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec, tuple) or len(rec) != 3:
        raise ValueError('Запись должна содержать ФИО, группу и GPA')

    fio, group, gpa = rec

    if not isinstance(fio, str) or not isinstance(group, str):
        raise TypeError('ФИО и группа должны быть строками')

    if not fio.strip() or not group.strip():
        raise ValueError('ФИО и группа не могут быть пустыми')

    if not isinstance(gpa, (int, float)) or isinstance(gpa, bool):
        raise TypeError('GPA должен быть числом')

    if gpa < 0.0 or gpa > 5.0:
        raise ValueError('GPA должен быть от 0.0 до 5.0')

    fio_parts = fio.strip().split()

    if len(fio_parts) < 2:
        raise ValueError('ФИО должно содержать фамилию и имя')

    surname = fio_parts[0].capitalize()
    initials = ''

    for name in fio_parts[1:3]:
        initials += name[0].upper() + '.'

    group = group.strip()

    return f'{surname} {initials}, гр. {group}, GPA {gpa:.2f}'

# print(format_record(
#     ("Иванов Иван Иванович", "BIVT-25", 4.6)
# ))

# print(format_record(
#     ("Петров Пётр", "IKBO-12", 5.0)
# ))

# print(format_record(
#     ("Петров Пётр Петрович", "IKBO-12", 5.0)
# ))

# print(format_record(
#     ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
# ))