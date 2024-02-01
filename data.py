import numpy as np

with np.load('data/mnist.npz', allow_pickle=True) as f:
    train_X, train_y = f['x_train'], f['y_train']
    test_X, test_y = f['x_test'], f['y_test']
