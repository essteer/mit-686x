# Introduction to Supervised Learning

The prediction problem examples outlined:

- Will I like this film?
- Is this chemical soluble in water?
- What is an image depicting?
- What is a sentence in a foreign language?

share a common property that it is difficult to formulate direct rules to determine the outcome for a given input.

It is difficult to specifiy the solution to these questions.

**Use of examples**

It is easier to express tasks by providing examples of the correct answer, rather than an instruction on how to reach it.

E.g., images of cats for an image classification problem.

The task then becomes one of automating the process of finding a solution based on examples.

**Mapping parameters**

To do this, we:

- hypothesise a set of potential mappings, a large set that takes an image, and specify a category
- the mapping is specified by parameters

$h([$ image of mushroom $]; θ)$

- a different value for the parameters will specify a different mapping
- we want to find a parameter which, out of the set of possible parameters, agrees with our set of examples for classification the best (the closest fit)

For machine translation, we may have English sentences ("Is it real?") mapped to Spanish sentences ("Es real?"), with a large set of examples to demonstrate what is being sought.

This would then work by taking a sentence as an input, along with adjustable parameters that specify different possible mappings, with each parameter value providing a possible answer.

$h($ 'Is it real?' $; θ) =$ 'Es real?'

(That "possible" answer may or may not match the correct answer.)

We search for those parameters in an automated way in order to find the best mapping for this task.

Google Translate operates in this mode for some language pairs already.
