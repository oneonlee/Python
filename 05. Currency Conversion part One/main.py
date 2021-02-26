import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

result=requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

tbody = soup.tbody
tr = tbody.find_all('tr')
element = tbody.find_all('td')

country_list=[]
currency_list=[]
code_list=[]
number_list=[]

for i in range(len(element)):
  if i%4 == 0:
    country_list.append(" ".join(element[i].string.split()))
  elif i%4 == 1:
    currency_list.append(element[i].string)
  elif i%4 == 2:
    code_list.append(element[i].string)
  elif i%4 == 3:
    number_list.append(element[i].string)

print("Hello! Please choose select a country by number : \n")
for i in range(len(country_list)):
  print(f"#{i} {country_list[i]}")

while True:
  try:
    user_input = int(input("#: "))
    print(f"You choose {country_list[user_input]}.")
    print(f"The currency code is {code_list[user_input]}")
    break
  except ValueError:
    print("That wasn't a number.")
  except IndexError:
    print("Choose a number from the list.")
