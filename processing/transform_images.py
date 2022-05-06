import os

import matlab.engine

import binary_search as bs
import compress
import quality_metrics as qm

INPUT_IMAGES = "../images/input"
COMPRESSIONS = [
    ("heic", compress.heic),
    ("jp2", compress.jp2),
    ("jpg", compress.jpg),
    ("jxl", compress.jxl),
    ("jxr", compress.jxr),
    ("webp", compress.webp)
]
TARGET_PSNR = 25
TARGET_SSIM = 0.9
TARGET_NIQE = 5


def main():
    input_images = os.listdir(INPUT_IMAGES)
    problematic = set()

    # PSNR
    outpath = f"../images/output/psnr_{TARGET_PSNR}"
    for img in input_images:
        in_img = os.path.join(INPUT_IMAGES, img)
        for name, fn in COMPRESSIONS:
            out_path = os.path.join(outpath, name)
            try:
                bs.search_fr(in_img, TARGET_PSNR, fn, qm.psnr, out_path)
            except matlab.engine.MatlabExecutionError:
                problematic.add(in_img)
                print(f"Could not convert {in_img}")

    # ms-ssim, 2 options: avg or best value
    outpath = f"../images/output/ssim_avg_{TARGET_SSIM}"
    for img in input_images:
        in_img = os.path.join(INPUT_IMAGES, img)
        for name, fn in COMPRESSIONS:
            out_path = os.path.join(outpath, name)
            try:
                bs.search_fr(in_img, TARGET_SSIM, fn, qm.mssim_avg, out_path)
            except matlab.engine.MatlabExecutionError:
                problematic.add(in_img)
                print(f"Could not convert {in_img}")

    outpath = f"../images/output/ssim_bv_{TARGET_SSIM}"
    for img in input_images:
        in_img = os.path.join(INPUT_IMAGES, img)
        for name, fn in COMPRESSIONS:
            out_path = os.path.join(outpath, name)
            try:
                bs.search_fr(in_img, TARGET_SSIM, fn, qm.mssim_bv, out_path)
            except matlab.engine.MatlabExecutionError:
                problematic.add(in_img)
                print(f"Could not convert {in_img}")

    # niqe
    outpath = f"../images/output/niqe_{TARGET_NIQE}"
    for img in input_images:
        in_img = os.path.join(INPUT_IMAGES, img)
        for name, fn in COMPRESSIONS:
            out_path = os.path.join(outpath, name)
            try:
                bs.search_fr(in_img, TARGET_SSIM, fn, qm.niqe, out_path,False) #False flag to toggle approximation from above
            except matlab.engine.MatlabExecutionError:
                problematic.add(in_img)
                print(f"Could not convert {in_img}")

    print(problematic)

if __name__ == "__main__":
    main()
