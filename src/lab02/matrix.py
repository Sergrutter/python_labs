def check_matrix(mat: list[list[float | int]]) -> None:
    if not mat:
        return

    length = len(mat[0])

    for row in mat:
        if len(row) != length:
            raise ValueError('Матрица должна быть прямоугольной')


def transpose(mat: list[list[float | int]]) -> list[list]:
    check_matrix(mat)

    if not mat:
        return []

    result = []

    for j in range(len(mat[0])):
        row = []

        for i in range(len(mat)):
            row.append(mat[i][j])

        result.append(row)

    return result


def row_sums(mat: list[list[float | int]]) -> list[float]:
    check_matrix(mat)

    result = []

    for row in mat:
        total = 0

        for num in row:
            total += num

        result.append(total)

    return result


def col_sums(mat: list[list[float | int]]) -> list[float]:
    check_matrix(mat)

    if not mat:
        return []

    result = []

    for j in range(len(mat[0])):
        total = 0

        for i in range(len(mat)):
            total += mat[i][j]

        result.append(total)

    return result
