#!/usr/bin/env wolframscript

(* ::Input:: *)
ClearAll["Global`*"]
data=Table[{x,2*x+1},{x,0,10}];
staticpath="/Users/robertpoenaru/Library/Mobile\ Documents/com~apple~CloudDocs/Work/Pipeline/DevWorkspace/Github/mathematica-useful-algorithms/Devs/math-jupyter-connection/math";
finalpath=StringJoin[staticpath,"/data.csv"];
Export[finalpath,TableForm[data]];


(* get the current path of the file using a function that works within the script executables*)
(* source: https://mathematica.stackexchange.com/questions/133276/how-to-find-source-of-frontendobjectnotavail-warning *)
parentPath = $InputFileName;

cleanpath=StringDrop[parentPath,-11];
Print[cleanpath]