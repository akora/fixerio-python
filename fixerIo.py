#!/usr/bin/python

# Fixer.io is a free JSON API for current and historical foreign exchange rates.
# It relies on daily feeds published by the European Central Bank.

import sys
import requests

base_url = 'http://api.fixer.io/latest'
base_currencies = ['GBP', 'USD', 'EUR']
rate_in = 'HUF'


def get_currency_rate(currency, rate_in):
  query = base_url + '?base=%s&symbols=%s' % (currency, rate_in)
  try:
    response = requests.get(query)
    # print("[%s] %s" % (response.status_code, response.url))
    if response.status_code != 200:
      response = 'N/A'
      return response
    else:
      rates = response.json()
      rate_in_currency = rates["rates"][rate_in]
      return rate_in_currency
  except requests.ConnectionError as error:
    print error
    sys.exit(1)


def main():
  for currency in base_currencies:
    rate = get_currency_rate(currency, rate_in)
    print currency, rate

if __name__ == '__main__':
  main()
