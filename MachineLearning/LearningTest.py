import numpy as np
import matplotlib.pyplot as plt

def plot_data(x_vals, y_vals, t, ms, x_label="Dependent", y_label="Independent"):
    plt.plot(x_vals, y_vals, t, markersize=ms)
    plt.axis([0, max(x_vals) + 10, min(y_vals) - 10, max(y_vals) + 10])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.autoscale()

def compute_cost(x_val_mat, y_val_mat, theta):
    m = y_val_mat.size
    H = theta * x_val_mat
    S = np.sum(np.asarray(H - y_val_mat)**2, axis=1)[0]
    return S/(2*m)  # J (cost) value

def gradient_descent(x_val_mat, y_val_mat, theta, iterations, alpha):
    print "Performing gradient descent... "
    m = y_val_mat.size
    for i in range(0, iterations):
        HY = (theta * x_val_mat) - y_val_mat
        SA = HY * x_val_mat.transpose()
        SA *= alpha/m
        theta = theta - SA
        if i%(iterations/100) == 0:
            print str((float(i)/float(iterations))*100)+"% finished... "
        if np.any(np.isnan(theta)):
            raise ValueError("Smaller learning rate needed!")
    return theta

def learn(degree=1, iterations=1500000, learning_rate=0.01):
    succeeded = False
    theta = "0 "*degree + "0"
    theta = np.matrix(theta)
    # infile = input("Name of formatted data file: ")
    # xvals, yvals = np.loadtxt(infile, delimiter=",", unpack=True)
    xvals, yvals = np.loadtxt("ex1data1.txt", delimiter=",", unpack=True)
    x_vals = [np.ones(len(xvals))]
    for d in range(1, degree+1):
        x_vals = np.append(x_vals, [xvals**d], axis=0)
    x_val_mat = np.matrix(x_vals)
    y_val_mat = np.matrix(yvals)
    plot_data(xvals, yvals, "rs", 6.0)
    cost = compute_cost(x_val_mat, y_val_mat, theta)
    print "Initial cost: " + str(cost)
    theta_new = theta
    while not succeeded:
        try:
            print "Current learning rate: " + str(learning_rate)
            theta_new = np.asarray(gradient_descent(x_val_mat, y_val_mat, theta, iterations, learning_rate))[0]
            print "Theta values found: " + str(theta_new)
            succeeded = True
        except ValueError:
            print "Learning rate too large, trying a smaller one... "
            learning_rate /= 10
    cost_new = compute_cost(x_val_mat, y_val_mat, theta_new)
    print "Final cost: " + str(cost_new)
    template = np.arange(min(xvals) - 10, max(xvals) + 10, 0.2)
    function = theta_new[0]
    for l in range(1, len(theta_new)):
        function += theta_new[l]*(template**l)
    plot_data(template, function, "b-", 6.0)
    print "Plotting data... "
    plt.show()
    return theta_new

if __name__=="__main__":
    learn()