# Clustering Definition

Here we look at two forms of clustering, through partitioning and representatives.

**Partition clustering**

The first way of thinking about clustering, is thinking about it as partitioning.

Our clustering input is a set of feature vectors and $K$, the number of clusters (e.g., the number of colours in an image compression):

$S_n = \lbrace x^{(i)} | i = 1, ⋯, n \rbrace, K$

The clustering output is partitions, where each partition records the index of the elements that belong to that cluster:

$C_1, ⋯, C_K$

Taking a union of the partitions would get all elements of the training set.

$∪C_j = \lbrace 1, ⋯, n \rbrace$

This union does not record the elements themselves, but the indices of the elements.

When we look at $C_i$ and $C_j$, for a different $i$ and $j$:

$C_i ∩ C_j = ∅ (i ≠ j)$

So, in aggregate our clustering input and output are:

Input: $S_n = \lbrace x^{(i)} | i = 1, ⋯, n \rbrace, K$

Output: $C_1 ⋯ C_K; ∪C_j = \lbrace 1, ⋯, n \rbrace, C_i ∩ C_j = ∅ (i ≠ j)$

This is "hard" clustering, where every element belongs to just one partition.

This is one way to think of clustering, as simply a grouping of elements.

**Representative clustering**

Another important way to consider clustering, is to think of clustering in terms of their representatives.

Representatives would be vectors that include every single partition:

$z^{(1)}, ⋯, z^{(K)}$

Back to the Google News example, the cluster would be the stories selected to represent a particular news article.

In the case of image quantization, the representative would be the colour selected to represent the pixels that were collapsed into a single colour.
