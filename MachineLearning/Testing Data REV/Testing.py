import numpy as np
import matplotlib.pyplot as plt

def plot_data(x_vals, y_vals, t, ms, x_label="Magnitude", y_label="Total Damage (Millions of Dollars)"):
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

def test():
    infile = input("Name of formatted data file: ")
    thetas = input("Theta values: ")
    theta = np.matrix(thetas)
    degree = len(thetas.split(" "))
    xvals, yvals = np.loadtxt(infile, delimiter=",", unpack=True)
    x_vals = [np.ones(len(xvals))]
    for d in range(1, degree):
        x_vals = np.append(x_vals, [xvals ** d], axis=0)
    x_val_mat = np.matrix(x_vals)
    y_val_mat = np.matrix(yvals)
    plot_data(xvals, yvals, "rs", 6.0)
    cost = compute_cost(x_val_mat, y_val_mat, theta)
    print("Cost: " + str(cost))
    template = np.arange(min(xvals) - 10, max(xvals) + 10, 0.2)
    theta = np.asarray(theta)[0]
    function = theta[0]
    for l in range(1, len(theta)):
        function += theta[l]*(template**l)
    plot_data(template, function, "b-", 6.0)
    print("Plotting data...")
    plt.show()

if __name__ == "__main__":
    test()
