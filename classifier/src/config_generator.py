from random import Random, random
from channel_enum import ChannelYUV
from feature_config import FeatureConfig

SMALLEST_BLOCK_SIZE = 6
BIGGEST_BLOCK_SIZE = 14
BLOCK_SIZE_INCREMENT = 2

RANDOM_COEFF_ITERATION_PER_CONFIG = 5
MAX_NR_ADDITIONAL_COEFFS_PER_CONFIG = 4 # excluding DC

MAX_NR_CONFIGS = 100

def generate_configs(max_nr: int = MAX_NR_CONFIGS) -> list[FeatureConfig]:
  base_config = FeatureConfig(ChannelYUV.Y, 7, 0.1, [(2, 2)])

  configs = _prepare_multiple_block_sizes(base_config)
  
  configs2 = []
  for config in configs:
    configs2.extend(_prepare_random_coefficient_group(config))
  
  configs = []
  for config in configs2:
    configs.extend(_prepare_channels(config))

  return configs[0:max_nr]


def _prepare_multiple_block_sizes(feature_config: FeatureConfig) -> list[FeatureConfig]:
  configs: list[FeatureConfig] = []
  for i in range(SMALLEST_BLOCK_SIZE, BIGGEST_BLOCK_SIZE + BLOCK_SIZE_INCREMENT, BLOCK_SIZE_INCREMENT):
    configs.append(FeatureConfig(feature_config.color_channel, i,
                                          feature_config.bin_width,
                                          feature_config.dct_coefficients))
  return configs


def _prepare_channels(feature_config: FeatureConfig) -> list[FeatureConfig]:
  configs: list[FeatureConfig] = [
    FeatureConfig(ChannelYUV.Y, feature_config.block_size, feature_config.bin_width,
                  feature_config.dct_coefficients),
    FeatureConfig(ChannelYUV.U, feature_config.block_size, feature_config.bin_width,
                  feature_config.dct_coefficients),
    FeatureConfig(ChannelYUV.V, feature_config.block_size, feature_config.bin_width,
                  feature_config.dct_coefficients),
  ]
  return configs


def _prepare_random_coefficient_group(feature_config: FeatureConfig) -> list[FeatureConfig]:
  configs: list[FeatureConfig] = []
  coefficients: list[tuple[int, int]] = []
  random = Random(1234) # fix seed helps for reproducability

  for i in range(0, feature_config.block_size):
    for j in range(0, feature_config.block_size):
      coefficients.append((i,j))

  for _ in range(RANDOM_COEFF_ITERATION_PER_CONFIG):  
    nr_of_coeffs = random.randint(1, min(feature_config.block_size, MAX_NR_ADDITIONAL_COEFFS_PER_CONFIG))
    coeff_indizes_to_take: set[int] = { 0 } # DC coeff is always used
    for _ in range(nr_of_coeffs):
      index = random.randint(0, len(coefficients) - 1)
      coeff_indizes_to_take.add(index)

    coeffs_to_take = []
    for index in coeff_indizes_to_take:
      coeffs_to_take.append(coefficients[index])

    configs.append(FeatureConfig(feature_config.color_channel, 
      feature_config.block_size, feature_config.bin_width, coeffs_to_take))

  return configs


def main():
  configs: list[FeatureConfig] = generate_configs(MAX_NR_CONFIGS)
  for config in configs:
    print(f"Config: block_size={config.block_size}, bin_width={config.bin_width}, color_channel={config.color_channel}, coeffs={config.dct_coefficients}")

  print(f"Generated {len(configs)} configs")


if __name__ == '__main__':
  main()