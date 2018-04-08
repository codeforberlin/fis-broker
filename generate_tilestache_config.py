#!/usr/bin/env python3

import argparse
import json

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

PREFIX = 'berlin-'

PREVIEW = {
    'lat': 52.518611,
    'lon': 13.408333,
    'zoom': 15
}

data = {
    'cache': {
        'name': 'Multi',
        'tiers': [
            {
                'name': 'Memcache',
                'servers': ['127.0.0.1:11211']
            },
            {
                'name': 'Disk',
                'path': '/tmp/tilestache'
            }
        ]
    },
    'layers': {}
}

parser = argparse.ArgumentParser()
parser.add_argument('path', help='base path to the files')

args = parser.parse_args()

for directory in DIRECTORIES:
    layer = PREFIX + directory

    data['layers'][layer] = {
        'provider': {
            'class': 'TileStache.Goodies.Providers.GDAL:Provider',
            'kwargs': {
                'filename': args.path + '1650/tiles.vrt',
                'maskband': 1
            }
        },
        'preview': PREVIEW
    }

print(json.dumps(data, sort_keys=True, indent=4))
