
from restaurant.management import add_item_to_tab, calculate_tab
import os

TABLE_TAB = []

def initial_screen():
    os.system('clear')
    while True: 
        print('Selecione a opção desejada: \n')
        print('1. Adicionar item à comanda')
        print('2. Fechar a comanda \n')

        answer = input('Digite o que deseja fazer:')

        if answer == '1':
            
            add_item_screen()
            
            
        elif answer == '2':
           check_out_screen()
           return False
            
            
        else:
            os.system('clear')
            print('Digite uma opção válida!')
            
            


def add_item_screen():
    os.system('clear')

    print('Digite as informações do item desejado: ')

    item_id = input('Digite o id do item:')
    amount = input('Digite a quantidade desejada:')

    add_item_to_tab(TABLE_TAB, int(item_id), amount)

    if (not add_item_to_tab):
        print(f'{item_id} não é um item válido!')

    

    
def check_out_screen(): 
    os.system('clear')
    while True:
        for item in TABLE_TAB:   
            print(f'Item {TABLE_TAB.index(item)+1}: {item["amount"]} {item["name"]} - R${item["price"] * int(item["amount"])}')

        print('-'*50)
        print(f'Total: R${calculate_tab(TABLE_TAB):.2f} \n\n\n\n')
        close = input('Digite F para finalizar o sistema \n')

        if (close == 'f' or close == 'F'):
            return False
    



