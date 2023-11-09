N = 4
def getCofactor(A, temp, p, q, n):
    i = 0
    j = 0
    for row in range(n):
        for col in range(n):
            if (row != p and col != q):
                temp[i][j] = A[row][col]
                j += 1
                if (j == n - 1):
                    j = 0
                    i += 1
def determinant(A, n):
    D = 0
    if (n == 1):
        return A[0][0]
    temp = []
    for i in range(N):
        temp.append([None for _ in range(N)])
    sign = 1
    for f in range(n):
        getCofactor(A, temp, 0, f, n)
        D += sign * A[0][f] * determinant(temp, n - 1)
        sign = -sign
    return D
def adjoint(A, adj):
    if (N == 1):
        adj[0][0] = 1
        return
    sign = 1
    temp = []
    for i in range(N):
        temp.append([None for _ in range(N)])
    for i in range(N):
        for j in range(N):
            getCofactor(A, temp, i, j, N)
            sign = [1, -1][(i + j) % 2]
            adj[j][i] = (sign)*(determinant(temp, N-1))
def inverse(A, inverse):
    det = determinant(A, N)
    adj = []
    for i in range(N):
        adj.append([None for _ in range(N)])
    adjoint(A, adj)
    for i in range(N):
        for j in range(N):
            inverse[i][j] = adj[i][j] / det
    return
def display(A):
    for i in range(N):
        for j in range(N):
            print(A[i][j], end=" ")
        print()
def displays(A):
    for i in range(N):
        for j in range(N):
            print(round(A[i][j], 6), end=" ")
        print()
A = [[5, -2, 2, 7], [1, 0, 0, 3], [-3, 1, 5, 0], [3, -1, -9, 4]]
adj = [None for _ in range(N)]
inv = [None for _ in range(N)]
for i in range(N):
    adj[i] = [None for _ in range(N)]
    inv[i] = [None for _ in range(N)]
print("Input matrix is :")
display(A)
print("\nThe Adjoint is :")
adjoint(A, adj)
display(adj)
print("\nThe Inverse is :")
inverse(A, inv)
displays(inv)
