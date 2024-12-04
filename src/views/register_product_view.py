import os
from typing import Dict

def register_product() -> Dict:
    os.system("cls||clear")
    message = f'''
======= CADASTRAR PRODUTO ========
    '''

    print(message)
    name = str(input("Digite o nome do produto: "))
    price = float(input("Digite o preço do produto: "))
    quantity = int(input("Digite a quantidade do produto em estoque: "))
    

    info_register_product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    return info_register_product