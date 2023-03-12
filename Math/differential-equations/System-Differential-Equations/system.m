(* This is a script that will find the solutions for a system of two differential equations*)

scriptPath = DirectoryName[$InputFileName];

(* This is the path to the folder where the script is located. This is used to find the path to the folder where the data is stored. *)

Print["Current location: ", scriptPath];

(*write the two equations that will enter in the system of ODE*)

eq1 = x'[t] == w1 * x[t] + y[t] + t1 + Sin[t];

eq2 = y'[t] == x[t] + w2 * Power[y[t], 2] + t2;

(*This is the solution for the system of ODE*)

solutions[w1_, w2_, t1_, t2_] = NDSolve[{eq1, eq2, x[0] == 1, y[0] ==
     -1}, {x[t], y[t]}, t] /. {w1 -> w1, w2 -> w2, t1 -> t1, t2 -> t2};

sol = solutions[1, 2, 3, 4];

Print["The solutions are: ", sol];

Export["plot.pdf", Plot[Evaluate[{x[t], y[t]} /. sol], {t, 0, 10}]]
