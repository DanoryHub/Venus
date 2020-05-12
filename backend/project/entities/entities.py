from dataclasses import dataclass


@dataclass
class ClothesEntity:
    id: int
    name: str
    blob_path: str
    color: str
    cloth_type: str
