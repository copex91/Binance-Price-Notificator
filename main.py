#!/usr/bin/env python
# -*- coding: utf-8 -*-
from binance.client import Client
from binance.websockets import BinanceSocketManager


def process_message(msg):
    print("message type: {}".format(msg))
    print(msg)
    # do something


if __name__ == '__main__':
    client = Client('','')
    bm = BinanceSocketManager(client)
    bm.start_ticker_socket(process_message)
    bm.start()