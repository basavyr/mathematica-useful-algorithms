(* ::Package:: *)

(* ::Chapter:: *)
(*Scatter Plot*)


(* ::Input:: *)
(*ClearAll["Global`*"]*)


(* ::Section:: *)
(*Helper functions (paths, exports, etc.)*)


(* ::Input:: *)
(*(* remove the math path and change to data directory when exporting files *)*)
(*localpath=StringDrop[ToString[NotebookDirectory[]],-5];*)
(*datadir=StringJoin[localpath,"data/"];*)
(*datapath[name_]:=StringTemplate["``data/``"][localpath,name];*)
(*datafile[id_,type_]:=datapath[StringTemplate["file_``.``"][id,type]];*)
(*csvtable[id_]:=datapath[StringTemplate["table_``.csv"][id]];*)
(*pdfdatafiles[n_]:=Table[datafile[id,"pdf"],{id,1,n}];*)
(*(* export function that saves an object into the data directory *)*)
(*exporter[path_,object_]:=Export[path,object];*)
(*grider[table_]:=Grid[table,Frame->All];*)
(*tabular[table_]:=TableForm[table];*)


(* ::Section:: *)
(*Parametrized scatter plots for a mathematical function*)


(* ::Text:: *)
(*Define the mathematical function that will be evaluated*)
(*f(x) = a 1/x-x^2*b*)


(* ::Input:: *)
(*mfunc[arg_,pars_]:=If[arg==0,1,pars[[1]]*1/arg-arg^2*pars[[2]]];*)


(* ::Section:: *)
(*Graphical representation of the mathematical function*)


(* ::Subsection:: *)
(*Working with a static list for the parameter set *)


(* ::Input:: *)
(*(* a list of parameters to be tested *)*)
(*listOfParams={{-1,-2},{2,3},{0,-4},{2,4}};*)
(*setlabel[params_]:=StringTemplate["a=`` | b=``"][params[[1]],params[[2]]];*)
(*labels[params_]:=Table[setlabel[params[[id]]],{id,1,Length[params]}];*)
(*plotTable[params_,limit_,dx_]:=Table[Table[{x,mfunc[x,params[[id]]]},{x,-limit,limit,dx}],{id,1,Length[params]}];*)
(*listplot[params_,limit_,dx_]:=ListPlot[plotTable[params,limit,dx],Joined->True,PlotMarkers->{Automatic, Small},ImageSize->Large,Frame->True,Axes->True,FrameStyle->Directive[Black,Thick],FrameLabel->{"x","\!\(\*SubscriptBox[\(m\), \(func\)]\)(x)"},LabelStyle->{18,Bold,Black,FontFamily->"Times New Roman"},PlotLegends->Placed[labels[params],Scaled[{0.7,0.25}]],AspectRatio->1];*)


(* ::Title:: *)
(*Testing the static procedure of ListPlot*)


(* ::Input:: *)
(*(* VALUES TO BE USED THROUGHOUT THE CALCULATIONS *)*)
(*xlimit=2.5;*)
(*dx=0.1;*)
(*pl1=listOfParams;*)
(*ptable1=plotTable[pl1,xlimit,dx];*)
(*exporter[datafile[1,"pdf"],listplot[pl1,xlimit,dx]];*)


(* ::Section:: *)
(*Randomised algorithm for generating objects*)


(* ::Input:: *)
(*rdpars[]:={RandomInteger[{0,4}],RandomInteger[{-6,6}]};*)
(*(*create a table with parameter sets *)*)
(*parsTable[n_]:=Table[rdpars[],{i,1,n}];*)
(*gfx[n_]:=listplot[rdpars[n]];*)
(*gfxObjects[n_]:=Table[gfx[rdpars],{i,1,n}];*)


(* ::Section:: *)
(*Create a pdf cleaner procedure*)


(* ::Input:: *)
(*pdflist=FileNames["*.pdf",datadir];*)
(*cleanpdf[]:=If[Length[pdflist]>0,DeleteFile[pdflist],Print["No cleaning required"]];*)
(*(*cleanpdf[]*)*)


(* ::Section:: *)
(*Implement csv table maker from a random list of parameters *)


(* ::Input:: *)
(*header={{"x","f(x;a,b)"}};*)
(*paramheader[params_]:={{"a","b"},{params[[1]],params[[2]]}};*)
(*specialHeader[h1_,h2_]:=Join[h2,h1];*)


(* ::Input:: *)
(*tablemaker[xlimit_,dx_,params_]:=Table[{x,mfunc[x,params]},{x,-xlimit,xlimit,dx}];*)
(*joiner[header_,data_]:=Join[header,data];*)
(**)


(* ::Input:: *)
(*(* Create the header with the values for the parameter set *)*)
(*sexyh[header_,paramset_]:=specialHeader[header,paramheader[paramset]];*)
(*(* create the table with arguments and the corresponding function values *)*)
(*sexydata[limit_,dx_,paramset_]:=tablemaker[limit,dx,paramset];*)
(*(* join the special header and the numerical data *)*)
(*sexyjoiner[sexyheader_,sexydata_]:=tabular[joiner[sexyheader,sexydata]];*)


(* ::Input:: *)
(*sh1=sexyh[header,pl1[[1]]];*)
(*sd1=sexydata[xlimit,dx,pl1[[1]]];*)
(*sJJ1=sexyjoiner[sh1,sd1];*)
(*exporter[csvtable[1],sJJ1];*)


(* ::Input:: *)
(*TableForm[{{"a","b"},{-1,-2},{"x","f(x;a,b)"}}]*)
