#!/bin/bash

cd images
gdal_translate -of GTiff -a_srs EPSG:3068 \
  -gcp 0 0 23100 22600 \
  -gcp 0 3497 23100 19600 \
  -gcp 3662 0 26300 22600 \
  -gcp 3662 3497 26300 19600 \
  Berlin\ um\ 1690\ entz.tif Berlin1690.tmp.tif

gdalwarp -s_srs EPSG:3068 -t_srs EPSG:3068 -r bilinear -srcnodata 0 -dstalpha \
  Berlin1690.tmp.tif Berlin1690.gdal.tif
cd ..

gdalbuildvrt -a_srs EPSG:3068 -overwrite tiles.vrt images/Berlin1690.gdal.tif
