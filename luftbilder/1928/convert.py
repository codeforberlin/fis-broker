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

        gdal_translate_cmd = [
            "gdal_translate",
            "-srcwin", str(xoff), str(yoff), str(xsize), str(ysize),
            "-of", "COG",
            "-b", "1",
            "-b", "2",
            "-a_srs", "EPSG:25833",
            "-co", "COMPRESS=JPEG",
            "-co", "QUALITY=75",
            "-co", "BLOCKSIZE=512",
            "-co", "OVERVIEWS=IGNORE_EXISTING",
            "-co", "NUM_THREADS=4",
            str(input_vrt),
            str(outfile)
        ]

        logging.info(' '.join(gdal_translate_cmd))
        subprocess.check_call(gdal_translate_cmd)

        gdalinfo_cmd = [
            "gdalinfo",
            "-stats",
            str(outfile)
        ]

        logging.info(' '.join(gdalinfo_cmd))
        gdalinfo = subprocess.check_output(gdalinfo_cmd)

        if b'''Band 1 Block=512x512 Type=Byte, ColorInterp=Gray
  Minimum=0.000, Maximum=0.000, Mean=0.000, StdDev=0.000''' in gdalinfo:
            logging.warning(f'remove empty {outfile}')
            outfile.unlink()
            outfile.with_suffix('.tif.aux.xml').unlink()
