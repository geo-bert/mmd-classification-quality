import matlab.engine

print("Starting matlab engine...")
eng = matlab.engine.start_matlab()
print("Finished starting matlab...")

memo = {}


def psnr(image_path: str, original_path: str) -> float:
    ref = eng.imread(image_path)
    if original_path in memo:
        vgl = memo[original_path]
    else:
        vgl = eng.imread(original_path)
        memo[original_path] = vgl
    return eng.psnr(vgl, ref)


def mssim(image_path: str, original_path: str) -> float:
    ref = eng.imread(image_path)
    if original_path in memo:
        vgl = memo[original_path]
    else:
        vgl = eng.imread(original_path)
        memo[original_path] = vgl
    return sum(eng.multissim(vgl, ref)[0][0]) / 3


def niqe(image_path: str) -> float:
    img = eng.imread(image_path)
    return eng.niqe(img)
