#!/usr/bin/env wolframscript

(* ::Input:: *)
ClearAll["Global`*"]

(* get the current path of the file using a function that works within the script executables*)
(* source: https://mathematica.stackexchange.com/questions/133276/how-to-find-source-of-frontendobjectnotavail-warning *)
parentPath=ToString[$InputFileName];
dataPath=StringJoin[StringDrop[parentPath,-15],"data/"];
filename[name_,idx_,type_]:=StringJoin[dataPath,StringTemplate["``_``.``"][name,idx,type]];
(* Export[filename["circle",1,".pdf"],Graphics[Circle[]]] *)

(* numerical parameters that will be used throughout the calculations *)
limit=5;
dx=0.1;

(* test the joining process of two tables *)
createTables[n_]:=Table[Table[{SetPrecision[x,4],SetPrecision[2*x+RandomReal[{1,10}],4]},{x,-limit,limit,dx}],{i,1,n}];

(* function that joins two tables side-by-side *)
lateralJoiner[table1_,table2_]:=Join[table1,table2,2];

(* export an object to a custom path *)
tabular[table_]:=TableForm[table];
export[object_,id_]:=Export[filename["table",id,"csv"],object];


(* Module that joins the list of tables T_i={x,f(x}} where i>=2 to an initial table component T_1={x,f(x)} *)
procedure[T_]:=Module[{localT=T},
temp=localT[[1]];
For[i=2,i<=Length[localT],i++,temp=Join[temp,localT[[i]],2]];
temp
];


T=createTables[5];
result=procedure[T];
export[result,1];