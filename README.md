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

ECW files
---------

In order to process `ecw` files, gdal needs to be compiled agains the proprietary ERDAS library (see also: https://trac.osgeo.org/gdal/wiki/ECW).

1) Download the ERDAS installer from https://download.hexagongeospatial.com/downloads/ecw/erdas-ecw-jp2-sdk-v5-4-linux. Run the installer with `bash` to install into `~/hexagon`. Move the directory afterwards to `/opt/hexagon`.

2) Then, obtain gdal from https://trac.osgeo.org/gdal/wiki/DownloadSource.

3) Extract the gdal source, change to the directory, and:

    ```
    ./configure --with-ecw=/opt/hexagon/ERDAS-ECW_JPEG_2000_SDK-5.3.0/Desktop_Read-Only
    make -j 8
    make install
    ```

4) On Debian 9.0 an additional softling needs to be created:

    ```
    ln -s /store/opt/hexagon/ERDAS-ECW_JPEG_2000_SDK-5.4.0/Desktop_Read-Only/lib/newabi/x64/release/libNCSEcw.so* /usr/local/lib/
    ldconfig
    ```
