SHELL := /bin/bash
NUM_THREADS := 4
ZIP_FILE := 1996.zip

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
	for f in tif/*.TIF; do mv "$$f" "tif/$$(basename "$${f%.TIF}").tif"; done
	sed -i '' 's/211666666667/4233520021175/g' tif/*.tfw

clean:
	rm -r tif

dist-clean:
	rm -r cog tif tiles.vrt

.PHONY: clean dist-clean
