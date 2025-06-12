SHELL:=/bin/bash

tiles.vrt: cog
	gdalbuildvrt -addalpha -a_srs EPSG:3068 tiles.vrt cog/*.tif

cog: warped
	mkdir -p cog;
	for input in warped/*.tif; do \
		output=cog/`basename $$input`; \
		gdal_translate $$input $$output -of COG -a_srs EPSG:3068 \
		                                -co COMPRESS=JPEG -co QUALITY=75 -co BLOCKSIZE=512 \
		                                -co OVERVIEWS=IGNORE_EXISTING; \
	done

warped: fixed
	mkdir -p warped;
	for input in fixed/*.tif; do \
		output=warped/`basename $$input`; \
		gdalwarp $$input $$output -s_srs EPSG:3068 -t_srs EPSG:3068 -r bilinear -srcnodata 0 -dstalpha; \
	done

fixed: tif
	mkdir -p fixed
	python fix_coordinates.py

tif: zip
	unzip zip/Gebaeudeschaeden_1945.zip -d tif
	rename 's/[^[:ascii:]]//g' tif/*  # fix the filenames

zip:
	wget https://fbinter.stadt-berlin.de/fb/atom/Berlin_um/Gebaeudeschaeden_1945.zip -P zip

clean:
	rm -r warped fixed tif

dist-clean:
	rm -r cog warped fixed tif zip tiles.vrt

.PHONY: clean dist-clean
