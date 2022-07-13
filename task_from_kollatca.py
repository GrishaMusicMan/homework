import time

number = 1_000_000
count_of_termin = []
start_time = time.time()
count_of_termin_dict = {}

for i in range(1, number)[-1:int(number - (number/5)):-1]:

  counter = []

  def karusel(x): 
     
    x = [x * 3 + 1, x / 2][x % 2 == 0]
    counter.append(None)

    if x == 1:
      return len(counter)+1
    else:
      return karusel(x)

  count_of_termin_dict[karusel(i)] = i

print(f'Число - {count_of_termin_dict[max(count_of_termin_dict)]} терминов - {max(count_of_termin_dict)}')
print(f'Время выполнения {time.time() - start_time}')

