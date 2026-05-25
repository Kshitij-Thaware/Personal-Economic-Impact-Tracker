from twelvedata import TDClient

API_KEY = "c70cf23a77e849ee801b4e3cde75185a"

td = TDClient(apikey=API_KEY)

def get_market_data():

    nifty = td.price(
        symbol = "NIFTY",
        exchange = "NSE"
    ).as_json()

    usd_inr = td.price(
        symbol = "USD/INR"
    ).as_json()

    gold = td.price(
        symbol = "XAU/USD"
    ).as_json()


    return {
        "NIFTY": round(float(nifty["price"]), 2),
        "USD/INR": round(float(usd_inr["price"]), 2),
        "GOLD": round(float(gold["price"]), 2)
    }