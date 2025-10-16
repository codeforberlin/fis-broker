SHELL := /bin/bash
NUM_THREADS := 4

tiles.vrt: cog
	gdalbuildvrt -addalpha -a_srs EPSG:25833 tiles.vrt cog/*.tif

cog: tif
	mkdir -p cog;
	for input in tif/*.tif; do \
		output=cog/`basename $$input`; \
		gdal_translate $$input $$output \
			-of COG -b 1 -expand rgb -a_srs EPSG:25833 \
			-co COMPRESS=JPEG -co QUALITY=75 -co BLOCKSIZE=512 \
			-co OVERVIEWS=IGNORE_EXISTING -co NUM_THREADS=$(NUM_THREADS); \
	done

tif: zip
	for f in zip/*.zip; do \
		unzip $$f -d tif; \
	done

zip:
	wget https://fbinter.stadt-berlin.de/fb/atom/K5/sw/k5_sw.zip -P zip

clean:
	rm -r tif

dist-clean:
	rm -r cog tif zip tiles.vrt

.PHONY: clean dist-clean
