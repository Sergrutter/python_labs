import random

from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def check_sorting(fn, trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)

        result = fn(nums)

        assert result == sorted(nums), (f'{fn.__name__} ошиблась на {nums}: {result}')
        assert nums == original, (f'{fn.__name__} изменила исходный список')


def check_search():
    for _ in range(100):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]

        for x in nums + [random.randint(-120, 120)]:
            expected = nums.index(x) if x in nums else -1

            assert linear_search(nums, x) == expected

        arr = sorted(nums)

        for x in arr + [-121, 121]:
            result = binary_search(arr, x)

            if x in arr:
                assert result != -1 and arr[result] == x
            else:
                assert result == -1


def check_two_sum(trials=100):
    for _ in range(trials):
        n = random.randint(0, 30)
        nums = [random.randint(-20, 20) for _ in range(n)]
        target = random.randint(-40, 40)

        brute = two_sum_brute(nums, target)
        fast = two_sum_fast(nums, target)

        for pair in (brute, fast):
            if pair is not None:
                i, j = pair

                assert 0 <= i < j < len(nums)
                assert nums[i] + nums[j] == target

        assert (brute is None) == (fast is None)


if __name__ == '__main__':
    random.seed(42)

    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)

    check_search()
    check_two_sum()

    print('OK')
