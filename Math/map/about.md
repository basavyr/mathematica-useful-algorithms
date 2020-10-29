# Mathematica `map` implementation

This document is based on the following [YT tutorial](https://www.youtube.com/watch?v=QzTVY3uFqgY&t=134s) and it deals with the `map` function inside Wolfram Mathematica.
```
In[1]:= Map[f,{a,b,c,d,e}]
Out[1]= {f[a],f[b],f[c],f[d],f[e]}
```


Alternative input form:
```
In[1]:= f/@{a,b,c,d,e}
Out[1]= {f[a],f[b],f[c],f[d],f[e]}
```

Use explicit pure functions:
```
In[1]:= (1+g[#])&/@{a,b,c,d,e}
Out[1]= {1+g[a],1+g[b],1+g[c],1+g[d],1+g[e]}
In[2]:= Function[x,x^2]/@{1,2,3,4}
Out[2]= {1,4,9,16}
```