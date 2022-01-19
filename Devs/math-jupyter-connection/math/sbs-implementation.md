# Implementing the side-by-side joiner in Mathematica

The joiner combines multiple tables **side-by-side**

## Mode of operation

- create a list of parameters
  
  - the list contains an arbitrary number of pairs `{p1,p2}` (where the actual `p_k` values are represented by the variables `a` and `b` within Mathematica)

- for a pair of params `{p1,p2}` we need
  
  - a set of headers giving the numerical values of the params
  
  - a set of headers for the legend -> `x, f(x)` **these are attributed to the numerical data that is built from the parameters**

- the steps
  
  1. generate a list of params from the random pair generator
  
  2. build a set of tables `{x,f(x)}` for each param set within the **param list**
  
  3. 
