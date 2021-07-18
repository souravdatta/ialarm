#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 10:56:22 2021

@author: sourav
"""

import os
import time

import requests


def beep(secs, freq=440):
    os.system('play -nq -t alsa synth {} sine {}'.format(secs, freq))


def raise_blocking_alarm():
    freq = 440
    for i in range(6):
        beep(0.2, freq=freq)
        time.sleep(0.4)
        freq += 2


def ping_endpoint(url='http://www.google.co.in'):
    try:
        r = requests.get(url, timeout=1)
        if r.ok:
            print('{} -- connection fine'.format(time.time()))
    except BaseException as error:
        print(error)
        raise_blocking_alarm()


def ping_loop():
    while True:
        ping_endpoint()
        time.sleep(1)


if __name__ == '__main__':
    ping_loop()
