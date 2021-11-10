# Homework2 README
## Problem 1
In order to completly answer problem 1-d, I wrote a python program in notebook form, <I>code-prob1d.ipynb</I>.<br>
* The main loop is to loop over every (<I>n</I>, <I>k</I>) combination and check whether there has different centralities for different vertices.<br>
* The last block shows the visualization of the special case, (<I>n</I>, <I>k</I>) = (7, 2).

## Problem 2
The dataset used in problem 2 can be accessed under the <I>Dataset</I> directory.<br><br>
In <I>code-prob2.ipynb</I> :
* The data pre-processing and visualizing parts are quite simple.
* Katz centrality:
  * Pre-process the adjacency matrix because original igraph adjacency matrix may contain some value bigger than 1.
  * Randomly generate α ∈ [0, 1/k)
  * Iterate the following formula to get Katz centrality:
    <pre><code>x(t) = αAx(t-1)+ β</code></pre>
* Compare with:
  * Eigenvector centrality
  * Closeness centrality
  * Harmonic centrality
  * Betweenness centrality
