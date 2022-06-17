import os
import cProfile
from multiprocessing import Pool
from itertools import repeat

from classification import run_classification
from channel_enum import ChannelYUV
from config_generator import generate_configs
from feature_config import FeatureConfig
from setup import get_feature_vectors

KNN_K = 1


def run_experiment(paths: list[str], result_file: str):
    configs = generate_configs()
    print(f"Starting experiment for {len(configs)} configurations")
    for config in configs:
        run_specific_experiment(paths, result_file, config)


def run_specific_experiment(paths: list[str], result_file: str, config: FeatureConfig):
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
    base_path = "images/output/niqe_4.2"
    paths = [
        os.path.join(base_path, "heic"),
        os.path.join(base_path, "jp2"),
        os.path.join(base_path, "jpg"),
        os.path.join(base_path, "jxl"),
        os.path.join(base_path, "jxr"),
        os.path.join(base_path, "webp")

    ]
    run_experiment(paths, "experiments/experiment_results_niqe_4_2.csv")

    config = FeatureConfig(color_channel=ChannelYUV.V, block_size=6, bin_width=0.1, dct_coefficients=[
        (0,5),(1,1),(1,3),(1,5),(4,5),(5,0)
    ])
    run_specific_experiment(paths, "experiments/experiment_results_niqe_4_2_single.csv", config)


if __name__ == '__main__':
    # cProfile.runctx('main()', globals={'main': main}, locals={}, sort="tottime")
    main()
