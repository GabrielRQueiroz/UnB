def order_by_col(matrix, col: int = 0) -> list:

    matrix.sort(key=lambda row: sum(row))

    matrix.sort(key=lambda row: row[col])

    return matrix
