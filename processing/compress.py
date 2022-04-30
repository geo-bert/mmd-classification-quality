import os
import decompress
from posixpath import splitext


def jxl(image: str, out_dir: str, quality: int):
    image_out = _create_out_image_path(image, out_dir, "jxl")
    os.system(f"cjxl {image} {image_out} -q {quality}")
    decompress.jxl(image_out)
    return image_out


def webp(image: str, out_dir: str, quality: float):
    image_out = _create_out_image_path(image, out_dir, "webp")
    os.system(f"cwebp -q {quality} {image} -o {image_out}")
    decompress.webp(image_out)
    return image_out


def jxr(image: str, out_dir: str, quality: int):
    image_out = _create_out_image_path(image, out_dir, "jxr")
    os.system(f"JxrEncApp -q {quality / 100} -i {image} -o {image_out}")
    decompress.jxr(image_out)
    return image_out


def jpg(image: str, out_dir: str, quality: int):
    image_out = _create_out_image_path(image, out_dir, "jpg")
    os.system(f"magick -quality {quality} {image} {image_out}")
    decompress.jpg(image_out)
    return image_out


def heic(image: str, out_dir: str, quality: int):
    image_out = _create_out_image_path(image, out_dir, "heic")
    os.system(f"heif-enc -q {quality} -o {image_out} {image}")
    decompress.heic(image_out)
    return image_out


def jp2(image: str, out_dir: str, quality: int):
    image_out = _create_out_image_path(image, out_dir, "jp2")
    os.system(f"magick {image} -quality {quality} {image_out}")
    decompress.jp2(image_out)
    return image_out


def _create_out_image_path(image_in: str, out_dir: str, extension: str) -> str:
    image_base_name = splitext(os.path.split(image_in)[1])[0]
    image_out = os.path.join(out_dir, f"{image_base_name}.{extension}")
    return image_out
