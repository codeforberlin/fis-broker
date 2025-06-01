SHELL:=/bin/bash

tiles.vrt: cog
	gdalbuildvrt -a_srs EPSG:25833 tiles.vrt cog/*.tif

cog:
	python download_and_convert.py

dist-clean:
	rm -r cog png tiles.vrt

.PHONY: dist-clean
