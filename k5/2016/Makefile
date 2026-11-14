SHELL := /bin/bash
NUM_THREADS := 4
ZIP_FILE := TIFF_F_2016.zip
GDAL_ECW := ~/code/maps/gdal-ecw-docker/bin/gdal-ecw

tiles.vrt: cog
	gdalbuildvrt -addalpha -a_srs EPSG:25833 tiles.vrt cog/*.tif

cog: ecw
	mkdir -p cog;
	for input in ecw/*.ecw; do \
		output=cog/`basename $${input%.ecw}.tif`; \
		$(GDAL_ECW) gdal_translate $$input $$output \
			-of COG -b 1 -b 2 -b 3 -a_srs EPSG:25833 \
			-co COMPRESS=JPEG -co QUALITY=75 -co BLOCKSIZE=512 \
			-co OVERVIEWS=IGNORE_EXISTING -co NUM_THREADS=$(NUM_THREADS); \
	done

ecw:
	unzip $(ZIP_FILE) -d ecw
	for f in ../2017/tif/*.tfw; do cp "$$f" "ecw/$$(basename "$${f%.tfw}").wld"; done

clean:
	rm -r ecw

dist-clean:
	rm -r cog tif tiles.vrt

.PHONY: clean dist-clean
