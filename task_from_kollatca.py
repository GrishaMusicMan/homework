import time
number = 100
count_of_termin = []
start_time = time.time()

def counter(func):
    
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)    
    wrapper.count = 0
    return wrapper

def kollatca(number):
  #print(number)
  
  @counter
  def karusel(x):    
    
    def chet(x):
      return x/2
    def notchet(x):
      return x*3+1

    x = [notchet(x), chet(x)][x % 2 == 0]
    
    if x == 1:
      return karusel.count + 1
    else:
      return karusel(x)
  
  count_of_termin.append(karusel(number))

  if number == 1:
    return max(count_of_termin)
  else:
     return kollatca(number - 1)

print(kollatca(number))

print(f'Время выполнения {time.time() - start_time}')


