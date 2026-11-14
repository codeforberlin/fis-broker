Karte von Berlin 1:5000 (K5 - Farbausgabe) - 2016
=================================================

## Quellenangabe

[Senatsverwaltung für Stadtentwicklung, Bauen und Wohnen Berlin / Karte von Berlin 1:5000 (K5) - 2016](https://gdi.berlin.de/geonetwork/srv/ger/catalog.search#/metadata/ed9d0b87-ab8b-3db0-9bf3-7f9218cc004a)

## Lizenz

Für die Nutzung der Daten ist die Datenlizenz Deutschland - Zero - Version 2.0 anzuwenden.
Die Lizenz ist über https://www.govdata.de/dl-de/zero-2-0 abrufbar.

## Projektion

[EPSG:25833](http://spatialreference.org/ref/epsg/25833/)

## Konvertierung

Mit `make` werden mit Hilfe von [GDAL](https://gdal.org) die [ECW](https://gdal.org/en/stable/drivers/raster/ecw.html)-Dateien aus der bereits heruntergeladenen Datei `TIFF_F_2016.zip` in [COG](https://gdal.org/en/stable/drivers/raster/cog.html) umgewandelt. Für ECW-Dateien wird GDAL mit ECW-Unterstützung benötigt (siehe [ECW files](../../README.md#ecw-files)). Die Georeferenzierung wird aus den `.tfw`-Dateien von 2017 übernommen. Details sind im `Makefile` zu finden.

## Nutzung

### [OpenLayers](https://openlayers.org)

```js
import TileLayer from 'ol/layer/Tile'
import XYZ from 'ol/source/XYZ'

map.addLayer(new TileLayer({
  source: new XYZ({
    url: 'https://tiles.codefor.de/berlin/geoportal/k5/2016/{z}/{x}/{y}.png',
    attributions: '<a href="https://gdi.berlin.de/geonetwork/srv/ger/catalog.search#/metadata/ed9d0b87-ab8b-3db0-9bf3-7f9218cc004a" target="_blank" rel="noopener">Senatsverwaltung für Stadtentwicklung, Bauen und Wohnen Berlin / Karte von Berlin 1:5000 (K5) - 2016</a>'
  })
}))
```

### [Leaflet](https://leafletjs.com)

```js
L.tileLayer('https://tiles.codefor.de/berlin/geoportal/k5/2016/{z}/{x}/{y}.png', {
  attribution: '<a href="https://gdi.berlin.de/geonetwork/srv/ger/catalog.search#/metadata/ed9d0b87-ab8b-3db0-9bf3-7f9218cc004a" target="_blank" rel="noopener">Senatsverwaltung für Stadtentwicklung, Bauen und Wohnen Berlin / Karte von Berlin 1:5000 (K5) - 2016</a>'
}).addTo(map)
```

### [gdal-tiles-api](https://github.com/codeforberlin/gdal-tiles-api)

```toml
[[maps]]
name = "Karte von Berlin 1:5000 (K5) - 2016"
path = "berlin/geoportal/k5/2016"
attribution.text = "Senatsverwaltung für Stadtentwicklung, Bauen und Wohnen Berlin / Karte von Berlin 1:5000 (K5) - 2016"
attribution.href = "https://gdi.berlin.de/geonetwork/srv/ger/catalog.search#/metadata/ed9d0b87-ab8b-3db0-9bf3-7f9218cc004a"
```

### [@jochenklar/maps](https://github.com/jochenklar/maps)

```json
{
  "name": "Karte von Berlin 1:5000 (K5) - 2016",
  "url": "https://tiles.codefor.de/berlin/geoportal/k5/2016/{z}/{x}/{y}.png",
  "attribution": "<a href=\"https://gdi.berlin.de/geonetwork/srv/ger/catalog.search#/metadata/ed9d0b87-ab8b-3db0-9bf3-7f9218cc004a\" target=\"_blank\" rel=\"noopener\">Senatsverwaltung für Stadtentwicklung, Bauen und Wohnen Berlin / Karte von Berlin 1:5000 (K5) - 2016</a>"
}
```
