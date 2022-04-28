
def binary_search(arr_q_steps, orig_img, wanted_quality, compression_func,quality_func, out_dir):
    low = 0
    high = len(arr_q_steps) - 1
    mid = 0
    best_estimate = (-1,float('inf'))
    
    def calc_new_quality():
        new_image = compression_func(orig_img, out_dir, mid)
        new_quality = quality_func(new_image,orig_img)
        print(f"calculated {new_quality} with quality option: {mid}")
        return  (new_quality)



    while low <= high:
 
        mid = (high + low) // 2

        currQ = calc_new_quality()
        
 
       
        if currQ < wanted_quality:
            low = mid + 1
 
        
        elif currQ > wanted_quality:
            high = mid - 1
 
        
        else:
            return (currQ,mid)
        
        # we need to approach quality from below and set new best estimate if
        if currQ < wanted_quality and (wanted_quality - currQ) < (wanted_quality - best_estimate[0]):
            best_estimate = (currQ,mid)  
 
    # return best estimate here because we will not find the quality spot on (not likely)
    return best_estimate

