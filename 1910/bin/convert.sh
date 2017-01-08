#!/bin/bash

cd images
gdal_translate -a_srs EPSG:3068 Berlin_1910.TIF Berlin_1910.TIF.gdal.tif
cd ..

gdalbuildvrt -a_srs EPSG:3068 -overwrite tiles.vrt images/*.gdal.tif
