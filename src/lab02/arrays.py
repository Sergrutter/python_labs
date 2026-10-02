def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError('Пустой список')

    min_value = nums[0]
    max_value = nums[0]

    for num in nums:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num

    return min_value, max_value


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    unique = []

    for num in nums:
        if num not in unique:
            unique.append(num)

    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if unique[i] > unique[j]:
                unique[i], unique[j] = unique[j], unique[i]

    return unique


def flatten(mat: list[list | tuple]) -> list:
    result = []

    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError('Строка матрицы должна быть списком или кортежем')

        for item in row:
            result.append(item)

    return result
