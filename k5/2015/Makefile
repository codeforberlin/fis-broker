SHELL := /bin/bash
NUM_THREADS := 4
ZIP_FILE := TIFF_F_2015.zip
TFW_PATH := ../2012/tif
GDAL_ECW := ~/code/maps/gdal-ecw-docker/bin/gdal-ecw

tiles.vrt: cog
	gdalbuildvrt -addalpha -a_srs EPSG:3068 tiles.vrt cog/*.tif

cog: ecw
	mkdir -p cog;
	for input in ecw/*.ecw; do \
		output=cog/`basename $${input%.ecw}.tif`; \
		$(GDAL_ECW) gdal_translate $$input $$output \
			-of COG -b 1 -b 2 -b 3 -a_srs EPSG:3068 \
			-co COMPRESS=JPEG -co QUALITY=75 -co BLOCKSIZE=512 \
			-co OVERVIEWS=IGNORE_EXISTING -co NUM_THREADS=$(NUM_THREADS); \
	done

ecw:
	unzip $(ZIP_FILE) -d ecw
	for f in $(TFW_PATH)/*.tfw; do cp "$$f" "ecw/$$(basename "$${f%.tfw}").wld"; done  # copy and rename 2012 .tfw files
	sed -i '' 's/211666666667/317501750295/g' ecw/*.wld                                # fix pixel width compared to 2012

clean:
	rm -r ecw

dist-clean:
	rm -r cog ecw tiles.vrt

.PHONY: clean dist-clean
