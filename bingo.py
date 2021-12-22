# from os import system
import numpy as np
import os
import termcolor

# load bingo.csv
def load_bingo_data():
    tickets = np.zeros((0, 5, 5), dtype=np.uint8)
    with open('./bingo.csv', 'r') as f:
        row_count = 0
        for row in f:
            if len(row) > 1:
                if not row_count % 5:
                    tickets = np.append(tickets, np.zeros((1, 5, 5), dtype=np.uint8), axis=0)
                tickets[int(row_count/5)][row_count %5] = np.array(row.rstrip('\n').split(','))
                row_count += 1
    return tickets

def game():
    tickets = load_bingo_data()
    check_table = np.zeros((tickets.shape[0], 12))
    bingo_set = []

    def sum_lines(ticket_index):
        table = np.zeros(12, dtype=np.int16)
        table[:5] = np.dot(np.ones((1, 5)), tickets[ticket_index])
        table[5:10] = np.dot(np.ones((1, 5)), tickets[ticket_index].T)
        table[10] = np.sum(np.sum(np.eye(5) * tickets[ticket_index]))
        table[11] = np.sum(np.sum(np.flip(np.eye(5), axis=1) * tickets[ticket_index]))
        return table
    
    for n in range(tickets.shape[0]):
        check_table[n] = sum_lines(n)
    while True:
        try:
            num = int(input('Input : '))
            if num > 0:
                count = 0
                for n in range(tickets.shape[0]):
                    if num in tickets[n]:
                        count += 1
                    tickets[n][tickets[n] == num] = 0
                    check_table[n] = sum_lines(n)
                    if 0 in check_table[n] and n not in bingo_set:
                        print(termcolor.colored(f'ticket {n}, line {np.where(check_table[n] == 0)[0]} bingo!!!', 'red', attrs=['bold']))
                        print(tickets[n])
                        bingo_set.append(n)
                print(termcolor.colored(f'{count} tickets has number {num}' if count else '', 'yellow'))
        except KeyboardInterrupt:
            print('shutdown')
            break
        except ValueError:
            print('integer only !')

if __name__ == "__main__":
    game()
