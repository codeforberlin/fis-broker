SHELL:=/bin/bash

tiles.vrt: tmp
	mkdir tif
	python convert.py

tmp: zip
	unzip zip/Gebaeudeschaeden_1945.zip -d tmp

zip:
	wget https://fbinter.stadt-berlin.de/fb/atom/Berlin_um/Gebaeudeschaeden_1945.zip -P zip

clean:
	rm -rf zip tmp

.PHONY: clean
