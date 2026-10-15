
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib.text import count_freq, normalize, tokenize, top_n
from lab04.io_txt_csv import read_text, write_csv


def get_freq(text: str) -> dict[str, int]:
    """Возвращает частоты слов в тексте"""

    tokens = tokenize(normalize(text))
    return count_freq(tokens)


def sort_freq(freq: dict[str, int]) -> list[tuple[str, int]]:
    """Сортирует словарь по убыванию частоты и алфавиту"""

    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def print_stats(freq: dict[str, int]) -> None:
    """Выводит статистику и топ-5 слов"""
    
    total = sum(freq.values())
    top = top_n(freq, 5)

    print(f'Всего слов: {total}')
    print(f'Уникальных слов: {len(freq)}')
    print('Топ-5:')

    for word, count in top:
        print(f'{word}: {count}')


def main() -> None:
    """Обрабатывает входные файлы и формирует CSV-отчёты"""

    parser = argparse.ArgumentParser(
        description='Подсчёт частот слов в текстовых файлах'
    )

    parser.add_argument(
        '--in',
        dest='inputs',
        nargs='+',
        default=['data/lab04/input.txt'],
        help='Пути к входным TXT-файлам'
    )

    parser.add_argument(
        '--out',
        default='data/lab04/report.csv',
        help='Путь к CSV-отчёту для одного файла'
    )

    parser.add_argument(
        '--encoding',
        default='utf-8',
        help='Кодировка входных файлов'
    )

    parser.add_argument(
        '--per-file',
        help='Путь к отчёту по каждому файлу'
    )

    parser.add_argument(
        '--total',
        help='Путь к общему отчёту по всем файлам'
    )

    args = parser.parse_args()

    if len(args.inputs) == 1 and not args.per_file and not args.total:
        text = read_text(args.inputs[0], encoding=args.encoding)
        freq = get_freq(text)

        rows = sort_freq(freq)
        write_csv(rows, args.out, header=('word', 'count'))
        print_stats(freq)
        return

    total_freq = {}
    per_file_rows = []

    for file_path in sorted(args.inputs):
        text = read_text(file_path, encoding=args.encoding)
        freq = get_freq(text)
        file_name = Path(file_path).name

        for word, count in sort_freq(freq):
            per_file_rows.append((file_name, word, count))
            total_freq[word] = total_freq.get(word, 0) + count

    per_file_path = args.per_file or 'data/lab04/report_per_file.csv'
    total_path = args.total or 'data/lab04/report_total.csv'

    per_file_rows.sort(key=lambda row: (row[0], -row[2], row[1]))

    write_csv(per_file_rows, per_file_path, header=('file', 'word', 'count'))
    write_csv(sort_freq(total_freq), total_path, header=('word', 'count'))

    print_stats(total_freq)


if __name__ == '__main__':
    main()
