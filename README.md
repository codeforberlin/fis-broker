Berlin FIS-Broker download scripts
==================================

Convert the ATOM FEED of the Berlin Geo-Data-Portal to GeoTIFF to create tile for Leaflet or openlayers.

More info in the README.md files of the directories.


Conversion
----------

Conversion is done following http://blog.cleverelephant.ca/2015/02/geotiff-compression-for-dummies.html. In particular:

```
gdal_translate -co COMPRESS=JPEG -co PHOTOMETRIC=YCBCR -co TILED=YES -a_srs EPSG:25833 ECWFILE GTIFFFILE
```

and

```
gdaladdo --config COMPRESS_OVERVIEW JPEG --config PHOTOMETRIC_OVERVIEW YCBCR --config INTERLEAVE_OVERVIEW PIXEL -r average GTIFFFILE 2 4 8 16
```

rsync
-----

To copy only the converted tif files and the vrt to a remote server use:

```
rsync --delete -av --include=*.gdal.tif --include=*.vrt --exclude-from=rsync-exclude ./ USER@SERVER:PATH/
```