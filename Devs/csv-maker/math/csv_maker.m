(* ::Package:: *)

(* ::Input:: *)
(*ClearAll["Global`*"]*)


(* ::Input:: *)
(*exporter[path_,data_]:=Export[path,data];*)
(*grider[object_]:=Grid[object,Frame->All];*)
(*tabular[object_]:=TableForm[object];*)


(* ::Subsection:: *)
(*Obtain the current path and create path for `.csv` tables*)


(* ::Input:: *)
(*currentpath[name_]:=StringTemplate["````.csv"][NotebookDirectory[],name];*)
(*csv[id_]:=currentpath[StringTemplate["table_``"][id]];*)


(* ::Subsection:: *)
(*Function: Two(2) parameters and one(1) argument*)
(* - two params { p1 , p2 }*)
(* - one argument x*)


(* ::Subsection:: *)
(*Create random data for generating tables*)


(* ::Input:: *)
(*(* FUNCTIONS *)*)
(*f1[x_,p1_,p2_]:=If[p1!=0&&p2!=0,p1*x^3+p2,0];*)
(*f2[x_,p1_,p2_]:=If[p1!=0&&p2!=0,p1/p2*x^5+p1*p2,0];*)
(*f3[x_,p1_,p2_]:=If[p1!=0&&p2!=0,p1*x^5+p1/p2,0];*)


(* ::Input:: *)
(*(* DATA GENERATORS *)*)
(*generateParamSet[]:={RandomReal[{1,4}],RandomInteger[{2,8}]};*)
(* (* generate a test parameter set *)*)
(*limit=10;*)
(*dp=0.1;*)
(*npoints=(2limit)/dp+1;*)
(*generateData[fi_,paramSet_]:=Table[{SetPrecision[x,5],SetPrecision[fi[x,paramSet[[1]],paramSet[[2]]],5]},{x,-limit,limit,dp}];*)


(* ::Subsection:: *)
(*Create headers for the tabular data*)


(* ::Input:: *)
(*pheader[i_]:={StringTemplate["p``1"][i],StringTemplate["p``2"][i]};*)
(*paramvalues[params_]:={params[[1]],params[[2]]};*)
(*header[i_]:={"x",StringTemplate["f(x;p_``)"][i]};*)
(*specialHeader[params_,i_]:=Join[{pheader[i],paramvalues[params]},{header[i]}];*)


(* ::Subsection:: *)
(*function for saving a table as a csv file*)


(* ::Input:: *)
(*makeCSV[table_,id_]:=exporter[csv[id],TableForm[table]];*)


(* ::Subsection:: *)
(*Create a table with the special header and the numerical data*)


(* ::Input:: *)
(*(* JOIN THE SPECIAL HEADER AND THE NUMERICAL DATA *)*)
(*joiner[header_,data_]:=Join[header,data,1];*)


(* ::Input:: *)
(*(* CREATE A TABLE FROM SCRATCH, ONLY PROVIDING THE ID AND A PARAMETER *)*)
(*createTable[id_,paramset_]:=joiner[specialHeader[paramset,id],generateData[f1,paramset]];*)


(* ::Input:: *)
(*completeGenerator[func_,id_]:=Module[{localID=id,localfunc=func},*)
(*localpS=generateParamSet[];*)
(*localhh=specialHeader[localpS,localID];*)
(*localdata=generateData[localfunc,localpS];*)
(*localtable=joiner[localhh,localdata];*)
(*makeCSV[localtable,localID];*)
(*];*)


(* ::Subsection:: *)
(*batch table maker and ".csv" exporter*)


(* ::Input:: *)
(*table1=createTable[1,generateParamSet[]];*)
(*csvtable[id_]:=makeCSV[createTable[id,generateParamSet[]],id];*)
(*Do[csvtable[x],{x,1,10,1}]*)


(* ::Subsection:: *)
(*create archive from all the csv files*)


(* ::Input:: *)
(*findfiles[type_]:=FileNames[StringTemplate["*.``"][type],NotebookDirectory[]];*)
(*getCSVFiles[list_]:=Module[{localL=list},*)
(*l0={};*)
(*csvlist=StringContainsQ[localL,".csv"];*)
(*Do[If[csvlist[[idx]]==True,AppendTo[l0,localL[[idx]]]],{idx,1,Length[localL]}];*)
(*l0*)
(*];*)
(*appendpath[filelist_]:=Table[FileNameJoin[{NotebookDirectory[],filelist[[idx]]}],{idx,1,Length[filelist]}];*)
(*zipfile[files_]:=CreateArchive[appendpath[files],StringTemplate["``csvfiles.tar.gz"][NotebookDirectory[]],OverwriteTarget->True];*)
