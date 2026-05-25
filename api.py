from twelvedata import TDClient

API_KEY = "c70cf23a77e849ee801b4e3cde75185a"

td = TDClient(apikey=API_KEY)

def get_market_data():

    assets = {
        "APPLE": "AAPL",
        "BITCOIN": "BTC/USD",
        "USD_INR": "USD/INR",
        "GOLD": "XAU/USD"
    }

    data = {}

    for name, symbol in assets.items():

        try:
            result = td.quote(symbol=symbol).as_json()

            print(result)  # Debugging

            if "close" in result:
                data[name] = round(float(result["close"]), 2)
            else:
                data[name] = "Unavailable"

        except Exception as e:
            print(f"{name} ERROR:", e)
            data[name] = "Error"

    return data