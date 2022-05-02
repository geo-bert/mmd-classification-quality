from numpy import ndarray, array


class FeatureVector:
    """
    Feature-Vector used for image comparison
    """

    def __init__(self, histograms: list[tuple[ndarray, tuple[float, float, float]]], filepath: str = "MEM") -> None:
        self._histograms = histograms
        self._filepath = filepath

    @property
    def histograms(self) -> list[tuple[ndarray, tuple[float, float, float]]]:
        """
        Histograms of this feature vector

        Returns:
        List[
            hist (List[float]): The values of the histogram
            bin_min (float): The bin minimum of the histogram
            bin_max (float): The bin maximum of the histogram
            bin_width (float): The bin width of the histogram
        ]
        """
        return self._histograms

    @histograms.setter
    def histograms(self, new_value: list[tuple[list[float], tuple[float, float, float]]]) -> None:
        self._histograms = array(new_value)

    @histograms.deleter
    def histograms(self) -> None:
        del self._histograms

    @property
    def filepath(self) -> str:
        """
        Filepath to the stored file of this feature vector, or `MEM` if the feature vector was not loaded from a file

        Returns: (str) Filepath to the stored file of this feature vector, or `MEM` if not loaded from file
        """
        return self._filepath

    @filepath.setter
    def filepath(self, new_value: str) -> None:
        self._filepath = new_value

    @filepath.deleter
    def filepath(self) -> None:
        del self._filepath
