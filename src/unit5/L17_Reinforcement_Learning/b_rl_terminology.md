# RL Terminology

**Markov decision process**

MDPs consist of the following components:

| Term        | Notation                 | Notes                                    |
| ----------- | ------------------------ | ---------------------------------------- |
| States      | s ∈ S                    | (observed)                               |
| Actions     | a ∈ A                    | e.g., left right up down                 |
| Transitions | T(s,a,s') = p(s' \| s,a) | e.g., 80% chance up, 10% left, 10% right |
| Reward      | R(s), or R(s,a,s')       |                                          |
| MDP         | <S,A,T,R>                |                                          |

So, with our MDP we have a set of states and actions, and our transitions which in a simple case can be thought of as a big table of the probabilities of the model.

For example, for the simple case of a robot in a 3x3 grid, with the centre square obstructed, there may be an 80% chance of going up, and a 10% chance of going both right and left.

MDPs satisfy the Markov property in that the transition probabilities and rewards depend only on the current state and action, and remain unchanged regardless of the history (i.e. past states and actions) that leads to the current state.
