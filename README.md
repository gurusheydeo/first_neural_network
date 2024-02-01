# WIP - First Neural Network
Neural Network From Scratch

For some fun, building an extremely basic neural network from scratch. 
Motivation behind this is to understand the math behind neural networks and how they work.
Math is assumed

This network is a classification network, and is trained on the classic MNIST dataset.
This dataset is a collection of 28x28 pixel images of handwritten digits, 0-9.
The network is trained to classify the images into their respective digits.

The network is built with 4 layers, an input layer, 2 hidden layers, and an output layer.
* The input layer is 784 neurons, one for each pixel in the image,
* The first hidden layer is 512 neurons, 
* The second hidden layer is 256 neurons, 
* The Output layer is 10 neurons - one for each digit.

The network is trained using backpropagation, and the weights are updated using gradient descent.

The data will be imported using the `python-mnist` library, and the network will be built using `numpy`.
