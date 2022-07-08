n, m = [int(i) for i in input().split()]
matrix = [[0]*m for i in range(n)]
count = 1

for i in range(m + n):
	for j in range(i):
		for k in range(i):
			if j + k == i - 1 and j < n and k < m:
				matrix[j][k] = count
				count += 1

for row in matrix:
	for el in row:
		print(str(el).ljust(3), end=' ')
	print()