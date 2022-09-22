def snail(snail_map):
    dx = 1  # -1, 0, 1
    dy = 0  # -1, 0, 1
    i = 0
    j = -1

    result = []

    if len(snail_map) == 1 and not snail_map[0]:
        return result

    while len(result) != len(snail_map) * len(snail_map):

        if 0 <= i + dy < len(snail_map) and 0 <= j + dx < len(snail_map) and snail_map[i + dy][j + dx] != 0:

            i += dy
            j += dx
            result.append(snail_map[i][j])
            snail_map[i][j] = 0

        else:
            if dx == 1:
                dx = 0
                dy = 1
            elif dy == 1:
                dy = 0
                dx = -1
            elif dx == -1:
                dx = 0
                dy = -1
            elif dy == -1:
                dy = 0
                dx = 1

    return result


array_1 = [[]]

array_2 = [[1, 2, 3],
           [8, 9, 4],
           [7, 6, 5]]

print(snail(array_1))
print(snail(array_2))
