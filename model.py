from dstoolbox.pipeline import Pipeline
import numpy as np
from sklearn.base import BaseEstimator
from sklearn.base import TransformerMixin
from sklearn.preprocessing import MinMaxScaler
from skorch import NeuralNetRegressor
from skopt import BayesSearchCV
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

        self.input = nn.Linear(self.num_inputs, self.layer_width)
        self.layer_dict = {}
        for n in range(1, self.num_layers):
            self.layer_dict["dense_"+str(n)] = nn.Linear(self.layer_width, self.layer_width)

        self.output = nn.Linear(self.layer_width, self.num_outputs)


    def forward(self, X, **kwargs):
        # print(X)
        X = self.input(X)
        X = torch.sin(X)
        for n in range(1,self.num_layers):
            X = self.layer_dict["dense_"+str(n)](X)
            X = torch.sin(X)
        X = self.output(X)
        # print(X.shape)
        X = torch.sigmoid(X)
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
    lr=2e-4,
    **kwargs
):
    return Pipeline([
        ('cast', Cast(np.float32)),
        ('scale', MinMaxScaler((-1, 1))),
        ('net', NeuralNetRegressor(
            module=MyModule,
            device=device,
            max_epochs=max_epochs,
            lr=lr,
            train_split=None,
            optimizer=torch.optim.Adam,
            **kwargs,
        ))]
        )
