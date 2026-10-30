
import argparse
from pathlib import Path

from src.lib.text import normalize, tokenize, count_freq, top_n


def main():
    parser = argparse.ArgumentParser(description='Утилиты для работы с текстовыми файлами')
    subparsers = parser.add_subparsers(dest='command', required=True)

    cat_parser = subparsers.add_parser('cat', help='Вывести содержимое файла')
    cat_parser.add_argument('--input', required=True, help='Путь к файлу')
    cat_parser.add_argument('-n', action='store_true', help='Нумеровать строки')

    stats_parser = subparsers.add_parser('stats', help='Подсчитать частоты слов')
    stats_parser.add_argument('--input', required=True, help='Путь к файлу')
    stats_parser.add_argument('--top', type=int, default=5, help='Количество самых частых слов')

    args = parser.parse_args()

    if args.command == 'cat':
        path = Path(args.input)
        text = path.read_text(encoding='utf-8')

        lines = text.splitlines()

        for i, line in enumerate(lines, start=1):
            if args.n:
                print(f'{i}: {line}')
            else:
                print(line)

    elif args.command == 'stats':

        path = Path(args.input)
        text = path.read_text(encoding='utf-8')

        words = tokenize(normalize(text))
        freq = count_freq(words)
        result = top_n(freq, args.top)

        print(f'Всего слов: {len(words)}')
        print(f'Уникальных слов: {len(freq)}')
        print(f'Топ-{args.top} слов:')

        for word, count in result:
            print(f'{word}: {count}')


if __name__ == '__main__':
    main()
