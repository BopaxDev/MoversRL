from enum import StrEnum

import torch
from torch.backends import mps


class EnhancedStrEnum(StrEnum):
    """
    A custom enumeration class with enhanced features.

    Methods:
        has(cls, key: str) -> bool: Check if a given key exists in the enumeration.
        list(cls) -> List[str]: Get a list of all values in the enumeration.
    """

    @classmethod
    def has(
        cls,
        key: str,
    ) -> bool:
        """
        Check if a given key exists in the enumeration.

        Parameters:
            key (str): The key to check.

        Returns:
            bool: True if the key exists, False otherwise.
        """

        return key in cls.__members__.values()

    @classmethod
    def list(cls) -> list[str]:
        """
        Get a list of all values in the enumeration.

        Returns:
            list[str]: A list of all values.
        """

        return list(cls.__members__.values())


def is_cuda_available():
    return torch.cuda.is_available()


def is_mps_available():
    return mps.is_available()


def get_device():
    if is_cuda_available():
        return torch.device(
            "cuda",
        )
    elif is_mps_available():
        return torch.device(
            "mps",
        )
    else:
        return torch.device(
            "cpu",
        )
