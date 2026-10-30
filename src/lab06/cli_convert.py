
import argparse

from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description='Утилиты для конвертации файлов')
    subparsers = parser.add_subparsers(dest='command', required=True)

    json_parser = subparsers.add_parser('json2csv', help='Преобразовать JSON в CSV')
    json_parser.add_argument('--in', dest='input', required=True)
    json_parser.add_argument('--out', dest='output', required=True)

    csv_parser = subparsers.add_parser('csv2json', help='Преобразовать CSV в JSON')
    csv_parser.add_argument('--in', dest='input', required=True)
    csv_parser.add_argument('--out', dest='output', required=True)

    xlsx_parser = subparsers.add_parser('csv2xlsx', help='Преобразовать CSV в XLSX')
    xlsx_parser.add_argument('--in', dest='input', required=True)
    xlsx_parser.add_argument('--out', dest='output', required=True)

    args = parser.parse_args()

    if args.command == 'json2csv':
        json_to_csv(args.input, args.output)
        print(f'Файл CSV создан: {args.output}')

    elif args.command == 'csv2json':
        csv_to_json(args.input, args.output)
        print(f'Файл JSON создан: {args.output}')

    elif args.command == 'csv2xlsx':
        csv_to_xlsx(args.input, args.output)
        print(f'Файл XLSX создан: {args.output}')


if __name__ == '__main__':
    main()
