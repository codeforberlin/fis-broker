SHELL := /bin/bash
NUM_THREADS := 4

export PATH := /opt/gdal-3.4.1/bin/:$(PATH)
export LD_LIBRARY_PATH := /opt/hexagon/ERDAS-ECW_JPEG_2000_SDK-5.5.0/Desktop_Read-Only/lib/cpp11abi/x64/release/

tiles.vrt: cog
	gdalbuildvrt -addalpha -a_srs EPSG:31468 tiles.vrt cog/*.tif

cog: ecw
	mkdir -p cog;
	for input in ecw/*.ecw; do \
		output=cog/`basename $${input%.ecw}.tif`; \
		gdal_translate $$input $$output \
			-of COG -b 1 -b 2 -b 3 -a_srs EPSG:31468 \
			-co COMPRESS=JPEG -co QUALITY=75 -co BLOCKSIZE=512 \
			-co OVERVIEWS=IGNORE_EXISTING -co NUM_THREADS=$(NUM_THREADS); \
	done

ecw: zip
	for f in zip/*.zip; do \
		unzip $$f -d ecw; \
	done

zip:
	wget https://fbinter.stadt-berlin.de/fb/atom/Geologie/geo_18-19/Geolog_Karte_gauss4.zip -P zip

clean:
	rm -r ecw

dist-clean:
	rm -r cog ecw zip tiles.vrt

.PHONY: clean dist-clean
