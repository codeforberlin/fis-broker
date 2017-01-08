#!/bin/bash

cd images
gdal_translate -of GTiff -a_srs EPSG:3068 \
  -gcp 0    0    21600 23820 \
  -gcp 0    7905 21600 17120 \
  -gcp 8547 0    28400 23820 \
  -gcp 8547 7905 28400 17120 \
  Berlin\ um\ 1750\ entz.tif Berlin1750.tmp.tif

gdalwarp -s_srs EPSG:3068 -t_srs EPSG:3068 -r bilinear -srcnodata 0 -dstalpha \
  Berlin1750.tmp.tif Berlin1750.gdal.tif
cd ..

gdalbuildvrt -a_srs EPSG:3068 -overwrite tiles.vrt images/Berlin1750.gdal.tif
