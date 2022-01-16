#!/usr/bin/env wolframscript

(* ::Input:: *)
ClearAll["Global`*"]

(* ::Input:: *)
localpath=StringDrop[ToString[NotebookDirectory[]],-5];
datadir=StringJoin[localpath,"data/"];
datapath[name_]:=StringTemplate["``data/``"][localpath,name];
datafile[id_,type_]:=datapath[StringTemplate["file_``.``"][id,type]];
csvtable[id_]:=datapath[StringTemplate["table_``.csv"][id]];
pdfdatafiles[n_]:=Table[datafile[id,"pdf"],{id,1,n}];
exporter[path_,object_]:=Export[path,object];
grider[table_]:=Grid[table,Frame->All];
tabular[table_]:=TableForm[table];

(* ::Input:: *)
mfunc[arg_,pars_]:=If[arg==0,1,pars[[1]]*1/arg-arg^2*pars[[2]]];

(* ::Input:: *)
listOfParams={{-1,-2},{2,3},{0,-4},{2,4}};
setlabel[params_]:=StringTemplate["a=`` | b=``"][params[[1]],params[[2]]];
labels[params_]:=Table[setlabel[params[[id]]],{id,1,Length[params]}];
plotTable[params_,limit_,dx_]:=Table[Table[{x,mfunc[x,params[[id]]]},{x,-limit,limit,dx}],{id,1,Length[params]}];
listplot[params_,limit_,dx_]:=ListPlot[plotTable[params,limit,dx],Joined->True,PlotMarkers->{Automatic, Small},ImageSize->Large,Frame->True,Axes->True,FrameStyle->Directive[Black,Thick],FrameLabel->{"x","\!\(\*SubscriptBox[\(m\), \(func\)]\)(x)"},LabelStyle->{18,Bold,Black,FontFamily->"Times New Roman"},PlotLegends->Placed[labels[params],Scaled[{0.7,0.25}]],AspectRatio->1];

(* ::Input:: *)
xlimit=2.5;
dx=0.1;
pl1=listOfParams;
ptable1=plotTable[pl1,xlimit,dx];
exporter[datafile[1,"pdf"],listplot[pl1,xlimit,dx]];

(* ::Input:: *)
rdpars[]:={RandomInteger[{0,4}],RandomInteger[{-6,6}]};
parsTable[n_]:=Table[rdpars[],{i,1,n}];
gfx[n_]:=listplot[rdpars[n]];
gfxObjects[n_]:=Table[gfx[rdpars],{i,1,n}];

(* ::Input:: *)
pdflist=FileNames["*.pdf",datadir];
cleanpdf[]:=If[Length[pdflist]>0,DeleteFile[pdflist],Print["No cleaning required"]];

(* ::Input:: *)
header={{"x","f(x;a,b)"}};
paramheader[params_]:={{"a","b"},{params[[1]],params[[2]]}};
specialHeader[h1_,h2_]:=Join[h2,h1];

(* ::Input:: *)
tablemaker[xlimit_,dx_,params_]:=Table[{x,mfunc[x,params]},{x,-xlimit,xlimit,dx}];
joiner[header_,data_]:=Join[header,data];

(* ::Input:: *)
sexyh[header_,paramset_]:=specialHeader[header,paramheader[paramset]];
sexydata[limit_,dx_,paramset_]:=tablemaker[limit,dx,paramset];
sexyjoiner[sexyheader_,sexydata_]:=tabular[joiner[sexyheader,sexydata]];

(* ::Input:: *)
sh1=sexyh[header,pl1[[1]]];
sd1=sexydata[xlimit,dx,pl1[[1]]];
sJJ1=sexyjoiner[sh1,sd1];
exporter[csvtable[1],sJJ1];

(* ::Input:: *)
TableForm[{{"a","b"},{-1,-2},{"x","f(x;a,b)"}}]
