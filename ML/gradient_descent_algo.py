import numpy as np
import numpy as np
import random
import sklearn
from sklearn.datasets.samples_generator import make_regression
import pylab
from scipy import stats

def compute_j_theta0_1(x, y, theta0, theta1):
    m = len(x)
    J_theta_0_1 = 0
    for xi, xj in zip(x, y):
        J_theta_0_1 += ((theta0 + theta1*xi-xj)**2)
    J_theta_0_1 = J_theta_0_1 /(2 * m)
    return J_theta_0_1

def gradient_descent(x, y, alpha):
    theta0 = 40
    theta1 = -2

    m = len(x)
    J_theta_0_1 = compute_j_theta0_1(x, y, theta0, theta1)
    max_iter = 1000
    iterations = 1
    while True:
        temp0 = theta0 - alpha * np.sum([theta0+theta1*xi-yi for xi, yi in zip(x, y)])
        temp1 = theta1 - ((alpha/m) * np.sum([(theta0+theta1*xi-yi)*theta1 for xi, yi in zip(x,y)]))
        # simultaenous update
        theta0 = temp0
        theta1 = temp1
        error = compute_j_theta0_1(x,y, temp0, theta1)
        print J_theta_0_1
        print error
        print abs(J_theta_0_1-error)
        if abs(J_theta_0_1-error) < 0.000000000001:
            print "Converged"
            print iterations
            print "theta0 = %s , theta1 = %s " %(str(theta0), str(theta1))
            break
        J_theta_0_1 = error
        if iterations > max_iter:
            break
        iterations = iterations + 1

x, y = make_regression(n_samples=100, n_features=1, n_informative=1, 
                    random_state=0, noise=35) 
print 'x.shape = %s y.shape = %s' %(x.shape, y.shape)

alpha = 0.01 # learning rate
ep = 0.01 # convergence criteria

# call gredient decent, and get intercept(=theta0) and slope(=theta1)
gradient_descent(list(x.reshape(100)),list(y.reshape(100)),alpha)


slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x[:,0], y)
print ('intercept = %s slope = %s') %(intercept, slope) 

