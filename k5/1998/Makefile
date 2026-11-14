SHELL := /bin/bash
NUM_THREADS := 4
ZIP_FILE := 1998.zip
WIDTH_THRESHOLD := 8000

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
	for f in tif/*.tif; do \
		tfw="$${f%.tif}.tfw"; \
		width=$$(gdalinfo "$$f" | sed -n 's/^Size is \([0-9]*\),.*/\1/p'); \
		if [ "$$width" -lt $(WIDTH_THRESHOLD) ]; then \
			sed -i '' 's/211666666667/4233520021175/g' "$$tfw"; \
		else \
			sed -i '' 's/211666666667/3175017502954086/g' "$$tfw"; \
		fi; \
	done

clean:
	rm -r tif

dist-clean:
	rm -r cog tif tiles.vrt

.PHONY: clean dist-clean
