SHELL := /bin/bash

tiles.vrt: cog
	gdalbuildvrt -addalpha -a_srs EPSG:25833 tiles.vrt cog/*.tif

cog: tif
	mkdir -p cog;
	gdal_translate tif/Berlin_1650.tif cog/Berlin_1650.tif \
		-of COG -co OVERVIEWS=IGNORE_EXISTING \
		-co COMPRESS=JPEG -co QUALITY=75 -co BLOCKSIZE=512

tif: zip
	unzip zip/Berlin1650.zip -d tif

zip:
	wget https://fbinter.stadt-berlin.de/fb/atom/Berlin_um/Berlin1650.zip -P zip

clean:
	rm -r tif

dist-clean:
	rm -r cog tif zip tiles.vrt

.PHONY: clean dist-clean
