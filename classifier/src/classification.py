import numpy as np

from channel_enum import *
from feature_vector import FeatureVector
from progress import ProgressBar


def run_classification(grouped_features: list[dict[str, FeatureVector]], k: int) -> float:
  '''
  Runs experiment with K nearest neighbors (KNN) and leave one out cross validation

  Returns:
      float: Accuracy of the experiment. 0 to 1 with 1 being 100% accuracy.
  '''

  features_length = len(grouped_features[0])
  for features in grouped_features:
    if features_length != len(features):
      print("ERROR: All groupes must have the same number of features")
      exit(1)

  print("Classifying vectors...")
  print()

  correct_cnt = []
  for group_index in range(len(grouped_features)):
    correct_cnt.append(_count_correct_classification(group_index, grouped_features, k))

  print()
  print("Finished classification. Results:")
  return _print_accuracy(correct_cnt, features_length)


def _print_accuracy(correct_cnt: list[int], features_length: int) -> float:
  number_of_groups = len(correct_cnt)
  overall_correct = 0
  for i, correct in enumerate(correct_cnt):
    overall_correct += correct
    print(f"Accuracy of group {i}: {correct / float(features_length):.3%}")
  
  total = overall_correct / float(number_of_groups * features_length)
  print(f"Overall Accuracy: {total:.3%}")
  print()
  return total


def _count_correct_classification(group_index: int, grouped_features: list[dict[str, FeatureVector]], k: int) -> int:
  '''
  Classification using leave one out cross validation for a given index of the grouped features.

  Returns:
      int: Number of correctly classified vectors.
  '''
  if group_index < 0 or len(grouped_features) <= group_index:
    print("Bad group index" + group_index)
    exit(1)

  progress = ProgressBar(len(grouped_features[0]), f"Classification for group {group_index}:")
  wrong_names = []
  correct = 0
  wrong_names = []
  for count, key in enumerate(grouped_features[group_index].copy(), start=1):
    progress.print_progress(count)
    features_with_key = grouped_features[group_index].copy()
    grouped_features[group_index].pop(key)

    classified_index = run_single_experiment(features_with_key[key], grouped_features, k)
    if classified_index == group_index:
      correct += 1
    else:
      wrong_names.append(features_with_key[key].filepath)

    # restore list
    grouped_features[group_index] = features_with_key

  print()
  wrong_names = list(map(lambda x: x.split("/")[-1], wrong_names))
  print(f"Wrong in group {group_index}: ", wrong_names)
  return correct


def run_single_experiment(test_vector: FeatureVector, grouped_features: list[dict[str, FeatureVector]], k: int) -> int:
  """
  Runs a single experiment with K nearest neighbors (KNN) on the given test feature vector

  Args:
          test_vector (FeatureVector): The test feature vector used for this experiment
          feature_vectors (List[FeatureVector]): List of grouped feature vectors
          k (int): The K for KNN

  Returns:
          int: Index of the group the test vector is classified to.
  """
  if len(grouped_features[0]) < k:
      raise Exception("Feature lists too small for k={}!", k)

  k_grouped_euclids = []
  for features in grouped_features:
    k_grouped_euclids.append(_find_k_min_euclid(test_vector, features.values(), k))

  return _get_nearest_group(k_grouped_euclids)


def _get_nearest_group(k_grouped_euclids: list[list[float]]) -> int:
  group_indizes = [0] * len(k_grouped_euclids)
  for _ in range(len(k_grouped_euclids)):
    _update_smallest_group_index(group_indizes, k_grouped_euclids)

  return _get_nearest_group_index(group_indizes)


def _update_smallest_group_index(group_indizes: list[int], k_grouped_euclids: list[list[float]]):
  curr_smallest_per_group = []
  for i, curr_smallest in enumerate(group_indizes):
    if curr_smallest >= len(k_grouped_euclids[i]):
      # smallest already found
      return

    curr_smallest_per_group.append(k_grouped_euclids[i][curr_smallest])

  index = 0
  for i in range(len(curr_smallest_per_group)):
    if curr_smallest_per_group[i] < curr_smallest_per_group[index]:
      index = i

  group_indizes[index] += 1

  
def _get_nearest_group_index(group_indizes: list[int]) -> int:
  index = 0
  for i in range(len(group_indizes)):
    if group_indizes[i] > group_indizes[index]:
      index = i

  return index

def _find_k_min_euclid(test_vector: FeatureVector, cmp_vectors: list[FeatureVector], k: int) -> list[float]:
  """
  Find the k feature vectors from cmp_vectors that have the smallest euclidean distance to test_vector.

  Args:
      test_vector (FeatureVector): The test feature vector
      cmp_vectors (List[FeatureVector]): An euclidean distance is created between every vector of this list
                                          and test_vector
      k (int): Length of the returned list

  Returns:
          List[float]: The k euclidean distances of feature vectors of cmp_vectors that have the smallest
                        euclidean distance to test_vector
  """
  euclids = []
  for vec in cmp_vectors:
      euclids.append(_get_euclidean_distance(test_vector, vec))

  asc_sorted_euclids = sorted(euclids)
  return asc_sorted_euclids[:k]



def _get_euclidean_distance(left_vector: FeatureVector, right_vector: FeatureVector) -> float:
  """
  Calculates the euclidean distance between two feature vectors.

  euclid: sqrt((pt_x1 - pt_y1)^2 + (pt_x2 - pt_y2)^2 + ... + (pt_xn - pt_yn)^2)

  Args:
          left_vector (FeatureVector): The left feature vector
          right_vector (FeatureVector): The right feature vector

  Returns:
          float: Euclidean distance between the left and right feature vector
  """
  if len(left_vector.histograms) != len(right_vector.histograms):
      raise Exception("Histograms of the two feature vectors differ in length!")

  euclid = 0.
  for left, right in zip(left_vector.histograms, right_vector.histograms):
      left_arr, (left_min, left_max, left_bin) = left
      right_arr, (right_min, right_max, right_bin) = right

      if left_bin != right_bin:
          raise ValueError("Can't use different bin widths")

      if left_min < right_min:
          right_arr = np.concatenate([np.zeros(int(round(abs(left_min - right_min) / left_bin))), right_arr])
      elif right_min < left_min:
          left_arr = np.concatenate([np.zeros(int(round(abs(left_min - right_min) / left_bin))), left_arr])

      if left_max < right_max:
          left_arr = np.concatenate([left_arr, np.zeros(int(round(abs(left_max - right_max) / left_bin)))])
      elif right_max < left_max:
          right_arr = np.concatenate([right_arr, np.zeros(int(round(abs(left_max - right_max) / left_bin)))])

      euclid += np.linalg.norm(left_arr - right_arr)
  return euclid



def main():
  groups = []
  for i in range(0, 6, 2):
    features = {}
    features["vec1"] = FeatureVector([(np.array([i]), (1,1,1))])
    features["vec2"] = FeatureVector([(np.array([i]), (1,1,1))])
    features["vec3"] = FeatureVector([(np.array([i+1]), (1,1,1))])
    groups.append(features)

  run_classification(groups, k=2)


if __name__ == '__main__':
  main()
