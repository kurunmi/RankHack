#!/home/bona/ben_test_env/bin/python3

import json
import logging
import time

from coinbase.rest import RESTClient
from coinbase.websocket import WSClient


mydict = {}

def print_msg(mydict, tx, px, old_px, asset, ts):
    if tx in ['up', 'down']:
        delta = abs(float(px) - float(old_px))
        print("Time: %s| Name:%s| current_price: %s| previous_price: %s| direction:%s| "
              "lowest_price: %s | lowest_time: %s | highest_price: %s| highest_time: %s widest: %f "
              "difference :%f " %
              (str(ts).ljust(32), asset.ljust(4), px.ljust(10), old_px.ljust(10),
               tx.ljust(6), mydict[asset]['min'], mydict[asset]['min_time'], mydict[asset]['max'],
               mydict[asset]['max_time'],  mydict[asset]['widest'], delta))


def on_message(msg):
    jmsg = json.loads(msg)
    try:
        if 'events' in jmsg:
            if 'tickers' in jmsg['events'][0]:
                tx = 'flat'
                old_px = False
                asset = jmsg['events'][0]['tickers'][0]['product_id']
                asset = asset.split('-')[0]
                px = jmsg['events'][0]['tickers'][0]['price']
                if asset in mydict:
                    if mydict[asset]['last'] > px:
                        tx = 'down'
                        if mydict[asset]['min'] > px:
                            mydict[asset]['min_time'] = jmsg['timestamp']
                            mydict[asset]['min'] = px
                            print(jmsg['timestamp'])
                            old_px = mydict[asset]['last']
                            print_msg(mydict,tx, px, old_px, asset, jmsg['timestamp'])
                    elif mydict[asset]['last'] < px:
                        tx = 'up'
                        if mydict[asset]['max'] < px:
                            mydict[asset]['max_time'] = jmsg['timestamp']
                            mydict[asset]['max'] = px
                            print(jmsg['timestamp'])
                            old_px = mydict[asset]['last']
                            print_msg(mydict,tx, px, old_px, asset, jmsg['timestamp'])
                    mydict[asset]['last'] = px
                    mydict[asset]['widest'] = float(mydict[asset]['max']) - float(mydict[asset]['min'])
                else:
                    mydict[asset] = {'last': px, 'max': px, 'min': px, 'max_time': jmsg['timestamp'],
                                     'min_time': jmsg['timestamp'], 'widest':0}
    except Exception as e:
        print("error: %s, %s" % (msg, e))

if __name__ == '__main__':
    client = WSClient(on_message=on_message)
    client.open()
    #client.ticker(product_ids=["BTC-USD"])
    client.subscribe(product_ids=["BTC-USD", "ETH-USD"], channels=["ticker", "heartbeats"])
    client.run_forever_with_exception_check()
    time.sleep(2)