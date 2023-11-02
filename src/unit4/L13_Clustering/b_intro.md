# Introduction to Clustering

Clustering is a form of unsupervised learning.

We still make use of training sets, but unlike in supervised learning, we will not have a label.

Classification for supervised learning:

S<sub>n</sub> = { (x<sup>(i)</sup>, y<sup>(i)</sup>) | i = 1, ⋯, n }

CLustering (unsupervised learning):

S<sub>n</sub> = { x<sup>(i)</sup> | i = 1, ⋯, n }

In this situation, we may have clouds of data points, but no knowledge of their labels. However, the groups or clusters themselves may be indicative of underlying classifications.

One of the most common uses of clustering is to visualise information, and thus improve access to information.

**Google News**

Google News _classifies_ news items, such as US news, world news, entertainment, politics, and so on.

It then _clusters_ news items together, such as through a lead news item, followed by further articles relevant to the same topic.

In order to group items into clusters, we need a means to compare similarity.
