import os
import cProfile
from multiprocessing import Pool
from itertools import repeat

from classification import run_classification
from config_generator import generate_configs
from feature_config import FeatureConfig
from setup import get_feature_vectors

KNN_K = 1


def run_experiment(paths: list[str], result_file: str):
    configs = generate_configs()
    print(f"Starting experiment for {len(configs)} configurations")
    for config in configs:
        with Pool(8) as p:
            feat_vecs = p.starmap(get_feature_vectors, zip(paths, repeat(config)))
        total_accuracy = run_classification(feat_vecs, KNN_K)
        _store_results(config, total_accuracy, result_file)


def _store_results(config: FeatureConfig, result: float, file: str):
    coeffs = "".join(f"({coeff[0]}|{coeff[1]})" for coeff in config.dct_coefficients)
    line = f"{result:1.4f},{config.block_size},{config.color_channel},{config.bin_width},[{coeffs}]\n"

    if os.path.exists(file):
        with open(file, "a") as f:
            f.write(line)
    else:
        with open(file, "x") as f:
            f.write(
                "total_result,block_size,color_channel,bin_width,coefficients\n"
            )
            f.write(line)


def main():
    base_path = "images/output/psnr"
    paths = [
        os.path.join(base_path, "heic"),
        os.path.join(base_path, "jp2"),
        os.path.join(base_path, "jpg"),
        os.path.join(base_path, "jxl"),
        os.path.join(base_path, "jxr"),
        os.path.join(base_path, "webp")

    ]
    run_experiment(paths, "experiment_results.csv")


if __name__ == '__main__':
    cProfile.runctx('main()', globals={'main': main}, locals={}, sort="tottime")
    # main()
