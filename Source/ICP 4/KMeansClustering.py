# http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
from sklearn.cluster import KMeans
import numpy as numpy
import pandas as pandas
from matplotlib import pyplot as plot

# Reading CSV File
"""
# 64-bit floating-point number - f8
# 64-bit Integer - i8
header=1 removes the 1st row
"""
data = pandas.read_csv('sample_stocks.csv', sep=',', header=1, dtype=[('int', 'i8'), ('float', 'f8')])
csvData = data.values

# Plotting initial array data
plot.scatter(csvData[:, 0], csvData[:, 1])
plot.show()

# Creating K-means Cluster with 2 clusters
kmeans = KMeans(n_clusters=2)
kmeans.fit(csvData)

# To See Centroid values the algorithm generated for the final clusters
print(kmeans.cluster_centers_)

# To get the Labels
print(kmeans.labels_)

# Plotting the Data Points along with the labels.
"""
Here we are plotting the first column of the csvData array against the second column
We are also passing kmeans.labels_ as value for the c parameter that corresponds to labels. 
The cmap='rainbow' parameter is passed for choosing the color type for the different data points
"""
plot.scatter(csvData[:, 0], csvData[:, 1], c=kmeans.labels_, cmap='rainbow')
plot.show()

"""Plotting the points along with the centroid coordinates of each cluster,
to see how the centroid positions effects clustering.
color='black' for the centroids"""
plot.scatter(csvData[:, 0], csvData[:, 1], c=kmeans.labels_, cmap='rainbow')
plot.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='black')
plot.show()

# With Increase in number of Clusters, we will get the datapoints clustering
# together based on the number.

"""
Elbow Method - Technique to determine the K
Location of a bend (knee) in the plot is generally considered as an indicator of the appropriate number of clusters.

SSE --> Sum Of Squared Errors

Plot a line graph of the SSE for each value of k. 
If the line graph looks like an arm - a red circle in below line graph (like angle), 
the "elbow" on the arm is the value of optimal k (number of cluster). 
Here, we want to minimize SSE. SSE tends to decrease toward 0 as we increase k 
(and SSE is 0 when k is equal to the number of data points in the dataset, 
because then each data point is its own cluster, and there is no error between it and the center of its cluster).

So the goal is to choose a small value of k that still has a low SSE, and the elbow usually represents 
where we start to have diminishing returns by increasing k.
"""
distortions = {}
# Selecting k in range of 1 to 10
for k in range(1, 10):
    kmeans = KMeans(n_clusters=k).fit(csvData)
    # Inertia: Sum of distances of samples to their closest cluster center
    distortions[k] = kmeans.inertia_

plot.plot(list(distortions.keys()), list(distortions.values()))
plot.show()
