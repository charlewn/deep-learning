import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_path = 'Bike-Sharing-Dataset/hour.csv'

rides = pd.read_csv(data_path)

rides.head()

def sigmoid(x):
	return 1/(1+np.exp(-x))

def sigmoid_prime(x):
	return sigmoid(x) * (1-sigmoid(x))


inputs = np.array([0.7, -0.3])
weights = np.array([0.1, 0.8])
bias = -0.1

x = np.array([0.1, 0.3])
y = 0.2
weights = np.array([-0.8, 0.5])
#the learning rate, eta in the weight step equation
learnrate =0.5

output = sigmoid(np.dot(weights, inputs)+bias)

nn_output = sigmoid(x[0]*weights[0] + x[1]*weights[1])

error = y - nn_output

error_grad = error * sigmoid_prime(np.dot(x,weights))

del_w = [learnrate * error_grad * x[0], learnrate * error_grad * x[1]]

#implement gradient descent
#weights = np.random.normal(scale=1/n_features**.5, size=n_features)
#output_in = np.dot(weights, inputs)

from data_prep import features, targets, features_test, targets_test

# Use to same seed to make debugging easier
np.random.seed(42)

n_records, n_features = features.shape
last_loss = None

# Initialize weights
weights = np.random.normal(scale=1 / n_features**.5, size=n_features)

# Neural Network hyperparameters
epochs = 1000
learnrate = 0.5
for e in range(epochs):
    del_w = np.zeros(weights.shape)
    for x, y in zip(features.values, targets):
        # Loop through all records, x is the input, y is the target

        # TODO: Calculate the output
        output = sigmoid(np.dot(x, weights))

        # TODO: Calculate the error
        error =  y - output

        # TODO: Calculate change in weights
        del_w += error * output * (1 - output) * x

        # TODO: Update weights
    weights += 0
    
    # Printing out the mean square error on the training set
    if e % (epochs / 10) == 0:
        out = sigmoid(np.dot(features, weights))
        loss = np.mean((out - targets) ** 2)
        if last_loss and last_loss < loss:
            print("Train loss: ", loss, "  WARNING - Loss Increasing")
        else:
            print("Train loss: ", loss)
        last_loss = loss


# Calculate accuracy on test data
tes_out = sigmoid(np.dot(features_test, weights))
predictions = tes_out > 0.5
accuracy = np.mean(predictions == targets_test)
print("Prediction accuracy: {:.3f}".format(accuracy))

print("Output:")
print(output)

print(del_w)

