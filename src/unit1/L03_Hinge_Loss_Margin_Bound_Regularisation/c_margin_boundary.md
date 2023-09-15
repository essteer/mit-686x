# Margin Boundary

The **decision boundary** is the set of points _x_ which satisfy:

- `θ•x + θ0` = 0`.

The **margin boundary** is the set of points _x_ which satisfy:

- `θ•x + θ0 = ±1`.

So, the distance from the decision boundary to the margin boundary is:

- `1 / ∥θ∥`

**Optimisation problem**

Returning to the optimisation problem: we want to determine what the margin boundaries (**MBs**) are, and how we can control them with respect to the decision boundary (**DB**).

- Recall that the MBs are equidistant to the DB.
- The linear function, `θ•x + θ0 = 0`, is exactly on the DB.

**Positive margin boundary**

- If we move in the direction of θ, that linear function (`θ•x + θ0`) will start to have more positive values.

We can define the **positive MB** as the set of x's where:

- `θ•x + θ0 = 1`

This new boundary (`θ•x + θ0 = 1`) is parallel to the DB (`θ•x + θ0 = 0`), because there is no point x that can satisfy both equations.

**Negative margin boundary**

Conversely, on the negative side if we move against the parameter vector θ, the linear function starts to take on more negative values. The **negative MB** is defined by:

- `θ•x + θ0 = -1`

**Putting it together**

We now have two MBs, one positive and one negative, and these are equidistant from the DB.

We can then try to push these MBs apart, because the MBs are also defined by the `θ and θ0` parameters we want to optimise.

**Distance from MBs to the DB**

We still need to understand the distance from the MBs to the DB, and how we can control the distance.

Again, our DB is all x that satisfy `θ•x + θ0 = 0`.

We can divide the equation by the norm of `θ`, `∥θ∥`, and it still defines the same decision boundary:
7

- `(θ•x)/∥θ∥ + θ0/∥θ∥ = 0`

As a result, **the norm of θ, ∥θ∥, is a free parameter that we have not yet used**.

- ∴ ∥θ∥ is the degree of freedom that gives the same DB as a result.
- We can use ∥θ∥ to push the MBs apart.

**Intuition**

As we move the MBs away from the DB, the value of the linear function increases at a rate that is related to ∥θ∥, the magnitude of the parameter vector θ.

- The larger the value of θ is, the faster the magnitude ∥θ∥ reaches +1 for the positive MB (-1 for the negative MB).

As a result, in terms of distance from the DB:

- The closer the MB is to the DB, the larger the value of ∥θ∥.

**The ∥θ∥ controls the distance from which the MBs are drawn to the DB.**

Consequently, when we select θ and θ<sub>0</sub> we determine the orientation of the DB, as well as where the MBs are drawn.

**Defining the resultant optimisation problem**

We can now define more formally, what the regularisation term is that allows us to control how far the MBs are from the DB.

Take a negatively labelled point that lies exactly on the negative MB:

- `γi(θ,θ0) = y^(i)(θ•x^(i) + θ0)/∥θ∥`

We can quantify the distance that it lies from the DB:

- We know that the magnitude of the linear function itself, as we move away from the DB, increases at a rate related to the norm of θ.
- Dividing this by the magnitude/norm, we get a measure of distance from the DB.
- Since with the negative MB our linear function is negative, and we are multiplying it by a negative point (y<sup>(i)</sup>), the result is (-1 \* -1) a positive distance 1/∥θ∥

- I.e., when exactly on the negative MB, both y<sup>(i)</sup> and (θ•x<sup>(i)</sup> + θ<sub>0</sub?>) in the numerator are equal to -1, so we have -1 x -1 = +1.

`γi(θ,θ0)` gives us the signed distance, because it measures the distance of a point from the DB, but also the side of the DB on which it lies:

- if a point is on the correct side of the DB, it will be positive
- if it lies on the negative side of the DB, and the distance will be -1/∥θ∥.

**The MBs are a distance of 1/∥θ∥ from the DB.**
