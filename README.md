# Cat Classifier Using Neural Networks
College project to classify pictures as cat or non-cat pictures using Neural network core coding in python.

# Abstract
## Background 
The images are represented as matrices in computer storage and to identy whether there is a cat or not in a picture is not a simple task for a machine as it is for humans. So, here a neural network implementation is used that basically mimics the human brain and allows the machine to learn by itself how to classify a picture as whether it is a cat or a non-cat picture.

## Objective
A Neural Network model is built to classify the images as cat or non cat. 

## Methods
The complete implementation is written with different functions to load the data, preprocess the data, data labelling, gradient descent, cost function and everything (which is given in helper_functions.py. The final model is assembled in final_model.py. For this project I have used binary cross enthropy loss function. Here i have used relu activations for all the layers except the last layer where a sigmoid function is used.

## Results
The neural network models built here is tested on standard datasets, and the metric area under the curve of 80% was observed with a training acuuracy of 98%.

## Conclusions
A Classification model is built that could look to a picture and identify it as cat or non-cat picture
