SHELL:=/bin/bash

tiles.vrt: tif
	gdalbuildvrt -a_srs EPSG:25833 tiles.vrt tif/*.tif

tif:
	mkdir tif
	cd tif-large; \
	for f in *.tif; do \
		gdal_translate -co COMPRESS=JPEG -co TILED=YES -a_srs EPSG:25833 $$f ../tif/$$f; \
	done
	for f in tif/*.tif; do \
		gdaladdo --config COMPRESS_OVERVIEW JPEG --config INTERLEAVE_OVERVIEW PIXEL -r average $$f 2 4 8 16; \
	done

ecw: zip
	for f in zip/*.zip; do unzip $$f -d ecw; done

zip:
	for url in \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2023/Mitte.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2023/Nord.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2023/Nordost.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2023/Nordwest.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2023/Ost.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2023/Sued.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2023/Suedost.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2023/Suedwest.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2023/West.zip'; \
	do wget $$url -P zip; \
	done

clean:
	rm -rf zip ecw tif tiles.vrt

.PHONY: clean
