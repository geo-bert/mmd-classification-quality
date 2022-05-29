import math
import os


def search(img_in, target, fn_compress, fn_quality, out):
    quality_flag = -1
    metric = -1

    def binary_search(low, high):
        nonlocal metric
        nonlocal quality_flag

        if high < low:
            return

        mid = (high + low) // 2
        q = calc_new_quality(mid)
        print(f"{q} - {mid}", end=" | ")

        if abs(metric - target) > abs(q - target) and q < target:
            metric = q
            quality_flag = mid

        if math.isnan(q) or q < target:
            binary_search(mid + 1, high)
        elif q > target:
            binary_search(low, mid - 1)

    def calc_new_quality(x):
        img = fn_compress(img_in, out, x)
        return fn_quality(img, img_in)

    binary_search(0, 100)

    print()
    print(f"{img_in.split(os.sep)[-1]} -> {out.split(os.sep)[-1]}: Metric={metric} Quality={quality_flag}")

    if metric > target:
        print("metric too large")
        exit(-1)

    return quality_flag


def search_niqe(img_in, target, fn_compress, fn_quality, out):
    def calc_new_quality(x):
        img = fn_compress(img_in, out, x)
        return fn_quality(img, img_in)

    stepRange = range(50, 100)
    q = calc_new_quality(50)
    currBest = (q, 50)

    # change range depening on first halfing
    if q < target:
        stepRange = range(0, 50)

    for x in reversed(stepRange):
        print(".", end="", flush=True)
        q = calc_new_quality(x)
        # check if best yet seen quality differs more than current quality
        # and niqe has to be approached from top so best estimate must be >= target
        if (abs(currBest[0] - target)) > (abs(q - target)) and q >= target:
            currBest = (q, x)

    print(f"\n{img_in.split(os.sep)[-1]} -> {out.split(os.sep)[-1]}: Metric={currBest[0]} Quality={currBest[1]}")
    fn_compress(img_in, out, currBest[1])

    return currBest[1]
