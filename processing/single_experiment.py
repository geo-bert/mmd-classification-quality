import quality_metrics;
import binarySearch
import compression_singles


def single_experiment(arr_q_steps, orig_img, wanted_quality, compression_func,quality_func, out_dir):
    result = binarySearch.binary_search(arr_q_steps, orig_img, wanted_quality, compression_func, quality_func, out_dir)

    #create best estimate compression image
    #binary search function returns (best_estimate_quality,q_flag_for_this_metric)
    return compression_func(orig_image, out_dir, result[1])


orig_image = "../example_images/original/Buildings.0001.png"
out_dir = "../test"
wanted_psnr = 42
possible_quals = list(range(1, 100))

res = single_experiment(possible_quals,orig_image,wanted_psnr,compression_singles.single_compression_jpg,quality_metrics.psnr,out_dir)


print(res)


