(* This is a script that will find the solutions for a system of two differential equations*)

Needs["Developer`"]

scriptPath = DirectoryName[$InputFileName];

(* This is the path to the folder where the script is located. This is used to find the path to the folder where the data is stored. *)

Print["Current location: ", scriptPath];

(*write the two equations that will enter in the system of ODE*)

eq1 = x'[t] == w1 * x[t] + y[t] + t1;

eq2 = y'[t] == x[t] + w2 * Power[y[t], -0.5] + t2;

(*This is the solution for the system of ODE*)

solutions[w1_, w2_, t1_, t2_] = NDSolve[{eq1, eq2, x[1] == 2, y[1] ==
     2}, {x[t], y[t]}, {t, 1, 10}] /. {w1 -> w1, w2 -> w2, t1 -> t1, t2 ->
     t2};

sol = solutions[1, 2, 3, 4];

(* Print["The solutions are: ", sol]; *)

solxt = x[t] /. sol[[1]];

solyt = y[t] /. sol[[1]];

plotdatax = Table[{t, x[t] /. sol[[1]]}, {t, 1, 10, 0.1}];

(* Print["The plotdatax is: ", plotdatax] *)

plotdatay = Table[{t, y[t] /. sol[[1]]}, {t, 1, 10, 0.1}];

(* Print["The plotdatay is: ", plotdatay] *)

Export["plot.pdf", Quiet[Plot[Evaluate[{x[t], y[t]} /. sol], {t, 1, 10
    }], InterpolatingFunction::dmval]]

Export["list_plot.pdf", Quiet[ListPlot[plotdatax, Joined -> True, PlotMarkers
     -> {Automatic, 5}, PlotStyle -> {Red}, Frame -> True, Axes ->
     False], InterpolatingFunction::dmval]]

array = {1, 2, 3, 4, "five"};

PackedArrayQ[array]

(* This is a script that will find the solutions for a system of two differential equations*)
