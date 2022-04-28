import os

from classification import run_classification
from feature_config import FeatureConfig
from setup import get_feature_vectors
from config_generator import generate_configs

KNN_K = 1

def run_experiment(paths: list[str], result_file: str):
  configs = generate_configs()
  print(f"Starting experiment for {len(configs)} configurations")
  for config in configs:
    feat_vecs = get_feature_vectors(paths, config)
    total_accuracy = run_classification(feat_vecs, KNN_K)
    _store_results(config, total_accuracy, result_file)


def _store_results(config: FeatureConfig, result: float, file: str):
  line = f"{result},{config.block_size},{config.color_channel},{config.bin_width},{config.dct_coefficients}\n"

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
  base_path = "example_images"
  paths = [
    os.path.join(base_path, "decompressed"),
    os.path.join(base_path, "original")
  ]
  run_experiment(paths, "experiment_results.csv")


if __name__ == '__main__':
  main()
