import cv2
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def showImage(frame):
    """
    Function to display an image using matplotlib.
    
    Arguments:
    frame -- The array to be displayed
    """
    # Convert BGR image read by cv2 to RGB
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    plt.imshow(img)

def svd(A):
    """
    Computes the singular value decomposition of a matrix A.
    
    Arguments:
    A -- The matrix to be decomposed
    
    Returns:
    U -- The left singular vectors
    S -- The singular values
    V -- The right singular vectors
    """
    m, n = A.shape
    assert m >= n, "The matrix must have more rows than columns"
    
    # compute the eigenvectors and eigenvalues of A^T A
    ATA = A.T @ A
    eigenvalues, eigenvectors = np.linalg.eigh(ATA)
    
    # sort the eigenvalues in decreasing order
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    
    # compute the singular values and the right singular vectors
    S = np.sqrt(np.abs(eigenvalues))
    V = eigenvectors
    
    # compute the left singular vectors
    U = np.zeros((m, n))
    for i in range(n):
        if S[i] != 0:
            U[:, i] = A @ V[:, i] / S[i]
    
    return U, S, V.T


# Standard Least squares solution for plane

def standardLS_Plane(arr):

    """
    Computes the Standard Least Squares solution for a plane fitting problem.
    
    Arguments:
    arr -- Array of point cloud. Each column represents x, y and z coordinates of each point
    
    Returns:
    coeff -- Coeffiecients [A,B,C] of the plane equation Ax + By + Cz = 1, computed using Standard Least Squares algorithm
    """

    N = arr.shape[0]

    A = arr

    B = np.ones((N,1))

    coeff = np.linalg.inv(A.T @ A) @ A.T @ B

    return coeff

# Total Least squares solution for plane

def totalLS_Plane(arr):    
    """
    Computes the Total Least Squares solution for a plane fitting problem.
    
    Arguments:
    arr -- Array of point cloud. Each column represents x, y and z coordinates of each point
    
    Returns:
    means -- Array of x, y and z means of the entire point cloud
    coeff -- Coeffiecients [A,B,C] of the plane equation A(x - x') + B(y - y') + C(z - z') = 0, computed using Total Least Squares algorithm, 
    where x', y' and z' are the x, y and z means respectively.

    """
    means = np.mean(arr, axis = 0)
    A = arr - means
    
    U,S,V = svd(A)

    coeff = V.T[:,-1]
    return means, coeff

# Plotting the point cloud data along with the fitted plane

def plotPlane(arr:np.array, coeff:np.array, method:str, title = 'Point Cloud vs Estimated Plane', means = None):
    """
    Function to plot the point cloud along with the estimated plane
    
    Arguments:
    arr -- Array of point cloud. Each column represents x, y and z coordinates of each point
    coeff -- Array of coeffiecients estimated using one of the estimation algorithms
    method -- Should either be 'SLS' or 'TLS' according to whether the coefficients were obtained using Standard Least Squares or Total Least Squares 
    respectively. Any other arguements throw an error.
    means -- Array of x, y and z means. This arguement is compulsory if 'TLS' is used as the arguement for 'method'
    title -- String to change the title of the plot

    """
    # Create a figure and a 3D axes object
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create the scatter plot
    ax.scatter(arr[:,0], arr[:,1], arr[:,2], c='r', marker='o', s=0.5)

    # Set the labels and title
    ax.set_xlabel('X coordinates')
    ax.set_ylabel('Y coordinates')
    ax.set_zlabel('Z coordinates')
    ax.set_title(title)

    x = np.linspace(-10, 10, 50)
    y = np.linspace(-10, 10, 50)
    X, Y = np.meshgrid(x, y)

    # Compute the corresponding z coordinates for the plane
    if method == 'SLS':
        Z = (1 - coeff[0]*X - coeff[1]*Y)/coeff[2]
    
    elif method == 'TLS':
        Z = ((-coeff[0]*(X-means[0]) - coeff[1]*(Y-means[1]))/(coeff[2])) + means[2]
    
    else:
        raise Exception("Please provide the right method - 'SLS' for standard least squares or 'TLS' for total least squares (CASE SENSITIVE)")

    # Plot the surface of the plane
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.5)

    # Show the plot
    plt.show()

def evalPlaneSLS(coeff:np.array,pts:np.array,thresh:float):
    """
    Function to evaluate the number of pts agreeing with the hypothesized plane and given distance threshold.
    
    Arguments:
    coeff -- Array of coefficients [A,B,C] of plane equation Ax + By + Cz = 1, computed using Standard Least Squares algorithm
    pts -- Array of point cloud. Each column represents x, y and z coordinates of each point
    thresh -- Threshold on the distance of each point to be considered agreeing with the hypothesis or not
    
    Returns:
    num_success -- Number of points from the point cloud agreeing with the hypothesis

    """
    x = pts[:,0]
    y = pts[:,1]
    z = pts[:,2]
    dist = np.abs(coeff[0]*x + coeff[1]*y + coeff[2]*z - 1)/np.sqrt(coeff[0]**2 + coeff[1]**2 + coeff[2]**2)
    num_success = np.where(dist <= thresh)[0].shape[0]
    return num_success

def evalPlaneTLS(coeff:np.array,pts:np.array,means:np.array,thresh:float):
    """
    Function to evaluate the number of pts agreeing with the hypothesized plane and given distance threshold.
    
    Arguments:
    coeff -- Array of coefficients [A,B,C] of plane equation A(x-x') + B(y-y') + C(z-z') = 0, computed using Total Least Squares algorithm,
    where x', y' and z' are the x, y and z means respectively.
    pts -- Array of point cloud. Each column represents x, y and z coordinates of each point
    means -- Array of x, y and z means of the point cloud
    thresh -- Threshold on the distance of each point to be considered agreeing with the hypothesis or not
    
    Returns:
    num_success -- Number of points from the point cloud agreeing with the hypothesis

    """

    x = pts[:,0]
    y = pts[:,1]
    z = pts[:,2]
    dist = np.abs(coeff[0]*(x - means[0]) + coeff[1]*(y - means[1]) + coeff[2]*(z - means[2]) )/np.sqrt(coeff[0]**2 + coeff[1]**2 + coeff[2]**2)
    num_success = np.where(dist <= thresh)[0].shape[0]
    return num_success

def planeRANSAC(arr:np.array, method:str, heading:str, thresh = 0.1, iter = 1000):
    """
    Function to fit and plot a plane over the given point cloud using RANSAC and a Least Squares Algorithm.
    
    Arguments:
    arr -- Array of point cloud
    method -- Least squares algorithm to be used : "SLS" for Standard Least Squares and "TLS" for Total Least Squares
    thresh -- Threshold on the distance of a point from a hypothesized plane to be considered agreeing with the hypothesis
    iter -- Number of hypothesis to be sampled

    """
    N = arr.shape[0]
    hypotheses = []
    success = []

    if method == 'SLS':
        for i in range(iter):
            rand = np.random.choice(np.array(range(N)), 3, replace=False)
            pts = arr[rand,:]
            coeff = standardLS_Plane(pts)
            num_success = evalPlaneSLS(coeff, arr, thresh=thresh)
            hypotheses.append(coeff)
            success.append(num_success)
    
    elif method == 'TLS':
        for i in range(iter):
            rand = np.random.choice(np.array(range(N)), 3, replace=False)
            pts = arr[rand,:]
            means,coeff = totalLS_Plane(pts)
            num_success = evalPlaneTLS(coeff, arr, means = means, thresh = thresh)
            hypotheses.append([means,coeff])
            success.append(num_success)
    
    else:
        raise Exception("Please provide the right method - 'SLS' for standard least squares or 'TLS' for total least squares (CASE SENSITIVE)")

    success = np.array(success)
    best = np.argmax(success)

    best_plane = hypotheses[best]

    if method == 'SLS':
        plotPlane(arr, coeff=best_plane, method=method, title=heading)
    
    else:
        plotPlane(arr, coeff=best_plane[1], method = method, means = best_plane[0], title=heading)