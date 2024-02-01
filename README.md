# WIP - First Neural Network
Neural Network From Scratch

For some fun, building an extremely basic neural network from scratch. 
Motivation behind this is to understand the math behind neural networks and how they work.
Math is assumed

This network is a classification network, and is trained on the classic MNIST dataset.
This dataset is a collection of 28x28 pixel images of handwritten digits, 0-9.
The network is trained to classify the images into their respective digits.

The network is built with 3 layers, an input layer, a hidden layer, and an output layer.
The input layer is 784 neurons, one for each pixel in the image.
The hidden layer is 16 neurons, and the output layer is 10 neurons, one for each digit.

The hidden layer is 16 neurons because it is a power of 2, and it is a small number.
The output layer is 10 neurons because there are 10 digits, 0-9.

The network is trained using backpropagation, and the weights are updated using gradient descent.

