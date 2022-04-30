import os
from posixpath import splitext

import cli_config


def single_compression_xl(image: str, out_dir: str, quality: int) -> str:
    image_out = create_out_image_path(image, out_dir, "jxl")
    os.system(f"{cli_config.cjxl} {image} {image_out} -q {quality}")
    return image_out


def single_compression_webp(image: str, out_dir: str, quality: float) -> str:
    image_out = create_out_image_path(image, out_dir, "webp")
    os.system(f"{cli_config.cwebp} -q {quality} {image} -o {image_out}")
    return image_out


def single_compression_xr(image: str, out_dir: str, quality: int) -> str:
    image_out = create_out_image_path(image, out_dir, "jxr")
    os.system(f"{cli_config.JxrEncApp} -q {quality/100} -i {image} -o {image_out}")
    return image_out


def single_compression_jpg(image: str, out_dir: str, quality: int) -> str:
    image_out = create_out_image_path(image, out_dir, "jpg")
    os.system(f"{cli_config.magick} -quality {quality} {image} {image_out}")
    return image_out


def single_compression_heic(image: str, out_dir: str, quality: int) -> str:
    image_out = create_out_image_path(image, out_dir, "heic")
    os.system(f"{cli_config.magick} {image} -quality {quality} {image_out}")
    return image_out


def single_compression_jp2(image: str, out_dir: str, quality: int) -> str:
    image_out = create_out_image_path(image, out_dir, "jp2")
    os.system(f"{cli_config.magick} {image} -quality {quality} {image_out}")
    return image_out


def create_out_image_path(image_in: str, out_dir: str, extension: str) -> str:
    image_base_name = splitext(os.path.split(image_in)[1])[0]
    image_out = os.path.join(out_dir, f"{image_base_name}.{extension}")
    return image_out


def compress_dir(filepath: str):
    """for testing"""
    quality = 20
    original_images = os.path.join(filepath, "original")
    compressed_images = os.path.join(filepath, f"comp_jp2_{quality}")
    os.mkdir(compressed_images)
    for f in os.listdir(original_images):
        single_compression_jp2(os.path.join(original_images, f), compressed_images, quality)


if __name__ == "__main__":
    compress_dir("../example_images")
