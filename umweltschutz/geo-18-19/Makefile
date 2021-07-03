SHELL:=/bin/bash

tiles.vrt: tif
	gdalbuildvrt -a_srs EPSG:31468 tiles.vrt tif/*.tif

tif: ecw
	mkdir tif
	cd ecw; \
	for f in *.ecw; do \
		gdal_translate -co COMPRESS=JPEG -co PHOTOMETRIC=YCBCR -co TILED=YES -a_srs EPSG:31468 $$f ../tif/$${f%.ecw}.tif; \
	done
	for f in tif/*.tif; do \
		gdaladdo --config COMPRESS_OVERVIEW JPEG --config PHOTOMETRIC_OVERVIEW YCBCR --config INTERLEAVE_OVERVIEW PIXEL -r average $$f 2 4 8 16; \
	done

ecw: zip
	for f in zip/*.zip; do unzip $$f -d ecw; done

zip:
	wget https://fbinter.stadt-berlin.de/fb/atom/Geologie/geo_18-19/Geolog_Karte_gauss4.zip -P zip

clean:
	rm -rf zip ecw tif tiles.vrt

.PHONY: clean
