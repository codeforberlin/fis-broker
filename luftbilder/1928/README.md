Luftbilder 1928, Maßstab 1:4 000
================================

## Metadaten

* https://gdi.berlin.de/geonetwork/srv/ger/catalog.search#/metadata/6b746499-7354-3a3a-aa70-60e1fb37f993

## Downloaddienst (Atom)

* https://fbinter.stadt-berlin.de/fb/feed/senstadt/a_luftbild1928
* https://fbinter.stadt-berlin.de/fb/feed/senstadt/a_luftbild1928/0

## Attribution

Senatsverwaltung für Stadtentwicklung, Bauen und Wohnen Berlin / Luftbilder 1928, Maßstab 1:4 000

## Lizenz

Für die Nutzung der Daten ist die Datenlizenz Deutschland - Zero - Version 2.0 anzuwenden.
Die Lizenz ist über https://www.govdata.de/dl-de/zero-2-0 abrufbar.

## Projektion

[EPSG:25833](http://spatialreference.org/ref/epsg/25833/)

## Blattschnitt

https://fbinter.stadt-berlin.de/fb/atom/DOP/Blattschnitt2x2km.gif

## Setup

Run `make` to download and convert the tiles. See the `Makefile` for details.

The original images have unusual dimensions of 7874 x 7874 pixel, which (for reasons unknown to me) breaks the use
of overview in COG. There for the area is cut into 10000 x 10000 tiles by `convert.py`.
