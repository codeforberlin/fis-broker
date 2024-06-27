SHELL:=/bin/bash

tiles.vrt: tif
	gdalbuildvrt -a_srs EPSG:25833 tiles.vrt tif/*.tif

tif: jp2
	mkdir tif
	cd jp2; \
	for f in *.jp2; do \
		gdal_translate -co COMPRESS=JPEG -co TILED=YES -a_srs EPSG:25833 $$f ../tif/$${f%.jp2}.tif; \
	done
	for f in tif/*.tif; do \
		gdaladdo --config COMPRESS_OVERVIEW JPEG --config INTERLEAVE_OVERVIEW PIXEL -r average $$f 2 4 8 16; \
	done

jp2: zip
	for f in zip/*.zip; do unzip $$f -d jp2; done
	mv jp2/Mitte/* jp2/.
	rm -r jp2/Mitte

zip:
	for url in \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2024/Mitte.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2024/Nord.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2024/Nordost.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2024/Nordwest.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2024/Ost.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2024/Sued.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2024/Suedost.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2024/Suedwest.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2024/West.zip'; \
	do wget $$url -P zip; \
	done

clean:
	rm -rf zip jp2 tiles.vrt

.PHONY: clean
