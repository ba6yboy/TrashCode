import requests
from bs4 import BeautifulSoup
import time 
import random
import ast

total_money = 400.0
limit = 20
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

tokens = {'cardano': 0,
        'tether': 0,
        'xrp': 0,
        'solana': 0,
        'polkadot': 0,
        'dogecoin': 0,
        'avalanche': 0,
        'uniswap': 0}


def get_money():
    global total_money
    global limit
    global tokens

while total_money < 500:
        rand_item = random.randrange(0, 7)
        item_list = tokens.keys()
        sale = random.randint(0, 1)
        rand_token = list(item_list)[rand_item]
        token_counter = 0

        token = "http://ru.investing.com/crypto/" + rand_token
        full_page = requests.get(token, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        price = soup.findAll("span", {"id": "last_last"})

        print("Общая сумма: $" + str(total_money) + "\n")

        try:
            print(rand_token.title() + ': $' + price[0].text + "\n")
        except IndexError:
            print("Сбой!\n\n")
            continue 

        token_price = price[0].text
        
        token_price = token_price.replace(',', '.')
        token_price = eval(token_price)

        if sale == 1:
            print("Покупка\n")
            if total_money < limit:
                print("Нехватает средств\n\n")
                continue
            token_counter = float(limit)/token_price
            print("Куплено " + str(token_counter) + " токен(ов)\n\n")
            tokens.update({rand_token: token_counter})
            total_money -= limit
            time.sleep(10)
        else:
            print("Продажа\n")
            if tokens.get(rand_token) != 0:
                total_money += tokens.get(rand_token) * token_price
                print("Продано токенов на $" + str(tokens.get(rand_token) * token_price) + "\n\n")
                tokens.update({rand_token: 0})
                time.sleep(10)
            else:
                print("Нет токенов\n\n")
                time.sleep(10)
get_money()

