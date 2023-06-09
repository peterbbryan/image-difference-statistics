"""
Distance for image comparison.
Low is similar. High is dissimilar.
"""

from functools import partial

import numpy as np


def _lp_metric(imdata_one: np.ndarray, imdata_two: np.ndarray, norm: int) -> float:
    """
    Lp norm metrics.

    Args:
        imdata_one: First image.
        imdata_two: Seconds image.
        norm: p norm.
    Returns:
        Lp norm distance.
    """

    raise NotImplementedError


l1 = partial(_lp_metric, norm=1)
l2 = partial(_lp_metric, norm=2)
