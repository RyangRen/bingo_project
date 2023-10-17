import numpy as np
try:
    ticket_num = int(input('Input number of tickets : '))
except TypeError:
    ticket_num = 0

with open('bingo.csv', 'w') as file:
    for i in range(ticket_num):
        num_list = []
        count = 1
        while count < 26:
            num = np.random.randint(1, 100)
            if num not in num_list:
                num_list.append(num)
                file.write(f'{num},' if count%5 else f'{num}\n')
                count += 1
        file.ilewrite('\n')
