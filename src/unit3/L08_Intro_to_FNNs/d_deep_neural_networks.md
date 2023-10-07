# Introduction to Deep Neural Networks

A deep (feedforward) neural network refers to a neural network that contains not only the input and output layers, but also hidden layers in between.

One of the main advantages of deep neural networks is that in many cases, they can learn to extract very complex and sophisticated features from just the raw features presented to them as their input. For instance, in the context of image recognition, neural networks can extract the features that differentiate a cat from a dog based only on the raw pixel data presented to them from images.

The initial few layers of neural networks typically capture the simpler and smaller features whereas the later layers use information from these low-level features to identify more complex and sophisticated features.

**Deep neural networks**

Rather than just an input and output, we now have hidden layers between them.

The width is the number of units in each layer.

The depth is the number of layers of transformation until we get to the answer.

**Applications**

In recent years, DNNs have become adopted in numerous academic disciplines, including:

- computer vision (e.g., image, scene analysis)
- natural language processing (e.g., machine translation)
- speech recognition
- computational biology

They have played a key role in commercial successes such as:

- self-driving vehicles
- speech interfaces
- conversational agents
- super-human game playing (Alpha Zero, Alpha Go)

There are many more on the way, including:

- personalised / automated medicine
- chemistry, robotics, materials science

**Why now?**

1. Lots of data - many problems can only be solved at scale.
2. Computational resources (especially GPUs) - platforms / systems that support running deep ML algorithms at scale.
3. Large models are easier to train - they can be successfully estimated with simple gradient-based learning algorithms. (Small models were relatively rigid from an optimisation standpoint.)
4. Flexible neural "lego" pieces - common representations, diversity of architectural choices.
