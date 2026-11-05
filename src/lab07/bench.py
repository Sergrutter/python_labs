import csv
import random
import timeit
from pathlib import Path

from src.lab04.io_txt_csv import write_csv
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def make_samples(n):
    path = Path(__file__).resolve().parents[2] / 'data' / 'samples' / 'lab07' / f'numbers_{n}.csv'

    if path.exists():
        return

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['value'])
        for _ in range(n):
            w.writerow([random.randint(0, 1000000)])


def read_numbers(path):
    with open(path, encoding='utf-8') as f:
        return [int(row['value']) for row in csv.DictReader(f)]


def bench_sorts(n):
    make_samples(n)
    data = read_numbers(Path(__file__).resolve().parents[2] / 'data' / 'samples' / 'lab07' / f'numbers_{n}.csv')
    rows = []

    t = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(('sort', n, 'sorted', t))

    funcs = (
        ('bubble_sort', bubble_sort),
        ('insertion_sort', insertion_sort),
        ('selection_sort', selection_sort),
    )

    for name, fn in funcs:
        if n >= 100000:
            rows.append(('sort', n, name, '>60'))
            continue

        arr = data.copy() 
        start = timeit.default_timer()
        fn(arr)
        t = timeit.default_timer() - start

        rows.append(('sort', n, name, '>60' if t > 60 else t))

    return rows


def main():
    rows = []
    for n in (1000, 10000, 100000):
        rows.extend(bench_sorts(n))

    (Path(__file__).resolve().parents[2] / 'data' / 'lab07').mkdir(parents=True, exist_ok=True)

    write_csv(rows, Path(__file__).resolve().parents[2] / 'data' / 'lab07' / 'bench.csv', header=('task', 'n', 'impl', 'seconds'))

    for row in rows:
        print(row)

    print(f"Результаты сохранены: {Path(__file__).resolve().parents[2] / 'data' / 'lab07' / 'bench.csv'}")


if __name__ == '__main__':
    main()