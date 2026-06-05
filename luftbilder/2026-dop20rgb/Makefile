SHELL := /bin/bash
NUM_THREADS := 4

tiles.vrt: cog
	gdalbuildvrt -addalpha -a_srs EPSG:25833 tiles.vrt cog/*.tif

cog: jp2
	mkdir -p cog;
	for input in jp2/*.jp2; do \
		output=cog/`basename $${input%.jp2}.tif`; \
		gdal_translate $$input $$output \
			-of COG -b 1 -b 2 -b 3 -a_srs EPSG:25833 \
			-co COMPRESS=JPEG -co QUALITY=75 -co BLOCKSIZE=512 \
			-co OVERVIEWS=IGNORE_EXISTING -co NUM_THREADS=$(NUM_THREADS); \
	done

jp2: zip
	for f in zip/*.zip; do \
		unzip $$f -d jp2; \
	done

zip:
	for url in \
			'https://gdi.berlin.de/data/truedop_2026/atom/Mitte.zip' \
			'https://gdi.berlin.de/data/truedop_2026/atom/Nord.zip' \
			'https://gdi.berlin.de/data/truedop_2026/atom/Nordost.zip' \
			'https://gdi.berlin.de/data/truedop_2026/atom/Nordwest.zip' \
			'https://gdi.berlin.de/data/truedop_2026/atom/Ost.zip' \
			'https://gdi.berlin.de/data/truedop_2026/atom/Süd.zip' \
			'https://gdi.berlin.de/data/truedop_2026/atom/Südost.zip' \
			'https://gdi.berlin.de/data/truedop_2026/atom/Südwest.zip' \
			'https://gdi.berlin.de/data/truedop_2026/atom/West.zip'; \
		do wget $$url -c -P zip; \
	done

clean:
	rm -r jp2

dist-clean:
	rm -r cog jp2 zip tiles.vrt

.PHONY: clean dist-clean
