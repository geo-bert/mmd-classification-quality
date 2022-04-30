import os


def jpg(inp: str):
    os.system(f"djpeg -outfile {inp}.ppm {inp} >/dev/null 2>&1")
    os.system(f"magick {inp}.ppm {inp}.png")
    os.system(f"rm {inp}")
    os.system(f"rm {inp}.ppm")


def jxl(inp: str):
    os.system(f"djxl {inp} {inp}.png >/dev/null 2>&1")
    os.system(f"rm {inp}")


def jp2(inp: str):
    os.system(f"opj_decompress -i {inp} -o {inp}.png >/dev/null 2>&1")
    os.system(f"rm {inp}")


def jxr(inp: str):
    os.system(f"JxrDecApp -i {inp} -o {inp}.tif >/dev/null 2>&1")
    os.system(f"magick {inp}.tif {inp}.png")
    os.system(f"rm {inp}")
    os.system(f"rm {inp}.tif")


def webp(inp: str):
    os.system(f"dwebp {inp} -o {inp}.png >/dev/null 2>&1")
    os.system(f"rm {inp}")


def heic(inp: str):
    os.system(f"magick {inp} {inp}.png")
    os.system(f"rm {inp}")
