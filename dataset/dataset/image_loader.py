import torch
import pydicom


def image_loader(path: str) -> torch.Tensor:
    ds = pydicom.dcmread(path)
    pixel_array = ds.pixel_array
    tensor = torch.from_numpy(pixel_array)
    scaled_tensor = normalize(tensor)
    interpolated_tensor = interpolate_negative_values(scaled_tensor)
    return interpolated_tensor


def normalize(tensor: torch.Tensor) -> torch.Tensor:
    raise NotImplementedError()


def interpolate_negative_values(tensor: torch.Tensor) -> torch.Tensor:
    raise NotImplementedError()

