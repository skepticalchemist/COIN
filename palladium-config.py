{
    'dataset_loader_train': {
        '__factory__': 'dataset.ImageLoader',
        'path': 'data/kodim23.png',
    },

    'model_persister': {
        '__factory__': 'palladium.persistence.File',
        'path': 'models/model-{version}.pkl',
    },

    'model': {
        '__factory__': 'model.create_pipeline',
        'lr': 1e-2,
        'module__num_layers': 10,
        'module__layer_width': 28
        # YOUR CODE HERE:
        #
        # The new dataset has a different number of inputs and
        # outputs.  Adjust these parameters:
        #
        # 'module__num_inputs': 4,   # Number of features
        # 'module__num_outputs': 3,  # Number of classes
    },
}

