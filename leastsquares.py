import cv2
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from utils import standardLS_Plane, totalLS_Plane, plotPlane

def main():

    pc1 = np.loadtxt("pc1.csv",
                 delimiter=",", dtype=np.float64) # Point cloud 1

    pc2 = np.loadtxt("pc2.csv",
                    delimiter=",", dtype=np.float64) # Point cloud 2

    coeff_pc1 = standardLS_Plane(pc1)
    plotPlane(pc1,coeff_pc1, method="SLS", title="Standard LS plane fitting for PC1")

    coeff_pc2 = standardLS_Plane(pc2)
    plotPlane(pc2,coeff_pc2, method='SLS', title="Standard LS plane fitting for PC2")

    means_1, coeff_pc1 = totalLS_Plane(pc1)
    plotPlane(pc1,coeff_pc1, method="TLS", means=means_1, title="Total LS plane fitting for PC1")

    means_2, coeff_pc2 = totalLS_Plane(pc2)
    plotPlane(pc2,coeff_pc2, method="TLS", means=means_2, title="Total LS plane fitting for PC2")


if __name__ == "__main__":
    main()