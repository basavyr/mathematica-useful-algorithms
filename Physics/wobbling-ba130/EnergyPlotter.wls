#!/usr/bin/env wolframscript

parampath="/Users/basavyr/Documents/Work/DFT/mathematica-useful-algorithms/Physics/wobbling-ba130/fit_params.dat";
band1path="/Users/basavyr/Documents/Work/DFT/mathematica-useful-algorithms/Physics/wobbling-ba130/ba_130_B1_band.dat";
band2path="/Users/basavyr/Documents/Work/DFT/mathematica-useful-algorithms/Physics/wobbling-ba130/ba_130_B2_band.dat";



params=Flatten[Import[parampath]];
dataBand1=Import[band1path];
dataBand2=Import[band2path];

Print[params]