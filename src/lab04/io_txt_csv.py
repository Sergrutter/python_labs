import csv
from pathlib import Path
from typing import Iterable, Sequence


from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает текстовый файл в указанной кодировке. 
    По умолчанию используется UTF-8, но для файлов Windows можно указать encoding='cp1251' """

    p = Path(path)
    return p.read_text(encoding=encoding)


def ensure_parent_dir(path: str | Path) -> None:
    """Создаёт родительские директории, если их нет"""
    
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)


def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """Записывает строки в CSV-файл с разделителем - запятой"""

    p = Path(path)
    rows = list(rows)
    
    if rows:
        size = len(rows[0])

        for row in rows:
            if len(row) != size:
                raise ValueError('Все строки CSV должны иметь одинаковую длину')

        if header is not None and len(header) != size:
            raise ValueError('Количество столбцов заголовка не совпадает с данными')

    ensure_parent_dir(path)

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)