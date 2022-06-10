import numpy as np


def resample_data_by_blocks(original_sample, blocks_length):
    n_rows_original = len(original_sample)
    block_labels = _get_labels(n_rows_original, blocks_length)
    rows = _get_rows(block_labels, n_rows_original, blocks_length)
    resample = original_sample.loc[rows, :]
    return resample


def _get_labels(n_rows_original, blocks_length):
    blocks_number = np.ceil(n_rows_original / blocks_length)
    block_labels = np.arange(blocks_number)
    return block_labels


def _get_rows(block_labels, n_rows_data, blocks_length):
    aux = np.arange(n_rows_data)
    rows = []
    for i in block_labels:
        rows.extend(aux[0 + i : blocks_length + i])
    return rows
