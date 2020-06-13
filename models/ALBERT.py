import torch
import torch.nn.functional as F
import torch.nn as nn
from torch.nn.parameter import Parameter

import numpy as np
import scipy.stats as st


def probability(n, N):
    s = 0
    for k in range(1, N, 1):
        s = s + (1/k)

    return (1/n)/s
