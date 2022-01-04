# Mathematica <-> Jupyter Notebook Connection

Implementation for a consistent workflow between Mathematica and a Jupyter Notebook.

> In the following example, a scatter plot done within Mathematica will be saved as a `.csv`. file.
> The generated output file will be used within a Python script for some manipulation, then, by using Jupyter Notebook, more data wil be analyzed and plotted.


## Project structure

The structure of the current implementation works as follows:

``` shell
total 8
robertpoenaru  staff  160 Jan  4 03:10 .
robertpoenaru  staff  256 Jan  4 03:10 ..
robertpoenaru  staff   64 Jan  4 03:08 math
robertpoenaru  staff  414 Jan  4 03:10 readme.md
robertpoenaru  staff   64 Jan  4 03:08 src
```

``` shell
├── math
├── readme.md
└── src

2 directories, 1 file
```

The `/math` folder contains the Mathematica code, the `/src` folder contains the Python code, and the `/readme.md` file contains the documentation.
