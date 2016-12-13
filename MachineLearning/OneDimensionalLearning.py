#
# This is a program that performs a polynomial fit on a set of properly formatted data from a text file
# through a process called 'gradient descent.' Once the process finishes analyzing the data, it plots the
# data as well as the polynomial function it comes up with, and outputs the coefficients. The code is heavily
# based on the MATLAB gradient descent algorithm presented in Andrew Ng's Stanford Computer Science course on
# Machine Learning.
#
# name: Jacob Nazarenko
# email: jacobn@bu.edu
#

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# This is a function that simply plots whatever data is fed to it, along with some custom pyplot parameters
def plot_data(x_vals, y_vals, t, ms, x_label="Magnitude", y_label="Total Damage (Millions of Dollars)"):
    plt.plot(x_vals, y_vals, t, markersize=ms)
    plt.axis([0, max(x_vals) + 10, min(y_vals) - 10, max(y_vals) + 10])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.autoscale()

# This function computes the cost of a set of coefficients by 'vectorizing' them (turning them into a matrix)
# and seeing what the using a version of the mean square error function
def compute_cost(x_val_mat, y_val_mat, theta):
    m = y_val_mat.size
    H = theta * x_val_mat
    S = np.sum(np.asarray(H - y_val_mat)**2, axis=1)[0]  # mean square error function applied to polynomial
    return S/(2*m)  # J (cost) value

# This function performs the crucial main process known as gradient descent, in which it subtracts a small
# portion of the gradient from the estimated coefficients many time while updating the coefficients themselves
def gradient_descent(x_val_mat, y_val_mat, theta, iterations, alpha):
    print("Performing gradient descent...")
    m = y_val_mat.size
    for i in tqdm(range(0, iterations), desc="Percentage Completed"):
        HY = (theta * x_val_mat) - y_val_mat  # this line and the next line are the gradient
        SA = HY * x_val_mat.transpose()
        SA *= alpha/m  # gradient multiplied by alpha
        theta = theta - SA  # small portion of gradient subtracted
        if np.any(np.isnan(theta)):
            raise ValueError("Smaller learning rate needed!")
    return theta

# This is the main process that takes in data, formats it, and ensures that the gradient descent operation
# goes smoothly
def learn(iterations=150000, learning_rate=0.1):
    succeeded = False
    infile = input("Name of formatted data file: ")  # data file input goes here
    # data formatting...
    xvals, yvals = np.loadtxt(infile, delimiter=",", unpack=True)
    degree = int(input("Degree of polynomial: "))
    theta = "0 " * degree + "0"
    theta = np.matrix(theta)
    x_vals = [np.ones(len(xvals))]
    for d in range(1, degree+1):
        x_vals = np.append(x_vals, [xvals**d], axis=0)
    x_val_mat = np.matrix(x_vals)
    y_val_mat = np.matrix(yvals)
    plot_data(xvals, yvals, "rs", 6.0)
    cost = compute_cost(x_val_mat, y_val_mat, theta)
    print("Initial cost: " + str(cost))
    theta_new = theta
    while not succeeded:  # automatically adjusts the learning rate so as not to overshoot in the end
        try:
            print("Current learning rate: " + str(learning_rate))
            theta_new = np.asarray(gradient_descent(x_val_mat, y_val_mat, theta, iterations, learning_rate))[0]
            print("Theta values found: " + str(theta_new))
            succeeded = True
        except ValueError:
            print("Learning rate too large, trying a smaller one...")
            learning_rate /= 10
    cost_new = compute_cost(x_val_mat, y_val_mat, theta_new)
    print("Final cost: " + str(cost_new))
    template = np.arange(min(xvals) - 10, max(xvals) + 10, 0.2)
    function = theta_new[0]
    for l in range(1, len(theta_new)):
        function += theta_new[l]*(template**l)
    plot_data(template, function, "b-", 6.0)
    print("Plotting data...")   # plots data + polynomial and spits out coefficients
    plt.show()
    return theta_new

if __name__=="__main__":
    learn()