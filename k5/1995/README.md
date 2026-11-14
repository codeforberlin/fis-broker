Karte von Berlin 1:5000 (K5 - SW-Ausgabe) - 1995
================================================

## Quellenangabe

[Senatsverwaltung für Stadtentwicklung, Bauen und Wohnen Berlin / Karte von Berlin 1:5000 (K5) - 1995](https://gdi.berlin.de/geonetwork/srv/ger/catalog.search#/metadata/ed9d0b87-ab8b-3db0-9bf3-7f9218cc004a)

## Lizenz

Für die Nutzung der Daten ist die Datenlizenz Deutschland - Zero - Version 2.0 anzuwenden.
Die Lizenz ist über https://www.govdata.de/dl-de/zero-2-0 abrufbar.

## Projektion

[EPSG:3068](http://spatialreference.org/ref/epsg/3068/)

## Konvertierung

Mit `make` werden mit Hilfe von [GDAL](https://gdal.org) die [GeoTIFF](https://gdal.org/en/stable/drivers/raster/gtiff.html)-Dateien aus der bereits heruntergeladenen Datei `1995.zip` in [COG](https://gdal.org/en/stable/drivers/raster/cog.html) umgewandelt. Die Pixelgröße in den `.tfw`-Dateien wird dabei korrigiert. Details sind im `Makefile` zu finden.

## Nutzung

### [OpenLayers](https://openlayers.org)

```js
import TileLayer from 'ol/layer/Tile'
import XYZ from 'ol/source/XYZ'

map.addLayer(new TileLayer({
  source: new XYZ({
    url: 'https://tiles.codefor.de/berlin/geoportal/k5/1995/{z}/{x}/{y}.png',
    attributions: '<a href="https://gdi.berlin.de/geonetwork/srv/ger/catalog.search#/metadata/ed9d0b87-ab8b-3db0-9bf3-7f9218cc004a" target="_blank" rel="noopener">Senatsverwaltung für Stadtentwicklung, Bauen und Wohnen Berlin / Karte von Berlin 1:5000 (K5) - 1995</a>'
  })
}))
```

### [Leaflet](https://leafletjs.com)

```js
L.tileLayer('https://tiles.codefor.de/berlin/geoportal/k5/1995/{z}/{x}/{y}.png', {
  attribution: '<a href="https://gdi.berlin.de/geonetwork/srv/ger/catalog.search#/metadata/ed9d0b87-ab8b-3db0-9bf3-7f9218cc004a" target="_blank" rel="noopener">Senatsverwaltung für Stadtentwicklung, Bauen und Wohnen Berlin / Karte von Berlin 1:5000 (K5) - 1995</a>'
}).addTo(map)
```

### [gdal-tiles-api](https://github.com/codeforberlin/gdal-tiles-api)

```toml
[[maps]]
name = "Karte von Berlin 1:5000 (K5) - 1995"
path = "berlin/geoportal/k5/1995"
attribution.text = "Senatsverwaltung für Stadtentwicklung, Bauen und Wohnen Berlin / Karte von Berlin 1:5000 (K5) - 1995"
attribution.href = "https://gdi.berlin.de/geonetwork/srv/ger/catalog.search#/metadata/ed9d0b87-ab8b-3db0-9bf3-7f9218cc004a"
```

### [@jochenklar/maps](https://github.com/jochenklar/maps)

```json
{
  "name": "Karte von Berlin 1:5000 (K5) - 1995",
  "url": "https://tiles.codefor.de/berlin/geoportal/k5/1995/{z}/{x}/{y}.png",
  "attribution": "<a href=\"https://gdi.berlin.de/geonetwork/srv/ger/catalog.search#/metadata/ed9d0b87-ab8b-3db0-9bf3-7f9218cc004a\" target=\"_blank\" rel=\"noopener\">Senatsverwaltung für Stadtentwicklung, Bauen und Wohnen Berlin / Karte von Berlin 1:5000 (K5) - 1995</a>"
}
```
