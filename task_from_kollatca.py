import time
number = 1000000

count_of_termin = []

start_time = time.time()

# def chet(n):
#   return n/2

# def notchet(n):
#   return n*3+1

for i in range(1, number):
  counter = []

  def karusel(x): 
     
    x = [x*3+1,x/2][x % 2 == 0]
    counter.append(None)


    if x == 1:
      return len(counter)
    else:
      return karusel(x)

  count_of_termin.append(karusel(i)+1)

print(max(count_of_termin))

print(f'Время выполнения {time.time() - start_time}')


