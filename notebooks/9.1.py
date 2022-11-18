#%matplotlib notebook
# 2D data generated and meanshift used to find labels, cluster centers and amount of clusters
from itertools import cycle
from sklearn.datasets import make_blobs

centers = [[2, 1], [0, 0], [1, -1]] # centers are now 2-d
data_2d, _ = make_blobs(n_samples=2500, centers=centers, cluster_std=0.1)

labels, cluster_centers, n_clusters = mean_shift(data_2d)

# Plot the clusters in different colors
fig = plt.figure()
ax = fig.add_subplot(111)

colors = cycle('bgrcmy')
print(list(zip(range(3),colors)))
for k, col in zip(range(n_clusters), colors):
    my_members = (labels == k)
    cluster_center = cluster_centers[k]
    
    x, y = data_2d[my_members,0], data_2d[my_members,1]
    ax.scatter(x, y, c=col, linewidth=0.2)
    ax.scatter(cluster_center[0], cluster_center[1], c='k', s=50, linewidth=0.2)
    
plt.title('Estimated number of clusters: {}'.format(n_clusters))