def get_matrix():
    matrix = []
    for i in range(5):
        x = list(map(int, input().split()))
        matrix.append(x)
    return  matrix


def count_moves(matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                target = (i+1,j+1)

    center = (3,3)
    count = abs(center[0]-target[0]) + abs(center[1]-target[1])
    return count

def main():
    matrix = get_matrix()
    count = count_moves(matrix)
    print(count)

main()