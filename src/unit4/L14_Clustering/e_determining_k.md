# Determining the Number of Clusters

In some cases, it may be intuitive to determine the number of clusters, $K$, that should be used.

For example, teaching a class at MIT, you may be given 5 recitations, and must take the whole class and divide it into 5 based on some principle.

In many cases, however, there is some freedom in selecting the number K.

**$K = 1$**

If all points were placed in a single cluster, so one representative and the cost measured in relation to that single point, the cost will be at the maximum.

**$K ⟶ n$**

Introducing a second point will reduce the cost, and so on as $K$ is increased to $n$, the number of data points, at which point the cost becomes zero (when every point occupies its own cluster).

**Which $K$ to choose?**

However the choice of $K$ depends on the application - zero cost in the case of image quantization, would mean no compression of the image, and thus failure to meet the goal set in the first place.

For visualisation purposes, you can just experiment with different $K$ and compare the results to find your preferred output.

**$K$ selection as pre-processing**

Clustering when used as part of the machine learning system, can be a way to pre-process the data.

There is a mechanism to select the number $K$.

Recall that in supervised learning, for classification, we had a finite number of points either +ve or -ve, and wanted to determine a decision boundary.

If there were introduced many points that were unknown, then knowing the underlying structure of the points would help to cluster them appropriately.

When we are generating the features, we run our $K$-means clustering, and then represent every single point here not by its cluster, because it's not good enough representation, but let's say by its distance to the centroid of the computed clusters.

So in addition to having the point itself, you also look how far it is located from the centroids of all the clusters.

Now in addition to however you represented the point $x$, you add information which tells how geometrically it relates to all the pre-computed clusters.

In this case, if you do this type of representation you can decide the number $K$ based on your development data.

You can say if I do $2$ clusters and I do this feature representation, then my performance on development is $75$ - but if I do $20$ clusters, my performance on the development is going to be $78$.

**Note on unsupervised learning**

Despite this being a form of unsupervised learning, this does not mean that no input is provided to the system.

In fact, we decide the number of clusters, we decide the similarity measurement, and we decide the cost function.
