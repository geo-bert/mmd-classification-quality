import os
import sys

import compress
import quality_metrics as qm
import binary_search as bs

import matlab.engine

COMPRESSIONS = [
    ("heic", compress.heic),
    ("jp2", compress.jp2),
    ("jpg", compress.jpg),
    ("jxl", compress.jxl),
    ("jxr", compress.jxr),
    ("webp", compress.webp)
]

METRICS = {
        "psnr": qm.psnr,
        "mssim_avg": qm.mssim_avg,
        "mssim_bv": qm.mssim_bv,
        "niqe": qm.niqe
}


def main(args):
    _, compression, target, folder = args
    target = float(target)
    folder = os.path.abspath(folder)

    if compression not in METRICS:
        print(f"Invalid compression type: {compression}")
        exit(1)

    input_images = os.listdir(folder)
    problematic = set()

    outpath = os.path.join("/", *os.path.abspath(folder).split(os.sep)[:-1], "output", f"{compression}_{target}")

    os.system(f"rm -r {outpath}")
    os.system(f"mkdir {outpath}")
    os.system(f"mkdir {os.path.join(outpath, 'heic')}")
    os.system(f"mkdir {os.path.join(outpath, 'jpg')}")
    os.system(f"mkdir {os.path.join(outpath, 'jxl')}")
    os.system(f"mkdir {os.path.join(outpath, 'jxr')}")
    os.system(f"mkdir {os.path.join(outpath, 'jp2')}")
    os.system(f"mkdir {os.path.join(outpath, 'webp')}")

    for img in input_images:
        in_img = os.path.join(folder, img)
        for name, fn in COMPRESSIONS:
            out_path = os.path.join(outpath, name)
            try:
                bs.search(in_img, target, fn, METRICS[compression], out_path, compression != "niqe")
            except matlab.engine.MatlabExecutionError:
                problematic.add(in_img)
                print(f"Could not convert {in_img}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("transform_images.py <compression> <target-value> <input-folder>")
        exit(1)
    main(sys.argv)
