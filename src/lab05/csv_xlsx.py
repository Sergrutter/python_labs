
import csv
from pathlib import Path

from openpyxl import Workbook


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """Преобразует CSV в XLSX с автоматической шириной колонок"""
    src = Path(csv_path)
    dst = Path(xlsx_path)

    if src.suffix.lower() != '.csv':
        raise ValueError('Входной файл должен иметь расширение .csv')

    if dst.suffix.lower() != '.xlsx':
        raise ValueError('Выходной файл должен иметь расширение .xlsx')

    with src.open('r', newline='', encoding='utf-8') as f:
        rows = list(csv.reader(f))

    if not rows or not rows[0] or not any(value.strip() for value in rows[0]):
        raise ValueError('CSV пустой или не содержит заголовка')

    if len(rows) < 2:
        raise ValueError('CSV не содержит строк с данными')

    width = len(rows[0])

    for row in rows:
        if len(row) != width:
            raise ValueError('Количество значений в строках CSV различается')

    wb = Workbook()
    ws = wb.active
    ws.title = 'Sheet1'

    for row in rows:
        ws.append(row)

    for col in ws.columns:
        letter = col[0].column_letter
        max_length = 0

        for cell in col:
            value = '' if cell.value is None else str(cell.value)
            max_length = max(max_length, len(value))

        ws.column_dimensions[letter].width = max(8, max_length + 2)

    dst.parent.mkdir(parents=True, exist_ok=True)
    wb.save(dst)
