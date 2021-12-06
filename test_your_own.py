import time
import numpy as np
import h5py
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from scipy import ndimage
from helper_function import predict 

num_px =64

def test_your_own(image_name, parameters, classes):
    ## START CODE HERE ##
    my_image = "syna" + ".jpg" # change this to the name of your image file 
    my_label_y = [0] # the true class of your image (1 -> cat, 0 -> non-cat)
    ## END CODE HERE ##

    fname = my_image
    image = np.array(Image.open(fname).resize((num_px, num_px)))
    plt.imshow(image)
    image = image / 255.
    image = image.reshape((1, num_px * num_px * 3)).T

    my_predicted_image = predict(image, my_label_y, parameters)

    print ("y = " + str(np.squeeze(my_predicted_image)) + ", your L-layer model predicts a \"" + classes[int(np.squeeze(my_predicted_image)),].decode("utf-8") +  "\" picture.")