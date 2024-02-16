# Gating and LSTM

Learning RNN models is similar to learning feed-forward NNs.

As we turn the sentence into a vector we make a prediction, which results in an error signal.

We can then backpropagate the error signal through the layer-wise transformation, just as with the FNNs.

The fact that the parameters are shared with RNNs, just means that we add the contribution of each of the suggested modifications for each of the parameters at each of the position where the transformation is applied.

A concern with backpropagation is the same as applies to deep NNs, that the gradients may vanish or explode.

Sequences can be long, and so the issue of this occurring is real for RNNs.

The functions inside the "box" for different architectures are therefore tailored for each task.

**Enhancing the model**

$s_t = tanh(W^{s,s}s_{t-1} + W^{s,x}x_t)$

The model so far is a very simple RNN.

A problem with this implementation is that as transformation proceeds, we forget what we had before, we overwrite it.

It can be useful to retain control over what is overwritten, and what is incorporated as new information.

This control is typically done by a gating network.

A gating network has the same input and form of input as the state transformation, but converts it into a continuous value between $0$ and $1$:

$g_t = sigmoid(W^{g,s}s_{t-1} + W^{g,x}x_t)$

$s_t = (1 - g_t) ⊙ s_{t-1} + g_t ⊙ tanh(W^{s,s}s_{t-1} + W^{s,x}x_t)$

where:

- $g_t ∈ [0, 1]$
- $⊙$ denotes element-wise multiplication

As before, the output is a vector of the same dimension as the state.

We then incorporate this gating prediction of what we should write and retain, into the state update itself.

We take a combination of what we had previously, and the new prediction, and balance between the two using the gating network.

For example:

- $(1 - g_t) = [0, 1, 0, ...]^T$
- $g_t = [1, 0, 1, ...]^T$

When $1 - g_t = 0$, it means we retain no information from the previous state.

Nor do we store that information; we overwrite that coordinate with the update we say before.

When that value $= 1$, we retain what we had previously, and completely ignore the suggested value.

We don't know what to retain and what to ignore, but we can learn how to control it, hence it is useful to build this control into the NN architecture.

This is simple gated RNN architecture.

**LSTM**

An example of one possible Long Short Term Memory network:

- Forget gate = $f_t = sigmoid(W^{f,h}h_{t-1} + W^{f,x}x_t)$
- Input gate = $i_t = sigmoid(W^{i,h}h_{t-1} + W^{i,x}x_t)$
- Output gate = $o_t = sigmoid(W^{o,h}h_{t-1} + W^{o,x}x_t)$
- Memory cell = $c_t = f_t ⊙ c_{t-1} + i_t ⊙ tanh(W^{c,h}h_{t-1} + W^{c,x}x_t)$
- Visible state = $h_t = o_t ⊙ tanh(c_t)$

In this model, the previous state is now given by the combination of the two variables $c_{t-1}$ and $h_{t-1}$.

Our new summary is then given by $c_t$ and $h_t$.

When we are updating the memory cell, we take the suggested new signal as in the basic RNN, $tanh(W^{c,h}h_{t-1} + W^{c,x}x_t)$, and pair it with an input gate $i_t$, that controls which of the suggested elements should enter the memory cell.

We also have a forget gate, $f_t$, that controls which of the coordinates from the previous memory cell should be erased.

When the forget gate has value $0$ for one coordinate, we would completely erase the infomration that that coordinate had in the previous memory cell.

The memory cell update is therefore helpful to maintain information over long sequences.

However, the memory cell is kept hidden, and we reveal only the visible portion of the state.

$h_t = o_t ⊙ tanh(c_t)$

So, we take the tanh transformation of the memory cell signal, $tanh(c_t)$, and since the memory cell signal is additive, it can incresae in value.

We turn that signal into $-1$ and $1$, by applying tanh, then control what portion of that signal should actually be made visible.

It is the $h_t$ that then at the end of the whole signal, that is used as the vector representation for the sequence.

There are alternatives to this approach, with more sophisticated architecture, but LSTM is still frequently used.
