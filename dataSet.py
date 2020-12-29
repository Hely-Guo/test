import os
from torch.utils.data import Dataset

class modelDataset(Dataset):

    def __init__(self, base_path, train=True):
        super(modelDataset, self).__init__()