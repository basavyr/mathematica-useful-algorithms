# Executing Mathematica Scripts Within the Command-Line

This guide will show how to run Wolfram Mathematica scripts right from the command-line, without using the **Frontend**.

## Setting up the console environment (MacOS)

Technically, a Mathematica script can be executed from the command line using the [Mathematica Kernel](https://reference.wolfram.com/language/ref/Kernels.html).

After installation of the Wolfram Mathematica application, default location of that *executable* kernel should be at `/Applications/Mathematica.app/Contents/MacOS`:
```bash
/Applications/Mathematica.app/Contents/MacOS
                                        ├── [  13]  MathKernel -> WolframKernel
                                        ├── [ 50M]  Mathematica
                                        ├── [  11]  MathematicaServer -> Mathematica
                                        ├── [196K]  WolframKernel
                                        ├── [  13]  wolfram -> WolframKernel
                                        └── [7.7M]  wolframscript

                                        1 directory, 6 files
```

Say there is a script `test.m`, then one would execute it via this command:
```bash
$ /Applications/Mathematica.app/Contents/MacOS/MathKernel -script test.m
```

ℹ️ A much easier approach would be to add the `MacOS` folder to the system's path:
```bash
export PATH=$PATH:/Applications/Mathematica.app/Contents/MacOS/
```
and also save this inside the `~/.zshrc` file to have it each time the shell is started.

An alias can be created, such that the `MathKernel -script` prefix can be typed faster when executing the scripts.

```
export PATH=$PATH:/Applications/Mathematica.app/Contents/MacOS
alias math="MathKernel -script"
```

⚠️ When executing the `MathKernel` on any script file, make sure **there are no running instances of other kernels**. This means that any Frontend Mathematica applications should be closed. Check the process tree for active kernels. Otherwise the script execution will throw error about license/credentials:
```bash
basavyr@192 System-Differential-Equations % math linear_ode.m 
No valid password found.
```

Example of script that can be executed is [this one](https://github.com/basavyr/mathematica-useful-algorithms/blob/43c628aa74ec56af930d17e5c4dcf4514ce88d0c/Math/System-Differential-Equations/linear_ode.m).

```Mathematica
(* solver for a linear ordinary differential equation *)

(* This script aims at solving Eq. (1) from https://mathinsight.org/ordinary_differential_equation_linear_integrating_factor*)

diffEq = f'[t] == Power[t, 2] - f[t];

sol = DSolve[diffEq, f[t], t]

(* make the constant from the sol term as a variable *)

solC[c_] :=
    Values @ sol[[1, 1]] /. {C[1] -> c};

Print["Solutions for f[t]"]

Export["c_values.pdf", ListPlot[Table[{t, solC[1]}, {t, -1, 10}], Joined
     -> True, PlotRange -> All, PlotStyle -> Red, PlotLabel -> "c=1", FrameLabel
     -> {"t", "f[t]"}, Frame -> True, ImageSize -> 400, PlotMarkers -> {Automatic,
     10}, Axes -> False, PlotRange -> All]]

currentWorkingDirectory = Directory[];

Print["Current working directory is: " <> currentWorkingDirectory]

initialDirectory = $InitialDirectory;

Print["The initial directory: ", initialDirectory]

(* change the current working directory one above*)

newWorkingDirectory = SetDirectory[ParentDirectory[currentWorkingDirectory
    ]];

Print["Current working directory is now: " <> newWorkingDirectory]

Print["The initial directory: ", initialDirectory]
```