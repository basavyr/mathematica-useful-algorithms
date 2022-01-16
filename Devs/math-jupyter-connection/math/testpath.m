#!/usr/bin/env wolframscript

(* ::Input:: *)
ClearAll["Global`*"]


data=Table[{x,2*x+1},{x,0,10}];

Print[data]

staticpath="/Users/robertpoenaru/Library/Mobile\ Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/mathematica-useful-algorithms/Devs/math-jupyter-connection/math";

finalpath=StringJoin[staticpath,"/data.csv"];

Export[finalpath,TableForm[data]]