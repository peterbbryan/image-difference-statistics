"""
Rotational/translation Euclidean transforms.
"""

import numpy as np
from PIL import Image

from image_difference_statistics.data import check


def rotate(imdata: np.ndarray, angle: float) -> np.ndarray:
    """
    Rotate image. Fill missing values with mean.

    Args:
        imdata: Image data.
        angle: Angle.
    Returns:
        Rotated image.
    """

    check.check_8bit(imdata=imdata)
    check.check_angle(angle=angle)

    # fill the missing pixels with the mean value
    mean_value = int(imdata.mean())

    # rotate with PIL library
    pil_image = Image.fromarray(imdata)
    pil_image = pil_image.rotate(angle=angle, fillcolor=mean_value)

    return np.array(pil_image)
