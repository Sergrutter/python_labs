
import csv
import json
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """Преобразует список словарей из JSON в CSV"""
    
    src = Path(json_path)
    dst = Path(csv_path)

    if src.suffix.lower() != '.json':
        raise ValueError('Входной файл должен иметь расширение .json')

    if dst.suffix.lower() != '.csv':
        raise ValueError('Выходной файл должен иметь расширение .csv')

    with src.open('r', encoding='utf-8') as f:
        data = json.load(f)

    if not isinstance(data, list) or not data:
        raise ValueError('Пустой JSON или неподдерживаемая структура')

    fields = sorted({key for item in data for key in item})

    dst.parent.mkdir(parents=True, exist_ok=True)

    with dst.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """Преобразует CSV в список словарей JSON"""

    src = Path(csv_path)
    dst = Path(json_path)

    if src.suffix.lower() != '.csv':
        raise ValueError('Входной файл должен иметь расширение .csv')

    if dst.suffix.lower() != '.json':
        raise ValueError('Выходной файл должен иметь расширение .json')

    with src.open('r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        if not reader.fieldnames or not any(reader.fieldnames):
            raise ValueError('CSV пустой или не содержит заголовка')

        data = list(reader)

    if not data:
        raise ValueError('CSV не содержит строк с данными')

    dst.parent.mkdir(parents=True, exist_ok=True)

    with dst.open('w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
