import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")
currency_url = "https://www.iban.com/currency-codes"

currency = requests.get(currency_url)
currency_soup = BeautifulSoup(currency.text, "html.parser")

tbody = currency_soup.tbody
tr = tbody.find_all('tr')
element = tbody.find_all('td')

# 번호를 맞추기 위해 [] 대신 [""] 사용
country_list = [""]
currency_list = [""]
code_list = [""]
number_list = [""]

for i in range(len(element)):
    if i % 4 == 0:
        country_list.append(" ".join(element[i].string.split()))
    elif i % 4 == 1:
        currency_list.append(element[i].string)
    elif i % 4 == 2:
        code_list.append(element[i].string)
    elif i % 4 == 3:
        number_list.append(element[i].string)

# 같은 나라의 다른 화폐 단위를 구별하기 위한 코드
for i in range(1, len(country_list)):
  if (country_list[i-1]==country_list[i]):
    country_list[i-1]=f"{country_list[i-1]} - [{currency_list[i-1]}]"
    country_list[i]=f"{country_list[i]} - [{currency_list[i]}]"
    print(country_list[i-1], country_list[i])

print("Welcome to Currency Convert PRO 2000\n")

for i in range(1, len(country_list)):
    print(f"#{i} {country_list[i]}")

print("\nWhere are you from? Choose a country by number.")
while True:
    try:
        user_num = int(input("#: "))
        if code_list[user_num] == None:
            print(
                f"Sorry. We don\'t support {country_list[user_num]}. Try another country."
            )
        else:
            print(f"You are from {country_list[user_num]}!\n")
            break
    except ValueError:
        print("That wasn't a number.")
    except IndexError:
        print("Choose a number from the list.")

print("Now, choose another country.")
while True:
    try:
        another_num = int(input("#: "))
        if code_list[another_num] == None:
            print(
                f"Sorry. We don\'t support {country_list[another_num]}. Try another country.\n"
            )
        elif (user_num == another_num):
            print("You choose the same country! Try another country.")
        else:
            print(f"You choose {country_list[another_num]}!\n")
            break
    except ValueError:
        print("That wasn't a number.")
    except IndexError:
        print("Choose a number from the list.")

print(
    f"How many {code_list[user_num]} do you want to convert to {code_list[another_num]}?"
)
while True:
    try:
        amount = int(input(f"{code_list[user_num]} Amount: "))
        exchange_url = f"https://transferwise.com/gb/currency-converter/{code_list[user_num]}-to-{code_list[another_num]}-rate?amount={amount}"
        exchange = requests.get(exchange_url)
        exchange_soup = BeautifulSoup(exchange.text, "html.parser")
        form_soup = exchange_soup.form
        input_soup = form_soup.input
        rate_value = float(input_soup['value'])

        print("\nResult:")
        print(f'{format_currency(amount, code_list[user_num], locale="ko_KR")} is {format_currency(amount * rate_value, code_list[another_num], locale="ko_KR")}')

        print("\nRate Value:")
        print(
            format_currency(1, code_list[user_num], locale="ko_KR"), "is",
            format_currency(rate_value, code_list[another_num],
                            locale="ko_KR"))
        break
    except ValueError:
        print("That wasn't a number.")
    except AttributeError:
        print("Sorry. Something Wrong. Try again.\n")
        break

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR")
"""
