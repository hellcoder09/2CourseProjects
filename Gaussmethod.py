myA = [
    [2.0, 1.0, 1.0],
    [1.0, -1.0, 0.0],
    [3.0, -1.0, 2.0]
]

myB = [
    2.0,
    -2.0,
    2.0
]


def FancyPrint(A, B, selected):
    for row in range(len(B)):
        print("(", end='')
        for col in range(len(A[row])):
            print("\t{1:10.2f}{0}".format(" " if (selected is None or selected != (row, col)) else "*", A[row][col]),
                  end='')
        print("\t) * (\tX{0}) = (\t{1:10.2f})".format(row + 1, B[row]))


def SwapRows(A, B, row1, row2):
    A[row1], A[row2] = A[row2], A[row1]
    B[row1], B[row2] = B[row2], B[row1]


def DivideRow(A, B, row, divider):
    A[row] = [a / divider for a in A[row]]
    B[row] /= divider


def CombineRows(A, B, row, source_row, weight):
    A[row] = [(a + k * weight) for a, k in zip(A[row], A[source_row])]
    B[row] += B[source_row] * weight


def Gauss(A, B):
    column = 0
    while (column < len(B)):

        current_row = None
        for r in range(column, len(A)):
            if current_row is None or abs(A[r][column]) > abs(A[current_row][column]):
                current_row = r
        if current_row is None:
            print("решений нет")
            return None

        if current_row != column:
            SwapRows(A, B, current_row, column)

        DivideRow(A, B, column, A[column][column])

        for r in range(column + 1, len(A)):
            CombineRows(A, B, r, column, -A[r][column])

        column += 1

    X = [0 for b in B]
    for i in range(len(B) - 1, -1, -1):
        X[i] = B[i] - sum(x * a for x, a in zip(X[(i + 1):], A[i][(i + 1):]))

    print("Получили ответ:")
    print("\n".join("X{0} =\t{1:10.2f}".format(i + 1, x) for i, x in enumerate(X)))

    return X


print("Исходная система:")
FancyPrint(myA, myB, None)
Gauss(myA, myB)
