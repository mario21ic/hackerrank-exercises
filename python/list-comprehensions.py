"""
input:
1
1
1
2
expected:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # generar matriz
    permutations = [[i, j, k] for k in range(z+1) for j in range(y+1) for i in range(x+1)]
    # print(permutations)
    # Excluir cuando la suma sea igual a n
    result = [r for r in permutations if sum(r) != n]
    print(sorted(result))

