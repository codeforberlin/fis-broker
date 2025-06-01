import logging
import subprocess
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)

input_vrt = Path('ecw.vrt')

output_path = Path('cog')
output_path.mkdir(exist_ok=True)

tile_size = 10000

width = 188975
height = 149605

for xoff in range(0, width, tile_size):
    for yoff in range(0, height, tile_size):
        xsize = tile_size
        ysize = tile_size

        if xoff + tile_size > width:
            xsize = width - xoff
        if yoff + tile_size > height:
            ysize = height - yoff

        outfile = output_path / f'tile_{xoff}_{yoff}.tif'

        cmd = [
            "gdal_translate",
            "-srcwin", str(xoff), str(yoff), str(xsize), str(ysize),
            "-of", "COG",
            "-b", "1",
            "-a_srs", "EPSG:25833",
            "-co", "COMPRESS=JPEG",
            "-co", "QUALITY=75",
            "-co", "BLOCKSIZE=512",
            "-co", "OVERVIEWS=IGNORE_EXISTING",
            "-co", "NUM_THREADS=4",
            str(input_vrt),
            str(outfile)
        ]

        logging.info(' '.join(cmd))
        subprocess.check_call(cmd)
