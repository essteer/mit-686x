# Learning to Control

In supervised learning, we assume that when we're teaching an algorithm to do something, we provide supervision at every single step.

However, many problems are not suited to applying supervision at each step.

We may need to use trial and error, then trace back to determine which attributes contributed to success.

A mouse in a maze is not rewarded at each step, but at the end once it finally identifies the way out.

Tasks in reinforcement learning do not necessarily correspond only to navigation tasks or games; many machine learning situations apply.

For instance, learning the preferences of clients in a business setting: we do not know whether we are making the right choices throughout the process, only at the end once the client signs on (or does not sign on).

The question for reinforcement learning is therefore, to understand how the end reward is obtained by propagating back through the steps that led to it.

**The goal of reinforcement learning is to learn a good policy, with zero or little supervision.**
