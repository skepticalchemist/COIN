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
        'lr': 2e-4,
        'module__num_layers': 10,
        'module__layer_width': 28,
        "iterator_train__shuffle": True
    },
}

