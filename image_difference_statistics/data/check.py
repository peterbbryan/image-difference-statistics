import logging

import numpy as np


def check_8bit(imdata: np.ndarray) -> None:
    """
    Check whether values are uint8-ish.

    Args:
        imdata: Image data.
    Raises:
        AssertionError if not integer-ish.
    """

    assert imdata.ndim == 2, "Not grayscale"

    assert imdata.min() >= 0, "8 bit imagery"
    assert imdata.max() <= 255, "8 bit imagery"


def check_angle(angle: float) -> None:
    """
    Check whether angle is in range.

    Args:
        angle: Angle.
    Raises:
        AssertionError if outside range.
    """

    assert 0 <= angle <= 360, "Angle outside range"
