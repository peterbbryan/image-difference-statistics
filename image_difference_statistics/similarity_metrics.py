"""
Metrics for image comparison. 
Low is dissimilar. High is similar.
"""

import numpy as np
from skimage import metrics


def ssim(imdata_one: np.ndarray, imdata_two: np.ndarray) -> float:
    """
    Structural similarity index measure.
    
    Args:
        imdata_one: First image.
        imdata_two: Seconds image.
    Returns:
        SSIM.    
    """

    return metrics.structural_similarity(imdata_one, imdata_two)


def normalized_mutual_information(imdata_one: np.ndarray, imdata_two: np.ndarray) -> float:
    """
    Normalized mutual information.
    
    Args:
        imdata_one: First image.
        imdata_two: Seconds image.
    Returns:
        Normalized mutual information.
    """

    return metrics.normalized_mutual_information(imdata_one, imdata_two)

