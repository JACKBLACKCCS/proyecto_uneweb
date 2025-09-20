# cart/utils.py
EXCHANGE_RATES = {
    'USD': 1,          # moneda base
    'EUR': 0.93,       # 1 USD = 0.93 EUR
    'COP': 4900,       # 1 USD = 4900 COP
    'BTC': 0.000043    # 1 USD = 0.000043 BTC
}

def convert_price(price, currency):
    rate = EXCHANGE_RATES.get(currency, 1)
    return round(price * rate, 2)
