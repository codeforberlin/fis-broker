SHELL:=/bin/bash

tiles.vrt: tif
	gdalbuildvrt -a_srs EPSG:25833 tiles.vrt tif/*.tif

tif: tmp
	mkdir tif
	cd tmp; \
	for f in *.tif; \
	do gdal_translate -co COMPRESS=JPEG -co TILED=YES -a_srs EPSG:25833 $$f ../tif/$$f; \
	done
	for f in tif/*.tif; \
	do gdaladdo --config COMPRESS_OVERVIEW JPEG --config PHOTOMETRIC_OVERVIEW YCBCR --config INTERLEAVE_OVERVIEW PIXEL -r average $$f 2 4 8 16; \
	done

tmp: zip
	unzip zip/Berlin1750.zip -d tmp

zip:
	wget https://fbinter.stadt-berlin.de/fb/atom/Berlin_um/Berlin1750.zip -P zip

clean:
	rm -rf zip tmp

.PHONY: clean
