
import csv
import json
from pathlib import Path

from src.lab08.models import student_from_dict, student_to_dict


def students_to_json(students, path):
    """Сохраняет список записей в JSON"""
    data = [student_to_dict(student) for student in students]

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def students_from_json(path):
    """Загружает студентов из JSON"""
    with open(path, encoding='utf-8') as file:
        data = json.load(file)

    students = []

    for i, item in enumerate(data, start=1):
        try:
            students.append(student_from_dict(item))
        except (ValueError, TypeError) as error:
            raise ValueError(f'record {i}: {error}') from error

    return students


def students_from_csv(path):
    """Загружает студентов из CSV"""
    students = []

    with open(path, encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)

        for i, row in enumerate(reader, start=1):
            try:
                row['gpa'] = float(row['gpa'])
                students.append(student_from_dict(row))
            except (ValueError, TypeError, KeyError) as error:
                raise ValueError(f'record {i}: {error}') from error

    return students
