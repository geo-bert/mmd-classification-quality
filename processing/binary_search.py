def search_fr(orig_img, wanted_quality, compression_func, quality_func, out_dir, from_below = True):
    low = 0
    high = 100
    mid = 0
    best_estimate = (-1, float('inf'))
    
    #when approaching from above the intial best estimates needs to be infinite for the calculation below
    if not from_below:
        best_estimate = (float('inf'),float('inf'))
        
    def calc_new_quality():
        new_image = compression_func(orig_img, out_dir, mid)
        new_quality = quality_func(new_image, orig_img)
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

        if from_below:
            # we need to approach quality from below and set new best estimate if
            if curr_q < wanted_quality and (wanted_quality - curr_q) < (wanted_quality - best_estimate[0]):
                best_estimate = (curr_q, mid)
        else:
            # we need to approach quality from above and set new best estimate if
            if curr_q > wanted_quality and (curr_q - wanted_quality) < (best_estimate[0] - wanted_quality):
                best_estimate = (curr_q, mid)

        print(f"Best: {best_estimate}, curr_q: {curr_q}, mid: {mid}")
            # return best estimate here because we will not find the quality spot on (not likely)
    print(f"{orig_img} -> {out_dir}: Metric={best_estimate} Quality={mid}")
    return best_estimate
