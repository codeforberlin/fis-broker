import math
import logging
import subprocess
from pathlib import Path

import requests

logging.basicConfig(level=logging.DEBUG)

wms_url = "https://gdi.berlin.de/services/wms/luftbild_1953_22"
crs = "EPSG:25833"

minx = 370000
maxx = 420000
miny = 5800000
maxy = 5840000

tile_size_px = 10000
pixel_size = 0.4
tile_size_m = tile_size_px * pixel_size

Path('png').mkdir(exist_ok=True)
Path('cog').mkdir(exist_ok=True)

def download_tile(tile_minx, tile_miny, tile_maxx, tile_maxy, out_png):
    params = {
        "SERVICE": "WMS",
        "VERSION": "1.3.0",
        "REQUEST": "GetMap",
        "LAYERS": "c_luftbilder_1953_22_raster",
        "STYLES": "",
        "CRS": crs,
        "BBOX": f"{tile_minx},{tile_miny},{tile_maxx},{tile_maxy}",
        "WIDTH": tile_size_px,
        "HEIGHT": tile_size_px,
        "FORMAT": "image/png",
    }

    r = requests.get(wms_url, params=params, stream=True)

    logging.info('downloading %s', r.url)
    if r.status_code == 200:
        with open(out_png, "wb") as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
    else:
        logging.error('[%s] %s', r.status_code, r.content)

def check_if_all_white(file_path):
        output = subprocess.check_output(["gdalinfo", "-stats", file_path])
        return b'Minimum=255.000, Maximum=255.000, Mean=255.000, StdDev=0.000' in output

def convert_to_cog(png_file, tiff_file, minx, maxy, maxx, miny):
    cmd = [
        "gdal_translate",
        "-of", "COG",
        "-a_srs", crs,
        "-a_ullr", str(minx), str(maxy), str(maxx), str(miny),
        "-b", "1",
        "-co", "COMPRESS=JPEG",
        "-co", "QUALITY=75",
        "-co", "BLOCKSIZE=512",
        "-co", "OVERVIEWS=IGNORE_EXISTING",
        "-co", "NUM_THREADS=4",
        str(png_file), str(tiff_file)
    ]
    logging.info(' '.join(cmd))
    subprocess.run(cmd, check=True)

x_tiles = math.ceil((maxx - minx) / tile_size_m)
y_tiles = math.ceil((maxy - miny) / tile_size_m)

for i in range(x_tiles):
    for j in range(y_tiles):
        tile_minx = minx + i * tile_size_m
        tile_maxx = tile_minx + tile_size_m
        tile_miny = miny + j * tile_size_m
        tile_maxy = tile_miny + tile_size_m

        tile_name = f"tile_{int(tile_minx)}_{int(tile_miny)}"
        png_path = Path('png') / f"{tile_name}.png"
        cog_path = Path('cog') / f"{tile_name}.tif"

        if check_if_all_white(png_path):
            png_path.unlink()
        else:
            convert_to_cog(png_path, cog_path, tile_minx, tile_maxy, tile_maxx, tile_miny)
