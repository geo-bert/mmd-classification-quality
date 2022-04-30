import os
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
TARGET_PSNR = 35
TARGET_SSIM = 0.9
TARGET_NIQE = 5


def main():
    input_images = os.listdir(INPUT_IMAGES)[:5]

    # PSNR
    outpath = "../images/output/psnr"
    for img in input_images:
        in_img = os.path.join(INPUT_IMAGES, img)
        for name, fn in COMPRESSIONS:
            out_path = os.path.join(outpath, name)
            bs.search_fr(in_img, TARGET_PSNR, fn, qm.psnr, out_path)

    # ms-ssim
    # TODO

    # niqe
    # TODO: von oben annähern, ist no reference


if __name__ == "__main__":
    main()
