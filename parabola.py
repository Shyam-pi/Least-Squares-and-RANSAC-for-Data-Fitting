import cv2
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from track import getTrack

def main():
    # Standard Least squares curve fitting for a parabola

    first, track = getTrack(disp_plot=False, disp_vid=False)

    N = track.shape[0]

    A = np.array([np.block([track[n,0]**2, track[n,0], 1])
                    for n in range(N)]).reshape(N, 3)

    sol = np.linalg.inv(A.T @ A) @ A.T @ track[:,1]

    print("\nEstimated coefficients A, B and C = ")
    print(sol)

    print(f"\nEquation of the curve :\n y = {sol[0]} x^2 + {sol[1]} x + {sol[2]}\n")

    x = track[:,0]

    y = sol[0] * x**2 + sol[1] * x + sol[2]

    fig, ax = plt.subplots()
    im = ax.imshow(cv2.cvtColor(first, cv2.COLOR_BGR2RGB))
    ax.scatter(x, y, s=2, color='blue', label = 'Fitted parabola')
    ax.scatter(track[:,0], track[:,1], s=2, color='red', label = 'Tracked data')
    ax.set_xlabel('X coordinates')
    ax.set_ylabel('Y coordinates')
    ax.set_title('Estimated ball trajectory vs fit parabola')
    plt.legend(loc="upper left")
    plt.show()

    # Calculation of landing location of the ball

    landing_y = track[0,1] + 300

    landing_x = (-sol[1] + np.sqrt(sol[1]**2 - 4*sol[0]*(sol[2] - landing_y)))/(2*sol[0])

    print("Landing pixel's Y coordinate = " + str(landing_y))

    print("X coordinate of the pixel of landing = " + str(landing_x))

    print("\n")

if __name__ == "__main__":
    main()