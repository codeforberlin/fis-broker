Berlin FIS-Broker download scripts
==================================

Convert the ATOM FEED of the Berlin Geo-Data-Portal to GeoTIFF to create tile for Leaflet or openlayers.

More info in the README.md files of the directories.


Cloud Optimized GeoTIFF (COG) 
-----------------------------

Upstream file are converted to [Cloud Optimized GeoTIFF (COG)](https://cogeo.org/). This is done using the following command (or a variation, depending on the upstream
data):

```
gdal_translate $input $output -of COG -b 1 -b 2 -b 3 -a_srs EPSG:25833
                              -co COMPRESS=JPEG -co QUALITY=75 -co BLOCKSIZE=512
                              -co OVERVIEWS=IGNORE_EXISTING
```

Some information about GeoTIFF and COG is given on http://blog.cleverelephant.ca/2015/02/geotiff-compression-for-dummies.html.

rsync
-----

To copy only the converted tif files and the vrt to a remote server use:

```
rsync --delete -av --include="*/" --include="cog/*.tif" --include="*.vrt" --exclude="*" ./ USER@SERVER:PATH/
```

ECW files
---------

In order to process `ecw` files, GDAL needs to be compiled agains the proprietary ERDAS library (see
also: https://trac.osgeo.org/gdal/wiki/ECW). You can use this installation as your only GDAL in
`/usr/local/bin`, but I prefer it to be decoupled from my regular setup in `/opt/`.

1) Install `libproj-dev` with `apt-get install libproj-dev`.

2) Download the ERDAS installer from http://download.hexagongeospatial.com/downloads/ecw/erdas-ecw-jp2-sdk-v5-5-update-4-linux.
You need to create an account for this. Run the installer with `bash` to install into `~/hexagon`.
Move the directory afterwards to `/opt/hexagon`.

    ```
3) Then, obtain and build `gdal-3.4.1` from https://gdal.org/en/stable/download_past.html. It might also work with a newer version, but I did not test this.

    ```bash
    export CXXFLAGS="-I/opt/hexagon/ERDAS-ECW_JPEG_2000_SDK-5.5.0/Desktop_Read-Only/include"
    export LDFLAGS="-L/opt/hexagon/ERDAS-ECW_JPEG_2000_SDK-5.5.0/Desktop_Read-Only/lib/cpp11abi/x64/release/"
    export LD_LIBRARY_PATH="/opt/hexagon/ERDAS-ECW_JPEG_2000_SDK-5.5.0/Desktop_Read-Only/lib/cpp11abi/x64/release/:$LD_LIBRARY_PATH"

    ./configure --with-ecw=/opt/hexagon/ERDAS-ECW_JPEG_2000_SDK-5.5.0/Desktop_Read-Only/ --prefix=/opt/gdal-3.4.1/
    make -j 8
    make install
    ```

4) To use the build GDAL use:

    ```
    export PATH=/opt/gdal-3.4.1/bin/:$PATH
    export LD_LIBRARY_PATH=/opt/hexagon/ERDAS-ECW_JPEG_2000_SDK-5.5.0/Desktop_Read-Only/lib/cpp11abi/x64/release/
    ```

    (Not needed for the included Makefiles.)
