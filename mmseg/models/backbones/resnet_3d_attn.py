import torch.nn as nn
from ..builder import BACKBONES

@BACKBONES.register_module
class ResNet3DAttn(nn.Module):

    def __init__(self, arg1, arg2):
        pass

    def forward(self, x):  # should return a tuple
        pass

    def init_weights(self, pretrained=None):
        pass

