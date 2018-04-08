#!/usr/bin/env python3

import argparse
import subprocess

DIRECTORIES = [
    '1650',
    '1690',
    '1750',
    '1800',
    '1850',
    '1880',
    '1910',
    '1928',
    '1940',
    '1953',
    '1986',
    '2004',
    '2007',
    '2010',
    '2014',
    '2016',
    '2016i',
    '2017',
    'gebaeudealter',
    'gebschaden',
    'geo',
    'hobrecht',
]

parser = argparse.ArgumentParser()
parser.add_argument('destination')

args = parser.parse_args()

destination = args.destination.rstrip('/')

for directory in DIRECTORIES:
    for source, target in [
        (directory + '/images/', destination + '/' + directory + '/images/'),
        (directory + '/tiles.vrt', destination + '/' + directory + '/tiles.vrt')
    ]:
        subprocess.check_call([
            'rsync',
            '--delete',
            '-av',
            '--include=*.gdal.tif',
            '--exclude=*',
            source,
            target
        ])
