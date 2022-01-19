#!/usr/bin/env wolframscript

(* generate path for saving the tables *)
(* files must be saved in the /data directory *)
dataDirectory=StringJoin[StringDrop[ToString[$InputFileName],-13],"data/"];
(* generate function that exports csv files to proper location with name and id for each file*)
generateFilePath[filename_,filetype_,fileid_]:=StringTemplate["````_``.``"][dataDirectory,filename,fileid,filetype];
(* generate a static file foe every export to csv format *)
FILEPATH[id_]:=generateFilePath["csvTable","csv",id];
(* generate a random pair of parameters (a,b) *)
rdPair[]:={RandomInteger[{1,5}],RandomInteger[{-8,8}]};
(* generate a list of FIXED length with random pairs*)
paramList[Nsize_]:=Table[rdPair[],{i,1,Nsize}];
(*generate a header with the numerical valiues of the parameters*)
paramHeader[params_]:={{"a","b"},{params[[1]],params[[2]]}};
(* generate the full header of a single table with given pair of "a" and "b"*)
fullHeader[params_]:=Join[paramHeader[params],{{"x","f(x)"}},1];
(* implement mathematical function with a set of two arbitrary paramaters*)
mfunc[arg_,params_]:=If[arg == 0, 1, params[[1]]*1/arg - arg^2*params[[2]]];
(* create a single FULL table with header (legend) and numerical data for a single parameter pair*)
oneTable[params_,xlimit_,dx_]:=Join[fullHeader[params],Table[{SetPrecision[x,4],SetPrecision[mfunc[x,params],4]},{x,-xlimit,xlimit,dx}],1];
(* generate a full table for an entire list of parameters (list of random pairs rdPair[]) *)
fullTable[paramList_,xlimit_,dx_]:=Table[oneTable[paramList[[idx]],xlimit,dx],{idx,1,Length[paramList]}];
joinProcedure[fullTable_]:=Module[{localT=fullTable},
temp=localT[[1]];
For[i=2,i<=Length[localT],i++,temp=Join[temp,localT[[i]],2]];
temp
];


(* TESTING PROCEDURE *)
NPARAMS=5;
XLIMIT=5;
DX=0.1;
PARAMLIST=paramList[NPARAMS];
FILEID=1
Export[FILEPATH[FILEID],joinProcedure[fullTable[PARAMLIST,XLIMIT,DX]]];