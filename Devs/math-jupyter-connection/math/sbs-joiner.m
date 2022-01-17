#!/usr/bin/env wolframscript

(* Create a list of random parameters *)
randomParams[n_]:=Table[{RandomInteger[{1,5},{-8,8}]},{i,1,n}];
(* construct the mathematical function that takes one argument and two random parameters *)
mfunc[arg_,params_]:=If[arg == 0, 1, pars[[1]]*1/arg - arg^2*pars[[2]]];
(* generate a table with numerical data based on the mathematical function *)
generateData[params_,xlimit_,dx_]:=Table[{x,mfunc[x,params]},{x,-limit,limit,dx}];
(* create a set with multiple data tables based on the numerical data generated from the set of parameters *)
createTable[paramsList_,xlimit_,dx_]:=Table[generateData[paramList[[idx]],xlimit,dx],{idx,1,Length[paramList]}];

dataPath=StringDrop[ToString[$InputFileName],-12];
filepath[name_,type_,idx_]:=StringTemplate["````_``.``"][dataPath,name,idx,type];
Print[filepath["table","csv",1]]