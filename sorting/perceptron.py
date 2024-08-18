"""This is code to implement basic linear perceptron"""

import torch
from torch import nn 

class Perceptron(nn.Module):
    """Class to implement simple perceptron"""
    
    def __init__(self, input_dim):
        super(Perceptron).__init__()
        self.fcl = nn.Linear(input_dim,1)
        