SHELL := /bin/bash
NUM_THREADS := 4

tiles.vrt: cog
	gdalbuildvrt -addalpha -a_srs EPSG:25833 tiles.vrt cog/*.tif

cog: tif
	mkdir -p cog;
	for input in tif/*.tif; do \
		output=cog/`basename $$input`; \
		gdal_translate $$input $$output \
			-of COG -b 1 -a_srs EPSG:25833 \
			-co COMPRESS=JPEG -co QUALITY=75 -co BLOCKSIZE=512 \
			-co OVERVIEWS=IGNORE_EXISTING -co NUM_THREADS=$(NUM_THREADS); \
	done

tif: zip
	for f in zip/*.zip; do \
		unzip $$f -d tif; \
	done

zip:
	for url in \
		'https://fbinter.stadt-berlin.de/fb/atom/K5/farbe/k5_nordost_f.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/K5/farbe/k5_nordwest_f.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/K5/farbe/k5_suedost_f.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/K5/farbe/k5_suedwest_f.zip'; \
	do wget $$url -P zip; \
	done

clean:
	rm -r tif

dist-clean:
	rm -r cog tif zip tiles.vrt

.PHONY: clean dist-clean
