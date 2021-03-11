from dstoolbox.pipeline import PipelineY
import numpy as np
from sklearn.base import BaseEstimator
from sklearn.base import TransformerMixin
from sklearn.preprocessing import MinMaxScaler
from skorch import NeuralNetRegressor
import torch
from torch import nn
import torch.nn.functional as F


torch.manual_seed(7)


class MyModule(nn.Module):
    def __init__(self, num_inputs=2, num_layers=5, layer_width=10, num_outputs=3):
        super(MyModule, self).__init__()

        self.num_inputs = num_inputs
        self.layer_width = layer_width
        self.num_layers = num_layers
        self.num_outputs = num_outputs
        self.dense0 = nn.Linear(num_inputs, layer_width)
        self.dense1 = nn.Linear(layer_width, layer_width)
        self.output = nn.Linear(layer_width, num_outputs)


    def forward(self, X, **kwargs):
        X = (self.dense0(X))
        for n in range(self.num_layers):
            X = (self.dense1(X))
        X = F.sigmoid(self.output(X))
        return X


class Cast(BaseEstimator, TransformerMixin):
    def __init__(self, dtype):
        self.dtype = dtype

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        Xt = X.astype(self.dtype)
        return Xt


def create_pipeline(
    device='cpu',  # or 'cuda'
    max_epochs=50,
    lr=0.1,
    **kwargs
):
    return PipelineY([
        ('cast', Cast(np.float32)),
        ('scale', MinMaxScaler((-1, 1))),
        ('net', NeuralNetRegressor(
            module=MyModule,
            device=device,
            max_epochs=max_epochs,
            lr=lr,
            train_split=None,
            **kwargs,
        ))],
        #y_transformer=,
        # predict_use_inverse=True,
        )
