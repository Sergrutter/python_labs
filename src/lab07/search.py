def linear_search(nums, x):
    """Возвращает индекс первого вхождения x или -1"""
    for i, num in enumerate(nums):
        if num == x:
            return i

    return -1


def binary_search(nums, x):
    """Ищет x в отсортированном списке или возвращает -1"""
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == x:
            return mid
        elif nums[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def two_sum_brute(nums, target):
    """Находит пару индексов с заданной суммой перебором"""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j

    return None


def two_sum_fast(nums, target):
    """Находит пару индексов с помощью словаря"""
    seen = {}

    for i, num in enumerate(nums):
        need = target - num

        if need in seen:
            return seen[need], i

        seen[num] = i

    return None