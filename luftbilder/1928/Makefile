SHELL := /bin/bash
NUM_THREADS := 4

export PATH := /opt/gdal-3.4.1/bin/:$(PATH)
export LD_LIBRARY_PATH := /opt/hexagon/ERDAS-ECW_JPEG_2000_SDK-5.5.0/Desktop_Read-Only/lib/cpp11abi/x64/release/

tiles.vrt:
	gdalbuildvrt -a_srs EPSG:25833 tiles.vrt cog/*.tif

cog: ecw.vrt
	python convert.py

ecw.vrt: ecw
	gdalbuildvrt -a_srs EPSG:25833 ecw.vrt ecw/*.tif

ecw: zip
	for f in zip/*.zip; do \
		unzip $$f -d ecw; \
	done

zip:
	for url in \
			'https://fbinter.stadt-berlin.de/fb/atom/luftbilder/1928/Mitte.zip' \
			'https://fbinter.stadt-berlin.de/fb/atom/luftbilder/1928/Nord.zip' \
			'https://fbinter.stadt-berlin.de/fb/atom/luftbilder/1928/Nordost.zip' \
			'https://fbinter.stadt-berlin.de/fb/atom/luftbilder/1928/Nordwest.zip' \
			'https://fbinter.stadt-berlin.de/fb/atom/luftbilder/1928/Ost.zip' \
			'https://fbinter.stadt-berlin.de/fb/atom/luftbilder/1928/Sued.zip' \
			'https://fbinter.stadt-berlin.de/fb/atom/luftbilder/1928/Suedost.zip' \
			'https://fbinter.stadt-berlin.de/fb/atom/luftbilder/1928/Suedwest.zip' \
			'https://fbinter.stadt-berlin.de/fb/atom/luftbilder/1928/West.zip'; \
		do wget $$url -P zip; \
	done

clean:
	rm -r ecw

dist-clean:
	rm -r cog ecw zip tiles.vrt

.PHONY: clean dist-clean
