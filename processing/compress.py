import os
import decompress
from posixpath import splitext


def jxl(image: str, out_dir: str, quality: int):
    image_out = _create_out_image_path(image, out_dir, "jxl")
    os.system(f"magick {image} {image[:-4]}.png")
    os.system(f"cjxl {image[:-4]}.png {image_out} -q {quality} >/dev/null 2>&1")
    decompress.jxl(image_out)
    os.system(f"rm {image[:-4]}.png")
    return f"{image_out}.png"


def webp(image: str, out_dir: str, quality: float):
    image_out = _create_out_image_path(image, out_dir, "webp")
    os.system(f"magick {image} {image[:-4]}.png")
    os.system(f"cwebp -q {quality} {image[:-4]}.png -o {image_out} >/dev/null 2>&1")
    decompress.webp(image_out)
    os.system(f"rm {image[:-4]}.png")
    return f"{image_out}.png"


def jxr(image: str, out_dir: str, quality: int):
    image_out = _create_out_image_path(image, out_dir, "jxr")
    os.system(f"magick {image} {image[:-4]}.tif")
    os.system(f"JxrEncApp -q {quality / 100} -i {image[:-4]}.tif -o {image_out} >/dev/null 2>&1")
    decompress.jxr(image_out)
    os.system(f"rm {image[:-4]}.tif")
    return f"{image_out}.png"


def jpg(image: str, out_dir: str, quality: int):
    image_out = _create_out_image_path(image, out_dir, "jpg")
    os.system(f"magick -quality {quality} {image} {image_out}")
    decompress.jpg(image_out)
    return f"{image_out}.png"


def heic(image: str, out_dir: str, quality: int):
    image_out = _create_out_image_path(image, out_dir, "heic")
    os.system(f"magick {image} -quality {quality} {image_out}")
    decompress.heic(image_out)
    return f"{image_out}.png"


def jp2(image: str, out_dir: str, quality: int):
    image_out = _create_out_image_path(image, out_dir, "jp2")
    os.system(f"magick {image} -quality {quality} {image_out}")
    decompress.jp2(image_out)
    return f"{image_out}.png"


def _create_out_image_path(image_in: str, out_dir: str, extension: str) -> str:
    image_base_name = splitext(os.path.split(image_in)[1])[0]
    image_out = os.path.join(out_dir, f"{image_base_name}.{extension}")
    return image_out
