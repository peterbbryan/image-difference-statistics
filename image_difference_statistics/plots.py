from typing import List

import matplotlib.pyplot as plt
import numpy as np


def imshow(imdata: np.ndarray) -> None:
    """
    Plot 8-bit imagery.

    Args:
        imdata: Image data.
    """

    assert imdata.min() >= 0, "8 bit imagery"
    assert imdata.max() <= 255, "8 bit imagery"

    imdata = np.squeeze(imdata)
    assert imdata.ndim == 2, f"Invalid shape: {imdata.shape()}"

    plt.imshow(imdata, clim=(0, 255), cmap="gray")
    plt.axis("off")


def imshow_many(imdata_list: List[np.ndarray]) -> None:
    """
    Plot a list of 8-bit images.

    Args:
        imdata_list: List of image data to plot.
    """

    n_images = len(imdata_list)

    for ind, imdata in enumerate(imdata_list, 1):

        plt.subplot(1, n_images, ind)
        imshow(imdata=imdata)
        