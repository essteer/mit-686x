# Another Example: Image Quantization

The Google News example introduced a form of use of clustering for visualisation.

Here we examine a different form of clustering, for data compression: image quantization.

A typical image may have $1024 \times 1024$ pixels, and each pixel has $24$ bits: $8$ for each of red, green, and blue.

That image is therefore $1024 \times 1024 \times ≈ 3$ million.

We may wish to compress this image so that it takes up much less space, but still have a high quality image.

One option is to make use of just $32$ colours rather than the rich description offered by the 24-bit rgb above.

This would need just $2^5$ to encode.

We would then need just: $1024 \times 1024 \:•\: 5 + 32 \:•\: 24$. Here the 32 represents a dictionary, which remembers how to transfer the colours from the original 24-bit representation.

| Term                       | Description                                   |
| -------------------------- | --------------------------------------------- |
| $1024 \times 1024 \:•\: 5$ | represents every pixel by one of $32$ colours |
| $32 • 24$                  | remembers how to translate the colours        |

$1024 \times 1024 \:•\: 5 + 32 \:•\: 24 ≈ 640R$, a much smaller representation of the image.

**K-means**

$K$ in terms of colours in an image refers to the number of colours the image is compressed down to.

For example, $2$-means would be an image compressed down to just $2$ colours. This would result in a highly compressed image, though the quality would be poor.

There are two contrasting objectives, to compress the image while preserving quality.
