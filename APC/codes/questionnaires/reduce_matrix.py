def reduce_matrix(matrix, factor):
    rows = len(matrix)
    cols = len(matrix[0])

    new_matrix = [[] for i in range(rows // factor)]

    for row in range(0, rows, factor):
        for col in range(0, cols, factor):
            elements = []

            for i in range(factor):
                for j in range(factor):
                    elements.append(matrix[row + i][col + j])

            elements.sort(reverse=True)

            new_matrix[row // factor].append(elements[0])

    return new_matrix
