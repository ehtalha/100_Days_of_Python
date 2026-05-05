'''
Problem: Given a 1D array of coordinates (representing points on a line), 
calculate the distance of every point from a specific origin point without using a loop.
'''
import numpy as np

# Points on a 1D coordinate system
points = np.array([10, 22, 35, 48, 52])
origin = 25

# NumPy broadcasts the scalar 'origin' to match the shape of 'points'
distances = np.abs(points - origin)

print(f"Points: {points}")
print(f"Distance from {origin}: {distances}")

#output
'''
Points: [10 22 35 48 52]
Distance from 25: [15  3 10 23 27]
'''
