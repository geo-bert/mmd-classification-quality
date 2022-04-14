from typing import Union

from channel_enum import ChannelYUV, ChannelRGB


class FeatureConfig:
    """
    Feature configuration used to generate FeatureVectors
    """

    def __init__(self, color_channel: Union[ChannelYUV, ChannelRGB], block_size: int, bin_width: float,
                 dct_coefficients: list[tuple[int, int]]) -> None:
        self._color_channel = color_channel
        self._block_size = block_size
        self._bin_width = bin_width
        self._dct_coefficients = dct_coefficients

    @property
    def color_channel(self) -> ChannelYUV:
        """
        The color channel to be used to get a feature vector

        Returns:
            Channel
        """
        return self._color_channel

    @color_channel.setter
    def color_channel(self, new_value: ChannelYUV) -> None:
        self._color_channel = new_value

    @color_channel.deleter
    def color_channel(self) -> None:
        del self._color_channel

    @property
    def block_size(self) -> int:
        """
        The dct block_size to be used to get a feature vector

        Returns:
            int
        """
        return self._block_size

    @block_size.setter
    def block_size(self, new_value: int) -> None:
        self._block_size = new_value

    @block_size.deleter
    def block_size(self) -> None:
        del self._block_size

    @property
    def dct_coefficients(self) -> list[tuple[int, int]]:
        """
        The dct coefficients to be used to get a feature vector

        Returns:
            list[tuple[int, int]]: The list of dct coefficients to use for feature vector extraction
        """
        return self._dct_coefficients

    @dct_coefficients.setter
    def dct_coefficients(self, new_value: list[tuple[int, int]]) -> None:
        self._dct_coefficients = new_value

    @dct_coefficients.deleter
    def dct_coefficients(self) -> None:
        del self._dct_coefficients

    @property
    def bin_width(self) -> float:
        """
        The histogram bin width to be used to get a feature vector

        Returns:
            int
        """
        return self._bin_width

    @bin_width.setter
    def bin_width(self, new_value: float) -> None:
        self._bin_width = new_value

    @bin_width.deleter
    def bin_width(self) -> None:
        del self._bin_width

    def get_feature_vec_filename(self, filename_prefix: str) -> str:
        return f"{filename_prefix}_ch_{self._color_channel.name}_blk_{self._block_size}_bin_{self._bin_width}" \
               f"_coeffs_{_coefficients_to_string(self.dct_coefficients)}"

    def __str__(self):
        return f"cfg{{ ch={self._color_channel.name}, bs={self._block_size}, " \
               f"c={self._dct_coefficients}, bw={self._bin_width} }}"


def _coefficient_to_string(coefficient: tuple[int, int]) -> str:
    coeff = coefficient
    return f"({coeff[0]}_{coeff[1]})"

def _coefficients_to_string(coefficients: list[tuple[int, int]]) -> str:
    s: str = ""
    for coeff in coefficients:
      s += _coefficient_to_string(coeff)

    return s
