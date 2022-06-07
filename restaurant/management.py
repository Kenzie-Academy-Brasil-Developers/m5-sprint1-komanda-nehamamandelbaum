
from restaurant.menu import AVAILABLE_MENU

def get_item(item_id: int):
    for item in AVAILABLE_MENU:
        if item["id"] == item_id:
            return item




def add_item_to_tab(table_tab, item_id, amount):
    item = get_item(item_id)

    if (not item):
        print(f'{item_id} não é um item válido!')
        return False
    
    table_tab.append({'id': item['id'], 'name': item['name'], 'price': item['price'], 'amount': amount})
    print(f' \n {amount} {item["name"]} adicionado(s) a comanda!')
    return True


def calculate_tab(table_tab):
    total = 0
    for item in table_tab:
        total = total + float(item['price'])*float(item['amount'])
    
    return total