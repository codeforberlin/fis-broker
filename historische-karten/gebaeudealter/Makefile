SHELL := /bin/bash

tiles.vrt: cog
	gdalbuildvrt -addalpha -a_srs EPSG:25833 tiles.vrt cog/*.tif

cog: tif
	mkdir -p cog;
	gdal_translate tif/Gebaeudealter_1992_93.tif cog/Gebaeudealter_1992_93.tif \
		-of COG -expand rgb -co OVERVIEWS=IGNORE_EXISTING \
		-co COMPRESS=JPEG -co QUALITY=75 -co BLOCKSIZE=512

tif: zip
	unzip zip/Gebaeudealter_1992_93.zip -d tif
	mv tif/*.tfw tif/Gebaeudealter_1992_93.tfw
	mv tif/*.tif tif/Gebaeudealter_1992_93.tif

zip:
	wget https://fbinter.stadt-berlin.de/fb/atom/Berlin_um/Gebaeudealter_1992_93.zip -P zip

clean:
	rm -r tif

dist-clean:
	rm -r cog tif zip tiles.vrt

.PHONY: clean dist-clean
