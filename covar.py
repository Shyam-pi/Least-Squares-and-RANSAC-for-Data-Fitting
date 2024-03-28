import cv2
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
    pc1 = np.loadtxt("pc1.csv",
                 delimiter=",", dtype=np.float64) # Point cloud 1

    pc2 = np.loadtxt("pc2.csv",
                    delimiter=",", dtype=np.float64) # Point cloud 2

    # Covariance matrix formation

    arr = pc1

    means = np.mean(arr, axis = 0)

    var = np.mean((arr - means)**2, axis = 0)

    cov_xy = np.mean((arr[:,0] - means[0]) * (arr[:,1] - means[1]), axis = 0)

    cov_yz = np.mean((arr[:,1] - means[1]) * (arr[:,2] - means[2]), axis = 0)

    cov_xz = np.mean((arr[:,0] - means[0]) * (arr[:,2] - means[2]), axis = 0)

    cov_matrix = np.array([[var[0], cov_xy, cov_xz],[cov_xy, var[1], cov_yz],[cov_xz, cov_yz, var[2]]])

    eig_values = np.linalg.eig(cov_matrix)[0]

    eig_vectors = np.linalg.eig(cov_matrix)[1]

    print("Covariance matrix of pc1 :")
    print(cov_matrix)

    print("\nDirection of the pc1's plane's normal :")
    print(eig_vectors[:,0])

    print("\nAll the eigen vectors that we get from np.linalg.eig function are normalized, hence the above vector's magnitude = 1")

    print("\nVariance of pc1 in the direction of the previously computed normal :")
    print(eig_values[0])
    print("\n")

if __name__ == "__main__":
    main()