import os
from posixpath import splitext
import cli_config


def single_compression_xl(image: str,out_dir: str, quality: int) -> str:
    image_out = create_out_image_path(image, out_dir, "jxl")
    print(image_out)
    print(cli_config.cjxl +" "+image+" "+ image_out +" -q " +str(quality))
    os.system(cli_config.cjxl +" "+image+" "+ image_out +" -q " +str(quality))
    return image_out

def single_compression_webp(image: str,out_dir: str, quality: float) -> str:
    image_out = create_out_image_path(image,out_dir, "webp")
    os.system(cli_config.cwebp +" -q "+str(quality)+" "+image+" -o "+image_out)
    return image_out

def single_compression_xr(image: str,out_dir: str, quality: float) -> str:
    image_out = create_out_image_path(image,out_dir, "jxr")
    os.system(cli_config.JxrEncApp +" -q " + str(quality)+" -i "+image+" -o "+image_out)
    return image_out

def single_compression_jpg(image: str,out_dir: str, quality: int) -> str:
    image_out = create_out_image_path(image,out_dir, "jpg")
    os.system(cli_config.magick+" -quality "+ str(quality)+" "+image+" "+image_out)
    return image_out    

def single_compression_heic(image: str,out_dir: str, quality: int) -> str:
    image_out = create_out_image_path(image,out_dir, "heic")
    os.system(cli_config.magick+" "+image+" -quality "+str(quality)+" "+image_out)
    return image_out   

def single_compression_jp2(image: str,out_dir: str, quality: int) -> str:
    image_out = create_out_image_path(image,out_dir, "jp2")
    os.system(cli_config.magick+" "+image+" -quality "+str(quality)+" "+image_out)
    return image_out  

def create_out_image_path(image_in: str, out_dir: str, format: str) -> str:
    image_base_name = splitext(os.path.split(image_in)[1])[0]
    image_out = os.path.join(out_dir, image_base_name+"."+format)
    return image_out

"""for testing"""
def compressDir(filepath: str): 
    quality = 20
    original_images = os.path.join(filepath, "original")
    compressed_images = os.path.join(filepath,"comp_jp2_"+str(quality))
    os.mkdir(compressed_images)
    for f in os.listdir(original_images):
        single_compression_jp2(os.path.join(original_images,f), compressed_images, quality)


compressDir("../example_images")