#!/bin/bash

cd images
gdal_translate -of GTiff -a_srs EPSG:3068 \
  -gcp 0 0 23100 22600 \
  -gcp 0 3511 23100 19600 \
  -gcp 3678 0 26300 22600 \
  -gcp 3678 3511 26300 19600 \
  Berlin\ um\ 1650\ entz.tif Berlin1650.tmp.tif

gdalwarp -s_srs EPSG:3068 -t_srs EPSG:3068 -r bilinear -srcnodata 0 -dstalpha \
  Berlin1650.tmp.tif Berlin1650.gdal.tif
cd ..

gdalbuildvrt -a_srs EPSG:3068 -overwrite tiles.vrt images/Berlin1650.gdal.tif
