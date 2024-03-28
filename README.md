# Least-Squares-and-RANSAC-for-Data-Fitting

**Goal**: Implementation and analysis of data fitting using Least Squares and RANSAC on a ball's trajectory obtained from a video footage and plane fitting on point cloud data followed by surface normal computation

# Project Overview

This repository contains the implementation and analysis of data fitting using Least Squares and RANSAC on a ball's trajectory obtained from a video footage and plane fitting on point cloud data followed by surface normal computation. Below is an overview of each problem tackled in the project along with a brief description of the pipeline, challenges faced, results obtained, and corresponding code files.

## Problem 1: Ball Tracking

### 1.1. Detect and Plot Ball Trajectory

**Task:** Extract pixel coordinates of the center point of a red ball in a video.

**Pipeline:**
1. **Masking Operation:** Utilize RGB space to separate the red ball from the background. Threshold values are applied to the R, G, and B channels.
2. **Coordinate Extraction:** Obtain pixel coordinates of the masked ball.
3. **Trajectory Plotting:** Plot the trajectory using the extracted coordinates, with the first frame as the background.

**Challenges:** Selection of appropriate color space for masking, ensuring accurate detection across frames.

**Code**: '''python track.py'''

**Results:** Visualization of the ball's trajectory over time:

![image](https://github.com/Shyam-pi/Least-Squares-and-RANSAC-for-Data-Fitting/assets/57116285/11c1b02c-00e4-4b71-a4ce-080749e5d11b)


### 1.2. Curve Fitting with Standard Least Squares

**Task:** Fit a parabolic curve to the extracted coordinates using Standard Least Squares.

**Pipeline:**
1. **Parabola Fitting:** Use the equation \(y = Ax^2 + Bx + C\) to fit a parabola to the data.
2. **Coefficient Computation:** Calculate coefficients \(A\), \(B\), and \(C\) using the least squares method.
3. **Equation Printing:** Print the equation of the fitted parabola.

**Challenges:** Choosing the appropriate form of the parabola for fitting, ensuring accurate parameter estimation.

**Code**: python parabola.py

**Results:** Equation of the fitted parabola and visualization of the data with the best fit curve:

\(y = 0.0005917138678251402* x^2 + -0.6008595599840281*x + 457.5293460387038\)

![image](https://github.com/Shyam-pi/Least-Squares-and-RANSAC-for-Data-Fitting/assets/57116285/b7fe2e78-7633-46f2-b12f-f3339a2c19d6)


### 1.3. Compute Ball's Landing Spot

**Task:** Determine the x-coordinate of the ball's landing spot on the video frame.

**Pipeline:**
1. **Initial Coordinate:** Use the trajectory data to find the initial coordinates of the ball.
2. **Landing Spot Computation:** Estimate the final y-coordinate of the ball and substitute it into the parabolic equation to compute the x-coordinate of the landing spot.

**Challenges:** Accounting for camera motion during trajectory calculation, determining the correct solution from the parabolic equation.

**Code**: python parabola.py

**Results:** Printed x-coordinate of the ball's landing spot:

![image](https://github.com/Shyam-pi/Least-Squares-and-RANSAC-for-Data-Fitting/assets/57116285/319e85db-fc82-4aaa-aa12-35e7c58e89d8)


## Problem 2: Surface Fitting

### 2.1. Compute Covariance Matrix and Surface Normal

**Task:** Analyze a point cloud to compute its covariance matrix and surface normal.

**Pipeline:**
1. **Covariance Matrix:** Compute the covariance matrix of the point cloud.
2. **Surface Normal:** Calculate the surface normal using eigenvectors of the covariance matrix.

**Challenges:** Interpreting the significance of the surface normal magnitude, ensuring correct computation of the covariance matrix.

**Code**: python covar.py

**Results:** Covariance matrix and direction/magnitude of the surface normal:

![image](https://github.com/Shyam-pi/Least-Squares-and-RANSAC-for-Data-Fitting/assets/57116285/2f560d97-2bb7-4834-8e31-b948691e04e1)
![image](https://github.com/Shyam-pi/Least-Squares-and-RANSAC-for-Data-Fitting/assets/57116285/43f6bfb9-14f2-4182-ae02-2ed316638f37)

### 2.2. Surface Fitting with Various Methods

**Task:** Fit a surface to the point cloud using Standard Least Squares, Total Least Squares, and RANSAC methods.

**Pipeline:**
1. **Plane Fitting:** Fit a plane to the point cloud using SLS and TLS algorithms.
2. **Outlier Rejection:** Implement RANSAC to robustly fit a plane by iteratively selecting random subsets of points and rejecting outliers.
3. **Comparison:** Evaluate the performance of each fitting method and interpret the results.

**Challenges:** Choosing the appropriate outlier rejection method, balancing computational efficiency with accuracy.

**Results:** Comparison of fitting methods and their suitability for different scenarios (LS = Least Squares)

![image](https://github.com/Shyam-pi/Least-Squares-and-RANSAC-for-Data-Fitting/assets/57116285/48816a88-9295-4d16-ae40-38dea2fcd262)

![image](https://github.com/Shyam-pi/Least-Squares-and-RANSAC-for-Data-Fitting/assets/57116285/d94591ed-e7ab-46cc-9940-48653640c68c)

![image](https://github.com/Shyam-pi/Least-Squares-and-RANSAC-for-Data-Fitting/assets/57116285/14831654-5693-4cd0-8d35-9189a34f4622)

![image](https://github.com/Shyam-pi/Least-Squares-and-RANSAC-for-Data-Fitting/assets/57116285/61ac8b99-9859-4c72-a960-49fdaa9425c0)

## Conclusion

This project showcases the application of various techniques in video and point cloud analysis, providing insights into curve fitting, surface fitting, and outlier rejection methods. Through detailed pipelines and analysis, it offers a deeper understanding of the challenges and considerations involved in data modeling and interpretation. Each task is accompanied by thorough documentation and code implementation for reproducibility and further experimentation.
