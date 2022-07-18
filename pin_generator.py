import random

def pin_generator(n: int):
    pin_list = []

    while len(pin_list) < n:
        check = True        
        
        while check:
            pin_gen = random.randint(1010,9090) # Create random pin code
            
            for i in range(len(str(pin_gen))):  # Check for different two near numbers
                if str(pin_gen)[i-1] == str(pin_gen)[i]:
                    check = False
                    break
            if check:
                pin_list.append(pin_gen)    
    
    for pin in pin_list:
        yield pin

amount_of_pin = int(input('How many pin codes do you need? '))
next_pin = pin_generator(amount_of_pin)

while amount_of_pin > 0:
    cmd = input('PUSH!')

    if cmd == '':
        print(next(next_pin))
        amount_of_pin -= 1
        if amount_of_pin == 0:
            print('Finish generating pin codes!') 
    else:
        print("I don't understand your command... Just PUSH" ) 