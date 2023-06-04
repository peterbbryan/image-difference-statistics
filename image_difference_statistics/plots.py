"""
Plotting functions.
"""

from typing import List

import matplotlib.pyplot as plt
import numpy as np

from image_difference_statistics.data import check


def imshow(imdata: np.ndarray) -> None:
    """
    Plot 8-bit imagery.

    Args:
        imdata: Image data.
    """

    check.check_8bit(imdata=imdata)

    plt.imshow(imdata, clim=(0, 255), cmap="gray")
    plt.axis("off")


def imshow_many(imdata_list: List[np.ndarray]) -> None:
    """
    Plot a list of 8-bit images.

    Args:
        imdata_list: List of image data to plot.
    """

    n_images = len(imdata_list)

    for ind, imdata in enumerate(imdata_list):
        check.check_8bit(imdata=imdata)

        plt.subplot(1, n_images, ind + 1)
        plt.title(ind)
        imshow(imdata=imdata)
