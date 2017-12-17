from bittrex.bittrex import Bittrex, API_V2_0
from datetime import datetime
import time
from pyq import q, K

get_bittrex = Bittrex(None, None)
starttime = time.time()

q.load(':alpha')

while True:
    market_result = get_bittrex.get_market_summaries()['result']
    for res in market_result:
        market_name = res['MarketName']
        ask = float(res['Ask'])
        bid = float(res['Bid'])
        last = float(res['Last'])
        volume = float(res['Volume'])
        if market_name in ['USDT-BTC', 'USDT-ETH', 'USDT-LTC', 'USDT-XRP', 'USDT-NEO', 'USDT-BCC', 'USDT-ZEC', 'USDT-XMR', 'USDT-DASH']:
            dT = datetime.fromtimestamp(time.time())
            data = [market_name[5:], ask, bid, last, volume, dT]
            q.upsert(':alpha', [data])
            q.get(':alpha').show()
    time.sleep(60.0)
