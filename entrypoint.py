#!/usr/bin/env python

import os
import sys
import argparse
import warnings
from selenium.webdriver.edge.options import Options
from selenium import webdriver

from func import run

warnings.filterwarnings('ignore')


def sys_path(browser):
    path = f'./{browser}/bin/'
    if sys.platform.startswith('win'):
        return path + f'{browser}.exe'
    elif sys.platform.startswith('linux'):
        return path + f'{browser}'
    elif sys.platform.startswith('darwin'):
        return path + f'{browser}'
    else:
        raise Exception('暂不支持该系统')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('username', type=str)
    parser.add_argument('password', type=str)
    parser.add_argument('campus', type=str)
    parser.add_argument('reason', type=str)
    parser.add_argument('in_habitation', type=str)
    parser.add_argument('in_district', type=str)
    parser.add_argument('in_street', type=str)
    parser.add_argument('out_destination', type=str)
    parser.add_argument('out_track', type=str)
    parser.add_argument('wechat', type=str)
    parser.add_argument('sckey', type=str)
    args = parser.parse_args()

    print('Driver Launching...')
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver_pjs = webdriver.edge(
            options=chrome_options,
            executable_path=sys_path(browser="msedgedriver"),
            service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
    print('Driver Launched\n')

    run(driver_pjs, args.username, args.password, args.campus, args.reason,
        args.out_destination, args.out_track,
        args.in_habitation, args.in_district, args.in_street, False, '',
        eval(args.wechat), args.sckey)

    driver_pjs.quit()
