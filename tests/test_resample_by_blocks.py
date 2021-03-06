import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from bootstrapping_tools import random_resample_data_by_blocks
import random


def test_random_resample_data_by_blocks():
    random.seed(2)
    blocks_length = 4
    block_size_4 = Tester_By_Size_Blocks(blocks_length)
    block_size_4.set_expected(
        [20, 30, 40, 50, 20, 30, 40, 50], [700, 800, 900, 1000, 700, 800, 900, 1000]
    )
    block_size_4.assert_random_resampled_by_blocks()


def test_length_block_labels():
    blocks_length = 5
    lenght_block_labels = 1
    block_size_4 = Tester_By_Size_Blocks(blocks_length)
    block_size_4.set_expected([10, 20, 30, 40, 50], [600, 700, 800, 900, 1000])
    n_rows_data = len(block_size_4.data)
    blocks_number = np.ceil(n_rows_data / blocks_length)
    assert lenght_block_labels <= blocks_number


class Tester_By_Size_Blocks:
    def __init__(self, blocks_length):
        self.blocks_length = blocks_length
        self.expected = None
        self.data = None
        self._set_data()

    def assert_random_resampled_by_blocks(self):
        obtained = random_resample_data_by_blocks(self.data, self.blocks_length)
        assert_frame_equal(self.expected, obtained)

    def set_expected(self, column_a, column_b):
        self.expected = self._data_from_columns(column_a, column_b).reset_index(drop=True)

    def _set_data(self):
        self.data = self._data_from_columns(np.arange(10, 60, 10), np.arange(600, 1100, 100))

    def _data_from_columns(self, column_a, column_b):
        return pd.DataFrame({"a": column_a, "b": column_b})
