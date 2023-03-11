Needs["DatabaseLink`"]

Needs["JLink`"]

dataPath = FileNameJoin[{Directory[], "data"}];

min = 4;

max = 69;

(* get the size of the table from the command line *)

tableSize =
    If[Length[$CommandLine] > 3,
        ToExpression[$CommandLine[[4]]]
        ,
        3
    ];

SeedRandom[1337, Method -> {"MersenneTwister", 32}];

data =
    Table[
        With[{randInt = RandomInteger[{min, max}]},
            {randInt, N[Log2[randInt]]}
        ]
        ,
        tableSize
    ];

conn = OpenSQLConnection[JDBC["SQLite", FileNameJoin[{dataPath, "mydatabase.db"
    }]]];

SQLExecute[conn, "CREATE TABLE IF NOT EXISTS mytable (number INTEGER, log2 REAL)"
    ];

SQLExecute[conn, "DELETE FROM mytable"];

Do[SQLExecute[conn, "INSERT INTO mytable VALUES (?, ?)", data[[i]]], 
    {i, Length[data]}];

(* select the 69th item from mytable*)

item69 = SQLExecute[conn, "SELECT * FROM mytable WHERE number = 69"];

(* create a function that checks if a number is prime*)

isPrimeCompiled =
    Compile[
        {{n, _Integer, 0}}
        ,
        Module[{i},
            If[n < 2,
                Return[False]
            ];
            If[n == 2,
                Return[True]
            ];
            If[EvenQ[n],
                Return[False]
            ];
            For[i = 3, i <= Sqrt[n], i += 2,
                If[Mod[n, i] == 0,
                    Return[False]
                ]
            ];
            True
        ]
    ];

allData = SQLExecute[conn, "SELECT * FROM mytable"];

selectedDataCompiled = Select[allData, isPrimeCompiled[#[[1]]]&];

selectedData = Select[allData, PrimeQ[#[[1]]]&];

Do[Print["Prime pairs: ", i], {i, selectedData}];

CloseSQLConnection[conn]
