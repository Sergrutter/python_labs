def bubble_sort(nums):
    """Возвращает новый отсортированный список"""
    arr = list(nums)
    n = len(arr)

    for i in range(n - 1):
        change = False

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                change = True

        if not change:
            break

    return arr


def insertion_sort(nums):
    """Возвращает новый отсортированный список"""
    arr = list(nums)

    for i in range(1, len(arr)):
        num = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > num:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = num

    return arr


def selection_sort(nums):
    """Возвращает новый отсортированный список"""
    arr = list(nums)
    n = len(arr)

    for i in range(n):
        min_pos = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_pos]:
                min_pos = j

        arr[i], arr[min_pos] = arr[min_pos], arr[i]

    return arr