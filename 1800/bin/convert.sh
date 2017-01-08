#!/bin/bash

cd images
gdal_translate -of GTiff -a_srs EPSG:3068 \
  -gcp 0    0    21600 23820 \
  -gcp 0    7912 21600 17120 \
  -gcp 8548 0    28400 23820 \
  -gcp 8548 7912 28400 17120 \
  Berlin\ um\ 1800\ entz.tif Berlin1800.tmp.tif

gdalwarp -s_srs EPSG:3068 -t_srs EPSG:3068 -r bilinear -srcnodata 0 -dstalpha \
  Berlin1800.tmp.tif Berlin1800.gdal.tif
cd ..

gdalbuildvrt -a_srs EPSG:3068 -overwrite tiles.vrt images/Berlin1800.gdal.tif
