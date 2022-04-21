#!/usr/bin/env wolframscript


parampath="/Users/basavyr/Documents/Work/DFT/mathematica-useful-algorithms/Physics/wobbling-ba130/fit_params.dat";
band1path="/Users/basavyr/Documents/Work/DFT/mathematica-useful-algorithms/Physics/wobbling-ba130/ba_130_B1_band.dat";
band2path="/Users/basavyr/Documents/Work/DFT/mathematica-useful-algorithms/Physics/wobbling-ba130/ba_130_B2_band.dat";



params=Flatten[Import[parampath]];
dataBand1=Import[band1path];
dataBand2=Import[band2path];



spinsband1=Table[dataBand1[[i,1]],{i,1,Length[dataBand1]}];
spinsband2=Table[dataBand2[[i,1]],{i,1,Length[dataBand2]}];
band1exp=Table[dataBand1[[i,2]],{i,1,Length[dataBand1]}];
band2exp=Table[dataBand2[[i,2]],{i,1,Length[dataBand2]}];
band1th=Table[dataBand1[[i,3]],{i,1,Length[dataBand1]}];
band2th=Table[dataBand2[[i,3]],{i,1,Length[dataBand2]}];



bandmaker[start_,shift_,energies_]:=Table[{{start,energies[[i]]},{start+shift,energies[[i]]}},{i,1,Length[energies]}];
energyplotter[energies_,color_]:=ListLinePlot[energies,Axes->{False,True,False,False},Frame->None,AxesStyle->Directive[Black,Thick],ImageSize->350,AspectRatio->1.4,PlotStyle->Directive[Thick,color],AxesLabel->{"","E [MeV]"},LabelStyle->{19,Bold,Black,FontFamily->"Arial"}];
shower[energiesexp_,energiesth_,spins_,color_,band_]:=Show[energyplotter[bandmaker[1,1,energiesexp],Black],energyplotter[bandmaker[2.3,1,energiesth],color],PlotRange->{Full,{Min[energiesexp]-1.5,Max[energiesexp]+0.3}},Epilog->{Table[Inset[Style[StringTemplate["\!\(\*SuperscriptBox[\(``\), \(+\)]\)"][spins[[i]]],Black,17,Bold,Italic],{1.5,energiesexp[[i]]+0.25}],{i,1,Length[energiesexp]}],Table[Inset[Style[StringTemplate["\!\(\*SuperscriptBox[\(``\), \(+\)]\)"][spins[[i]]],Black,17,Bold,Italic],{2.8,energiesth[[i]]+0.25}],{i,1,Length[energiesth]}],Inset[Style["Exp.",Black,Bold,17],{1.5,-.5}],Inset[Style["Th.",Black,Bold,17],{2.8,-.5}],Inset[Framed[Style[band,Black,Italic,Bold,17]],{2.1,-.5}]}];
plot1=shower[band1exp,band1th,spinsband1,Red,"B1"];
plot2=shower[band2exp,band2th,spinsband2,Blue,"B2"];
Export["/Users/basavyr/Documents/Work/PhD/phdthesis/Chapters/Figures/ba130-band1.pdf",plot1,ImageResolution->1200];
Export["/Users/basavyr/Documents/Work/PhD/phdthesis/Chapters/Figures/ba130-band2.pdf",plot2,ImageResolution->1200];
