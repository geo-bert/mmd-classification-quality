import math
import os


def search(img_in, target, fn_compress, fn_quality, out, from_below=True):
    quality_flag = -1
    metric = -1 if from_below else math.inf

    def binary_search(low, high):
        nonlocal metric
        nonlocal quality_flag

        if high < low:
            return

        mid = (high + low) // 2
        q = calc_new_quality(mid)

        if from_below and abs(metric-target) < abs(q-target):
            metric = q
            quality_flag = mid
        elif not from_below and abs(metric-target) > abs(q-target):
            metric = q
            quality_flag = mid

        if math.isnan(q) or q < target:
            binary_search(mid + 1, high)
        elif q > target:
            binary_search(low, mid - 1)
        else:
            metric = q
            quality_flag = mid

    def calc_new_quality(x):
        img = fn_compress(img_in, out, x)
        return fn_quality(img, img_in)

    binary_search(0, 100)

    print(f"{img_in.split(os.sep)[-1]} -> {out.split(os.sep)[-1]}: Metric={metric} Quality={quality_flag}")
    fn_compress(img_in, out, quality_flag)
    return quality_flag
