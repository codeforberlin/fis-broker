SHELL:=/bin/bash

tiles.vrt: tif
	gdalbuildvrt -a_srs EPSG:25833 tiles.vrt tif/*.tif

tif: zip
	for f in zip/*.zip; do unzip $$f -d tif; done

zip:
	for url in \
		'https://fbinter.stadt-berlin.de/fb/atom/K5/farbe/k5_nordost_f.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/K5/farbe/k5_nordwest_f.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/K5/farbe/k5_suedost_f.zip' \
		'https://fbinter.stadt-berlin.de/fb/atom/K5/farbe/k5_suedwest_f.zip'; \
	do wget $$url -P zip; \
	done

clean:
	rm -rf zip ecw

.PHONY: clean
