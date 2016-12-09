import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from tqdm import tqdm

def compute_cost(x_val_mat, y_val_mat, z_val_mat, theta, beta):
    m = z_val_mat.size
    H = (theta * x_val_mat) + (beta * y_val_mat)
    S = np.sum(np.asarray(H - z_val_mat)**2, axis=1)[0]
    return S/(2*m)  # J (cost) value

def gradient_descent(x_val_mat, y_val_mat, z_val_mat, theta, beta, iterations, alpha_t, alpha_b):
    print("Performing gradient descent...")
    m = z_val_mat.size
    for i in tqdm(range(0, iterations), desc="Percentage Completed"):
        # ------- gradient descent for theta: ----------
        HY = ((theta * x_val_mat) + (beta * y_val_mat)) - z_val_mat
        SA = HY * x_val_mat.transpose()
        SA *= alpha_t / m
        theta = theta - SA
        # ------- gradient descent for beta: ----------
        HY = ((theta * x_val_mat) + (beta * y_val_mat)) - z_val_mat
        SA = HY * y_val_mat.transpose()
        SA *= alpha_b / m
        beta = beta - SA
        # ------- check for overshoot: ----------
        if np.any(np.isnan(theta)):
            raise ValueError("Smaller theta learning rate needed!")
        if np.any(np.isnan(beta)):
            raise ValueError("Smaller beta learning rate needed!")
    return theta, beta

def learn(iterations=150000, theta_learning_rate=0.01, beta_learning_rate=0.01):
    succeeded = False
    infile = input("Name of formatted data file: ")
    xvals, yvals, zvals = np.loadtxt(infile, delimiter=",", unpack=True)
    x_degree = int(input("Degree of x polynomial: "))
    y_degree = int(input("Degree of y polynomial: "))
    theta = "0 " * x_degree + "0"
    theta = np.matrix(theta)
    beta = "0 " * y_degree + "0"
    beta = np.matrix(beta)
    x_vals = [np.ones(len(xvals))]
    y_vals = [np.ones(len(yvals))]
    for d in range(1, x_degree+1):
        x_vals = np.append(x_vals, [xvals**d], axis=0)
    for d in range(1, y_degree+1):
        y_vals = np.append(y_vals, [yvals**d], axis=0)
    x_val_mat = np.matrix(x_vals)
    y_val_mat = np.matrix(y_vals)
    z_val_mat = np.matrix(zvals)
    cost = compute_cost(x_val_mat, y_val_mat, z_val_mat, theta, beta)
    print("Initial cost: " + str(cost))
    theta_new = theta
    beta_new = beta
    while not succeeded:
        try:
            print("Current theta learning rate: " + str(theta_learning_rate))
            print("Current beta learning rate: " + str(beta_learning_rate))
            result = gradient_descent(x_val_mat, y_val_mat, z_val_mat, theta, beta,
                                      iterations, theta_learning_rate, beta_learning_rate)
            theta_new = np.asarray(result[0])[0]
            beta_new = np.asarray(result[1])[0]
            print("\nTheta values found: " + str(theta_new))
            print("Beta values found: " + str(beta_new))
            succeeded = True
        except ValueError as e:
            if "theta" in str(e):
                print("Theta learning rate too large, trying a smaller one...")
                theta_learning_rate /= 10
            elif "beta" in str(e):
                print("Beta learning rate too large, trying a smaller one...")
                beta_learning_rate /= 10
            else:
                print("UNIDENTIFIED ERROR\nEXITING...")
                return
    cost_new = compute_cost(x_val_mat, y_val_mat, z_val_mat, theta_new, beta_new)
    print("\nFinal cost: " + str(cost_new))

    # TODO change these parameters as needed - this is IMPORTANT!!
    x = np.arange(0, max(xvals) + 10, 100)
    y = np.arange(0, max(yvals) + 1, 0.2)

    x_template, y_template = np.meshgrid(x, y)
    function = theta_new[0]
    for l in range(1, len(theta_new)):
        function += theta_new[l]*(x_template**l)
    for l in range(0, len(beta_new)):
        function += beta_new[l]*(y_template**l)
    print("\nPlotting data...")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xvals, yvals, zvals, c='g', marker='o')
    surf = ax.plot_surface(x_template, y_template, function,
                           rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=True)
    surf.set_alpha(0.75)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.autoscale()
    plt.show()
    return theta_new, beta_new

if __name__ == "__main__":
    learn()
