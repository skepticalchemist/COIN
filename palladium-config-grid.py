{
    'dataset_loader_train': {
        '__factory__': 'dataset.ImageLoader',
        'path': 'data/kodim23.png',
    },

    'model_persister': {
        '__factory__': 'palladium.persistence.File',
        'path': 'models/model-{version}',
    },

    'model': {
        '__factory__': 'model.create_pipeline',
        'lr': 1e-2,
        'module__num_layers': 15,
        'module__layer_width': 52
        # YOUR CODE HERE:
        #
        # The new dataset has a different number of inputs and
        # outputs.  Adjust these parameters:
        #
        # 'module__num_inputs': 4,   # Number of features
        # 'module__num_outputs': 3,  # Number of classes
    },

    'grid_search': {
        '!': 'skopt.BayesSearchCV',
        'estimator': {'__copy__': 'model'},
        'n_iter': 16,
        'search_spaces': {
            "net__lr": {
                '!': 'skopt.space.Real',
                "low": 1e-6, "high": 1e1
            }
        },
        'return_train_score': True,
        'refit': False,
        'verbose': 4,
    }
}

