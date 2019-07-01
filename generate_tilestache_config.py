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
    '2018',
    '2019',
    'gebaeudealter',
    'gebschaden',
    'hobrecht',
]

PREVIEW = {
    'lat': 52.518611,
    'lon': 13.408333,
    'zoom': 15
}

parser = argparse.ArgumentParser()
parser.add_argument('path', help='base path to the files')
parser.add_argument('-p', '--prefix', help='prefix for the layers')
parser.add_argument('-o', '--output', help='name of the config file',
                    default='tilestache.cfg')

args = parser.parse_args()

path = args.path.rstrip('/')
prefix = args.prefix or None

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
                'path': '/tmp/cache'
            }
        ]
    },
    'layers': {}
}

for directory in DIRECTORIES:
    if prefix:
        layer = prefix + directory
    else:
        layer = directory

    data['layers'][layer] = {
        'provider': {
            'class': 'TileStache.Goodies.Providers.GDAL:Provider',
            'kwargs': {
                'filename': path + '/' + directory + '/tiles.vrt',
                'maskband': 1
            }
        },
        'preview': PREVIEW
    }

with open(args.output, 'w') as f:
    f.write(json.dumps(data, sort_keys=True, indent=4))
