SHELL:=/bin/bash

tiles.vrt: cog
	gdalbuildvrt -addalpha -a_srs EPSG:25833 tiles.vrt cog/*.tif

cog: tif
	mkdir -p cog;
	for input in tif/*.tif; do \
		output=cog/`basename $$input`; \
		gdal_translate $$input $$output -of COG -a_srs EPSG:25833 \
		                                -co COMPRESS=JPEG -co QUALITY=75 -co BLOCKSIZE=512 \
		                                -co OVERVIEWS=IGNORE_EXISTING; \
	done

tif: zip
	unzip zip/Straubeplan.zip -d tif

zip:
	wget 	https://fbinter.stadt-berlin.de/fb/atom/Straubeplan/Straubeplan.zip -P zip

clean:
	rm -r tif

dist-clean:
	rm -r cog tif zip tiles.vrt

.PHONY: clean dist-clean
