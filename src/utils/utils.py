import torch
from torch.backends import mps


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
