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
