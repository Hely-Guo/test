import os
import sys
import time
import cv2

import torch
import numpy as np
from dataSet import modelDataset

class layoutAnalyse:

    SAVE_PATH = ''
    SAVE_NAME = ''
    TARGET_IMAGE_PATH = ''

    def __int__(self, img_path):
        self.img_path = img_path

        # 准备数据集
        self.dataset = modelDataset(base_path=img_path, train=False)

        # 建立dataloader
        self.dataloader = torch.utils.data.DataLoader(dataset=train_set, batch_size=1, num_workers=1, shuffle=False)

        # 加载模型
        self.model = None

        model.eval()

    def modelSet(self):
        return

    def get_one_hot(self, label, N):
        return

    def save_image(self, img, num, dir):
        return

    def analyse(self):
        self.modelSet()

        for num, i in enumerate(self.dataset):
            x = torch.Tensor(i['target_image'][np.newaxis, :, :,:])
            output = self.model(x)

            _, pred = torch.topk(output)
