import quality_metrics;
import binarySearch
import compression_singles

orig_image = "../example_images/original/Buildings.0001.png"
out_dir = "../test"
watned_psnr = 42
possible_quals = list(range(1, 100))

result = binarySearch.binary_search(possible_quals, orig_image, watned_psnr, compression_singles.single_compression_jpg,
                                    quality_metrics.psnr, out_dir)

print(result)
