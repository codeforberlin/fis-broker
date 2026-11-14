SHELL := /bin/bash
NUM_THREADS := 4
ZIP_FILE := 2001-tif.zip

tiles.vrt: cog
	gdalbuildvrt -addalpha -a_srs EPSG:3068 tiles.vrt cog/*.tif

cog: tif
	mkdir -p cog;
	for input in tif/*.tif; do \
		output=cog/`basename $$input`; \
		gdal_translate $$input $$output \
			-of COG -expand gray -ot Byte -a_srs EPSG:3068 \
			-co COMPRESS=DEFLATE -co PREDICTOR=2 -co BLOCKSIZE=512 -co RESAMPLING=AVERAGE \
			-co OVERVIEWS=IGNORE_EXISTING -co NUM_THREADS=$(NUM_THREADS); \
	done

tif:
	unzip $(ZIP_FILE) -d tif

clean:
	rm -r tif

dist-clean:
	rm -r cog tif tiles.vrt

.PHONY: clean dist-clean
