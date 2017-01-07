#!/bin/bash

gdalbuildvrt -a_srs EPSG:31468 -overwrite tiles.vrt images/*.tif
