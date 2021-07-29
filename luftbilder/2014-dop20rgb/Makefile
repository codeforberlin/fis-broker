SHELL:=/bin/bash

tiles.vrt: tif
	gdalbuildvrt -a_srs EPSG:25833 tiles.vrt tif/*.tif

tif: ecw
	mkdir tif
	cd ecw; \
	for f in *.ecw; \
	do gdal_translate -co COMPRESS=JPEG -co PHOTOMETRIC=YCBCR -co TILED=YES -a_srs EPSG:25833 $$f ../tif/$${f%.ecw}.tif; \
	done
	for f in tif/*.tif; \
	do gdaladdo --config COMPRESS_OVERVIEW JPEG --config PHOTOMETRIC_OVERVIEW YCBCR --config INTERLEAVE_OVERVIEW PIXEL -r average $$f 2 4 8 16; \
	done

ecw: zip
	for f in zip/*.zip; do unzip $$f -d ecw; done

zip:
	for url in \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20c_2014/Mitte.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20c_2014/Nord.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20c_2014/Nordost.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20c_2014/Nordwest.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20c_2014/Ost.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20c_2014/Sued.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20c_2014/Suedost.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20c_2014/Suedwest.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20c_2014/West.zip'; \
	do wget $$url -P zip; \
	done

clean:
	rm -rf zip ecw

.PHONY: clean
