Luftbilder 1953, Maßstab 1:22 000
=================================

## Metadaten

* https://gdi.berlin.de/geonetwork/srv/ger/catalog.search#/metadata/6b746499-7354-3a3a-aa70-60e1fb37f993

## Attribution

Senatsverwaltung für Stadtentwicklung, Bauen und Wohnen Berlin / Luftbilder 1953, Maßstab 1:22 000

## Lizenz

Für die Nutzung der Daten ist die Datenlizenz Deutschland - Zero - Version 2.0 anzuwenden.
Die Lizenz ist über https://www.govdata.de/dl-de/zero-2-0 abrufbar.

## Projektion

[EPSG:25833](http://spatialreference.org/ref/epsg/25833/)

## Blattschnitt

https://fbinter.stadt-berlin.de/fb/atom/DOP/Blattschnitt2x2km.gif

## Setup

Run `make` to download and convert the tiles. See the `Makefile` for details.

The images are only available vie `WMS`, so we download them in 10000 x 10000 png tiles and
convert them to COG using `download.py`.
