#!/bin/bash

gdalbuildvrt -a_srs EPSG:25833 -overwrite tiles.vrt images/*.tif
