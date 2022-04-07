import matlab.engine

print("Starting matlab engine...")
eng = matlab.engine.start_matlab()
print("Finished starting matlab...")


def psnr(image_path: str, original_path: str) -> float:
    ref = eng.imread(image_path)
    vgl = eng.imread(original_path)
    return eng.psnr(vgl, ref)


def mssim(image_path: str, original_path: str) -> float:
    ref = eng.imread(image_path)
    vgl = eng.imread(original_path)
    return eng.multissim(vgl, ref)


def niqe(image_path: str) -> float:
    img = eng.imread(image_path)
    return eng.niqe(img)
