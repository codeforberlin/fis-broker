#!/bin/bash

cd images
gdal_translate -a_srs EPSG:3068 Berlin_1940.tif Berlin_1940.tif.gdal.tif
cd ..

gdalbuildvrt -a_srs EPSG:3068 -overwrite tiles.vrt images/*.gdal.tif
