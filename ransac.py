import cv2
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from utils import planeRANSAC

def main():

    pc1 = np.loadtxt("pc1.csv",
                 delimiter=",", dtype=np.float64) # Point cloud 1

    pc2 = np.loadtxt("pc2.csv",
                    delimiter=",", dtype=np.float64) # Point cloud 2

    planeRANSAC(arr = pc1, method='SLS', heading = "Plane fitting using Ransac + Standard LS for PC1")

    planeRANSAC(arr = pc2, method='SLS', heading = "Plane fitting using Ransac + Standard LS for PC2")

    planeRANSAC(arr = pc1, method='TLS', heading = "Plane fitting using Ransac + Total LS for PC1")

    planeRANSAC(arr = pc2, method='TLS', heading = "Plane fitting using Ransac + Total LS for PC2")

if __name__ == "__main__":
    main()