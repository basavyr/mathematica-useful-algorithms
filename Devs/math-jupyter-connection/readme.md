# Mathematica <-> Jupyter Notebook Connection

Implementation for a consistent workflow between Mathematica and a Jupyter Notebook.

> In the following example, a scatter plot done within Mathematica will be saved as a `.csv`. file.
> The generated output file will be used within a Python script for some manipulation, then, by using Jupyter Notebook, more data will be analyzed and plotted.

## Project structure

The structure of the current implementation works as follows:

📁

```shell
total 8
robertpoenaru  staff   192 Jan  4 03:47 .
robertpoenaru  staff   256 Jan  4 03:47 ..
robertpoenaru  staff    64 Jan  4 03:47 data
robertpoenaru  staff    64 Jan  4 03:08 math
robertpoenaru  staff  1159 Jan  4 03:47 readme.md
robertpoenaru  staff    64 Jan  4 03:08 src
```

📁

```shell
.
├── data
├── math
├── readme.md
└── src

3 directories, 1 file
```

The `/math` folder contains the Mathematica code, the `/src` folder contains the Python code, and the `/readme.md` file contains the documentation.

## Data output

The data generated from Mathematica will be saved in the appropriate files, within `/data` folder. Moreover, Python will use that directory as a data source (*input*).

## Repository

The repository is hosted on my [GitHub](https://github.com/basavyr/mathematica-useful-algorithms) profile.
