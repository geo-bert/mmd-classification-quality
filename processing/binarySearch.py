def binary_search(arr_q_steps, orig_img, wanted_quality, compression_func, quality_func, out_dir):
    low = 0
    high = len(arr_q_steps) - 1
    mid = 0
    best_estimate = (-1, float('inf'))

    def calc_new_quality():
        new_image = compression_func(orig_img, out_dir, mid)
        new_quality = quality_func(new_image, orig_img)
        print(f"calculated {new_quality} with quality option: {mid}")
        return new_quality

    while low <= high:

        mid = (high + low) // 2

        curr_q = calc_new_quality()

        if curr_q < wanted_quality:
            low = mid + 1
        elif curr_q > wanted_quality:
            high = mid - 1
        else:
            return curr_q, mid

        # we need to approach quality from below and set new best estimate if
        if curr_q < wanted_quality and (wanted_quality - curr_q) < (wanted_quality - best_estimate[0]):
            best_estimate = (curr_q, mid)

            # return best estimate here because we will not find the quality spot on (not likely)
    return best_estimate
