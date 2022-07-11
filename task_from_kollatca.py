import time
number = 1000000
counter = 0
count_of_termin = []

start_time = time.time()

def chet(n):
  return n/2

def notchet(n):
  return n*3+1

for i in range(2, number):

  while i > 1: 
    counter += 1  
    if i % 2 == 0:
      i = chet(i)      
    else:
      i = notchet(i)

  count_of_termin.append(counter+1)
  counter = 0

print(max(count_of_termin))

print(f'Время выполнения {time.time() - start_time}')


