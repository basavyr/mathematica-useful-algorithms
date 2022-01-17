#!/usr/bin/env wolframscript

(* ::Input:: *)
ClearAll["Global`*"]

(* get the current path of the file using a function that works within the script executables*)
(* source: https://mathematica.stackexchange.com/questions/133276/how-to-find-source-of-frontendobjectnotavail-warning *)
parentPath = ToString[$InputFileName];
dataPath=StringJoin[StringDrop[parentPath,-15],"data/"];
filename[name_,idx_,type_]:=StringJoin[dataPath,StringTemplate["``_``.``"][name,idx,type]];
(* Export[filename["circle",1,".pdf"],Graphics[Circle[]]] *)

(* numerical parameters that will be used throughout the calculations *)
limit=5;
dx=0.1;

(* test the joining process of two tables *)
createTables[n_]:=Table[Table[{x,2*x+RandomReal[{1,10}]},{x,-limit,limit}],{i,1,n}];

(* function that joins two tables side-by-side *)
lateralJoiner[table1_,table2_]:=Join[table1,table2,2];



T4=createTables[4];
t1=T4[[1]];
t2=T4[[2]];
(* Print[TableForm[t1]]
Print[t2] *)

tt={};
tt=Do[lateralJoiner[t1,T4[[idx]]],{idx,2,Length[T4]}]
Print[tt]