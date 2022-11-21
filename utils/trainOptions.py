import argparse

import torch.cuda


# train parameters
class TrainOptions:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self._setParameters()

    def __call__(self):
        self.parser.parse_args()

    def _setParameters(self):
        self.parser.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu',
                                 help='The device used for train. eg:cuda, cpu, cuda:0')
        self.parser.add_argument('--train-dir', default='dataset/train')
        self.parser.add_argument('--test-dir', default='dataset/test')
        self.parser.add_argument('--input-folder', default='LR')
        self.parser.add_argument('--target-folder', default='HR')
        self.parser.add_argument('--checkpoint', default='')
        self.parser.add_argument('--log-dir', default='logs/train_log')
        self.parser.add_argument('--lr', default=1e-4, type=float, help='The learning rate')
        self.parser.add_argument('--epoch', default=5, type=int)
        self.parser.add_argument('--seq-size', default=64, type=int)
        self.parser.add_argument('--scale', default=2, type=int)
        self.parser.add_argument('--border', default=3, type=int)
        self.parser.add_argument('--train-times', default=0, type=int)
        self.parser.add_argument('--test-times', default=0, type=int)
        self.parser.add_argument('--test-cycle', default=100, type=int)
        self.parser.add_argument('--save-cycle', default=500, type=int)
        self.parser.add_argument('--save-dir', default='checkpoint')

    def getOpts(self):
        return self.parser.parse_args()
