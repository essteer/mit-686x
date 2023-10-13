# Convolutional Neural Networks

Image classification: mapping images to categories.

We have an image of, e.g., a mushroom, and 1,000 possible categories. This is a multi-way classification problem.

x = input example, the image of the mushroom
y = the mushroom category

**Why feedforward NNs are unsuited for this purpose**

1. Number of parameters needed

Our input (the image) could be of 1,000 x 1,000 resolution, 1 million pixels.

Layer 1 also has 1,000 x 1,000 units, arranged in a similar way to pixels, and which each take the image as input.

Each of the million pixels in layer 1 receives the input with a set of 1 million weights associated with each of the pixels in the image.

The mapping between the image and layer 1 has a weight matrix, W, of order 10<sup>6</sup> \* 10<sup>6</sup> - i.e., 1 trillion weights.

It would take a large number of images, for the model to be able to learn the appropriate weights, with any degree of confidence.

2. Tunnel-vision

If the model is trained on, for example, images with mushrooms in the centre of the image, it would fail when tested on images that had mushrooms around the other areas of the image.

The weights for those areas would not have encountered the mushroom image, and thus be incapable of classifying it.

There would be too many degrees of freedom.

**Patch classifier / filter**

We can instead train on e.g., 11 x 11 patches of images, with again a weight corresponding to each pixel of the patch.

We now have 121 weight parameters (11 x 11) instead of the 1 trillion in the above model! And this is sufficient to learn what the weight should be.

We have a weight corresponding to each pixel in the image, which means we also can arrange a matrix of the same size as the input image.

E.g., the 11 x 11 image is mapped to an 11 x 11 matrix grid.

We then take an inner product between the two matrices - we vectorise the matrices - and take a normal inner product.

This can also be understood as taking each corresponding pixel from the two matrices, and adding them up to get one real number.

We pass this number to e.g., ReLU, and this results in our output.

In this sense, we can think of the weights matrix itself as an image - the image that the unit prefers to see.

If the image resembles the parameter patch, there is a large response, otherwise none.

**Convolution**

We now want to apply this for the first layer.

The feature map again has the same number of units as there are pixels in the original image.

But this time, we take the 11x11 patches of the original image, as the input to our smaller classifier, and use the same weights for that image patch.

We pass that through ReLU, then pass that on to the feature map for that patch.

We then move the patch slightly ("**stride**") on the original image - it might move only one pixel, or a few at a time, so there is overlap with the first patch.

We now pass this second patch as input, and apply the same weights in the ReLU function as before.

From this we get a real number, which we pass to the feature map.

So, in each location we have a patch that we run through a classifier, and get a corresponding value in the feature map.

This is much more efficient in terms of the parameters.

The transformation involves only 121 parameters, but we get a feature map where each location, each activation of the units, tells us how much that feature is present in the corresponding location.

**Comparison with simple feedforward transformation**

1. Each unit connects only locally, it doesn't look at the whole image.

2. The weights used to transform each patch into an activation in the feature map, uses the same set of weights.

So there is **local connectivity**, and **shared weights**.

This is known as a **convolution operation**.

**Pooling**

We wish to know whether a feature was present, but not exactly where it was.

This is facilitated by pooling.

It is simpler than convolution, but applied in a similar way.

Now take, for example, a smaller 5x5 patch. In the resulting map, we store only the maximum value of those 25 pixels.

f = max{.....}

I.e. the maximum activation of what that feature was trying to detect.

We store the fact that there is activation, but not where it is amongst those 25 pixels.

**Note**: Pooling region and stride may vary:

- pooling induces translation invariance at the cost of spatial resolution;
- stride reduces the size of the resulting feature map.
