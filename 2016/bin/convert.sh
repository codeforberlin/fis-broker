#!/bin/bash

cd images
for f in *.ecw
do
    gdal_translate -co COMPRESS=JPEG -co PHOTOMETRIC=YCBCR -co TILED=YES -a_srs EPSG:25833 $f $f.tif
done

for f in *.tif
do
    gdaladdo --config COMPRESS_OVERVIEW JPEG --config PHOTOMETRIC_OVERVIEW YCBCR --config INTERLEAVE_OVERVIEW PIXEL -r average $f 2 4 8 16
done
cd ..
