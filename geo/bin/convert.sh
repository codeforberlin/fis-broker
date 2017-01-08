#!/bin/bash

cd images
for f in *.ecw
do
    gdal_translate -co COMPRESS=JPEG -co PHOTOMETRIC=YCBCR -co TILED=YES -a_srs EPSG:31468 $f $f.gdal.tif
done

for f in *.gdal.tif
do
    gdaladdo --config COMPRESS_OVERVIEW JPEG --config PHOTOMETRIC_OVERVIEW YCBCR --config INTERLEAVE_OVERVIEW PIXEL -r average $f 2 4 8 16
done
cd ..

gdalbuildvrt -a_srs EPSG:31468 -overwrite tiles.vrt images/*.gdal.tif
