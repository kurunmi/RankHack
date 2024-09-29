#!/home/bona/ben_test_env/bin/python3

import json
import logging

from coinbase.rest import RESTClient



if __name__ == '__main__':
    benc = RESTClient()

    print(json.dumps(benc.get_accounts()))