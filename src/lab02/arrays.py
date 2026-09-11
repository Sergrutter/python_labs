def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError

    return tuple([min(nums), max(nums)])

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    set_nums = set(nums)
    massive = list(set_nums)
    massive.sort()
    return massive

def flatten(mat: list[list | tuple]) -> list:
    massive = []

    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError

        for elements in row:
            massive.append(elements)

    return massive


