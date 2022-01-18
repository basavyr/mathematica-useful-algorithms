#!/usr/bin/env wolframscript
ClearAll["Global`*"];
(* Create a pair of random parameters *)
rdPair[]:={RandomInteger[{1,5}],RandomInteger[{-8,8}]};
(* Create a list of random parameters *)
randomParams[n_]:=Table[rdPair[],{i,1,n}];
(* construct the mathematical function that takes one argument and two random parameters *)
mfunc[arg_,params_]:=If[arg == 0, 1, params[[1]]*1/arg - arg^2*params[[2]]];
(* generate a table with numerical data based on the mathematical function *)
generateData[params_,xlimit_,dx_]:=Table[{SetPrecision[x,4],SetPrecision[mfunc[x,params],4]},{x,-xlimit,xlimit,dx}];
(* create a set with multiple data tables based on the numerical data generated from the set of parameters *)
createTable[paramsList_,xlimit_,dx_]:=Table[generateData[paramsList[[idx]],xlimit,dx],{idx,1,Length[paramsList]}];
(* get the current path of the `.m` script and change the final path *)
dataPath=StringJoin[StringDrop[ToString[$InputFileName],-17],"data/"];
(* create a function that generates a path based on a name for the file and the type*)
filepath[name_,type_,idx_]:=StringTemplate["````_``.``"][dataPath,name,idx,type];
tabular[table_]:=TableForm[table];
exporter[path_,object_]:=Export[path,object]; 
exportCSV[table_,id_]:=exporter[filepath["table","csv",id],table];
(* join the header with the numerical data for a single set of params *)
joiner[header_, data_] := Join[header, data];
(* create the headers that will pe added at the front of the csv tables *)
header0 = {{"x", "f(x;a,b)"}};
paramHeader[params_] := {{"a", "b"}, {params[[1]], params[[2]]}};
specialHeader[h1_, h2_] := Join[h2, h1];



(* testing the implementation *)
Npars=5
rdpars=randomParams[Npars];
xlimit=5;
dx=0.1;

(* Create a joint table (header + numerical data) for a single set of parameters (a,b) *)
generateTable[params_,xlimit_,dx_]:=joiner[specialHeader[header0,paramHeader[params]],generateData[params,xlimit,dx]];
batchTableGenerator[paramsList_,xlimit_,dx_]:=Table[joiner[specialHeader[header0,paramHeader[ paramsList[[idx]] ] ],generateData[paramsList[[idx]],xlimit,dx] ],{idx,1,Length[paramsList]} ];
(*generate csv files from the joint  and export them in batch*)
(* bathExportCSV[T_]:=Do[exportCSV[T[[id]],id],{id,1,Length[T]}]; *)

(* create the procedure for joining tables side-by-side*)
sbsProcedure[T_]:=Module[{localT=T},
temp=localT[[1]];
(* create the for loop in which the temp object gets a new table with each iteration*)
For[idx=2,idx<=Length[localT],idx++,temp=Join[temp,localT[[idx]],2]];
temp
];

(* Testing the batch table generator and the export *)
T=generateTable[rdpars[[1]],xlimit,dx];
ST=sbsProcedure[Table[generateData[rdPair[],xlimit,dx],{i,1,10}]];
exportCSV[ST,1]
