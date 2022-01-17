#!/usr/bin/env wolframscript

(* ::Input:: *)
ClearAll["Global`*"]

(* get the current path of the file using a function that works within the script executables*)
(* source: https://mathematica.stackexchange.com/questions/133276/how-to-find-source-of-frontendobjectnotavail-warning *)
parentPath = ToString[$InputFileName];
dataPath=StringJoin[StringDrop[parentPath,-15],"data/"];
filename[name_,idx_,type_]:=StringJoin[dataPath,StringTemplate["``_``.``"][name,idx,type]];
(* Export[filename["circle",1,".pdf"],Graphics[Circle[]]] *)

(* test the joining process of two tables
limit=5;
dx=0.1;
t1=Table[{x,2*x+1},{x,-limit,limit}];
t2=Table[{x,2*x-1},{x,-limit,limit}];
createTables[n_]:=Table[Table[{x,2*x+RandomReal[{1,10}]},{x,-limit,limit}],{i,1,n}];
(* function that joins two tables side-by-side *)
lateralJoiner[table1_,table2_]:=Join[table1,table2,2];

T4=createTables[4];
Print[T4] *)