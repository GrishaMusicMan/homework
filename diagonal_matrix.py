n, m = [int(i) for i in input().split()]
matrix = [[0]*m for i in range(n)]
count = 1

for i in range(m+1):
	for j in range(i):
		for k in range(i):
			if j+k == i-1 and j < n:
				matrix[j][k] = count
				count += 1


for i in matrix:
	print(*i)