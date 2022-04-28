import glob
import os

from channel_enum import ChannelYUV
from feature_config import FeatureConfig
from feature_extraction import FeatureExtractor
from feature_vector import FeatureVector
from progress import ProgressBar


def get_feature_vectors(paths: list[str], feature_config: FeatureConfig) -> list[dict[str, FeatureVector]]:
    feature_extractor = FeatureExtractor(feature_config)
    features = []
    for path in paths:
        features.append(_get_feature_vectors_of_path(path, feature_extractor))

    return features


def _get_feature_vectors_of_path(path: str, feature_extractor: FeatureExtractor) -> dict[str, FeatureVector]:
    imgs = glob.glob('*.png', root_dir=path)
    vector_dict = {}
    progress = ProgressBar(len(imgs), f"Creating feature vectors of PNGs in {path:>7}:")
    for count, img in enumerate(imgs, start=1):
        img_path = os.path.join(path, img)
        progress.print_progress(count)
        feat_vec = feature_extractor.extract_feature_vector(img_path)
        vector_dict[img_path] = feat_vec

    print()
    return vector_dict


def main():
    feat_conf = FeatureConfig(ChannelYUV.Y, 20, 1, [(2, 2)])
    feature_groups = get_feature_vectors(["example_images/decompressed"], feat_conf)
    for features in feature_groups:
        for (_, vec) in features.items():
            print(vec.filepath)


if __name__ == '__main__':
    main()
