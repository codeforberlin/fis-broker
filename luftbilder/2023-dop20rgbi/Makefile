SHELL := /bin/bash
NUM_THREADS := 4

tiles.vrt: cog
	gdalbuildvrt -a_srs EPSG:25833 tiles.vrt cog/*.tif

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
	mv jp2/Ost/* jp2/.
	rm -r jp2/Ost

zip:
	for url in \
			'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2023/Mitte.zip' \
			'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2023/Nord.zip' \
			'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2023/Nordost.zip' \
			'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2023/Nordwest.zip' \
			'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2023/Ost.zip' \
			'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2023/Sued.zip' \
			'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2023/Suedost.zip' \
			'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2023/Suedwest.zip' \
			'https://fbinter.stadt-berlin.de/fb/atom/DOP/dop20true_rgbi_2023/West.zip'; \
		do wget $$url -P zip; \
	done

clean:
	rm -r jp2

dist-clean:
	rm -r cog jp2 zip tiles.vrt

.PHONY: clean dist-clean
