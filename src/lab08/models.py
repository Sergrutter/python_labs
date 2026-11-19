
from datetime import date


STUDENT_FIELDS = ('fio', 'birthdate', 'group', 'gpa')


def make_student(fio, birthdate, group, gpa):
    if not isinstance(fio, str) or not fio.strip():
        raise ValueError('Некорректное ФИО')

    if not isinstance(group, str) or not group.strip():
        raise ValueError('Некорректная группа')

    if not isinstance(birthdate, str):
        raise ValueError('Дата должна быть строкой')

    try:
        birth = date.fromisoformat(birthdate)
    except ValueError:
        raise ValueError('Некорректная дата рождения')

    if birth.isoformat() != birthdate or birth > date.today():
        raise ValueError('Дата рождения указана неверно')

    if isinstance(gpa, bool) or not isinstance(gpa, (int, float)):
        raise ValueError('GPA должен быть числом')

    if not 0 <= gpa <= 5:
        raise ValueError('GPA должен быть от 0 до 5')

    return {
        'fio': fio.strip(),
        'birthdate': birthdate,
        'group': group.strip(),
        'gpa': float(gpa),
    }


def validate_student(rec):
    if not isinstance(rec, dict) or set(rec) != set(STUDENT_FIELDS):
        raise ValueError('Неверный набор полей студента')

    make_student(
        rec['fio'],
        rec['birthdate'],
        rec['group'],
        rec['gpa'],
    )


def student_age(rec, today=None):
    validate_student(rec)

    birth = date.fromisoformat(rec['birthdate'])
    today = today or date.today()

    age = today.year - birth.year

    if (today.month, today.day) < (birth.month, birth.day):
        age -= 1

    return age


def format_student(rec):
    validate_student(rec)

    fio = rec['fio'].split()
    initials = ''.join(part[0] + '.' for part in fio[1:])

    return (
        f'{fio[0]} {initials} ({rec["group"]}), '
        f'{student_age(rec)} лет, GPA {rec["gpa"]:.2f}'
    )


def student_to_dict(rec):
    validate_student(rec)
    return {key: rec[key] for key in STUDENT_FIELDS}


def student_from_dict(d):
    try:
        return make_student(
            d['fio'],
            d['birthdate'],
            d['group'],
            d['gpa'],
        )
    except (KeyError, TypeError) as error:
        raise ValueError(f'Некорректная запись студента: {error}')


def update_student(rec, **fields):
    validate_student(rec)

    if not set(fields).issubset(STUDENT_FIELDS):
        raise KeyError('Неизвестное поле')

    new_rec = student_to_dict(rec)
    new_rec.update(fields)

    if 'gpa' in fields and isinstance(fields['gpa'], (int, float)):
        new_rec['gpa'] = float(fields['gpa'])

    validate_student(new_rec)
    return new_rec
