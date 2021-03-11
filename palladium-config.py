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

    'grid_search': {
        '!': 'skopt.BayesSearchCV',
        'estimator': {'__copy__': 'model'},
        'n_iter': 16,
        'search_spaces': {
            'net__lr': [1e-3, 1e-2, 1e-1],
            'net__max_epochs': [500],
            'net__module__layer_width': [8, 10, 12],
            'net__module__num_layers' : [5, 10, 20],
            },
        'cv': 5,
        'verbose': 4,
        'n_jobs': -1,

           #  'degree': {
           #      '!': 'skopt.space.Integer',
           #     'low': 1, 'high': 20,
           #  },
        },
        'return_train_score': True,
        'refit': False,
        'verbose': 4,
    }

