(* ::Package::  *)

(* ::Input::  *)

Needs["DatabaseLink`"]

Needs["JLink`"]

currentDir = Directory[];

Print["script is running from: ", currentDir]

dbDir = FileNameJoin[{currentDir, "data"}];

(* create the data directory *)

If[Not[FileExistsQ[dbDir]],
    CreateDirectory[dbDir];
    Print["Created directory: ", dbDir, "\n"]
    ,
    Print["Directory already exists: ", dbDir, "\n"]
];

(* create the database file *)

(* only create the file if it does not exist*)

Print["cmd args: ", $CommandLine, "\n"]

min = 4; max = 69;

(* get the size of the table from the command line *)

If[Length[$CommandLine] >= 4,
    tableSize = ToExpression[$CommandLine[[4]]];
    Print["Using size from the command line", "\n"]
    ,
    tableSize = 10;
    Print["Using fixed size", "\n"]
];

Print["tableSize: ", tableSize, "\n"]

(* get the seed from the cmd or else used a fixed size *)

If[Length[$CommandLine] >= 5,
    seed = ToExpression[$CommandLine[[5]]];
    SeedRandom[seed, Method -> "MersenneTwister"];
    Print["Using seed from the command line: ", seed]
    ,
    seed = 1337;
    SeedRandom[seed, Method -> "MersenneTwister"];
    Print["Using fixed seed: ", seed, "\n"]
]

data =
    Table[
        With[{randInt = RandomInteger[{min, max}]},
            {randInt, N[Log2[randInt]]}
        ]
        ,
        tableSize
    ];

conn = OpenSQLConnection[JDBC["SQLite", FileNameJoin[{dbDir, "mydatabase.db"
    }]]];

SQLExecute[conn, "DROP TABLE IF EXISTS mytable"];

SQLExecute[conn, "CREATE TABLE IF NOT EXISTS mytable (id INTEGER, number INTEGER, log2 REAL)"
    ];

(* need to measure the performance of the database update*)

{dbUpdateTime, funcRes} =
    AbsoluteTiming[
        Do[
            SQLExecute[conn, "INSERT INTO mytable (id, number, log2) VALUES (?, ?, ?)",
                 {idx, data[[idx, 1]], data[[idx, 2]]}];
            If[tableSize <= 100,
                Print["inserted: ", data[[idx, 1]], " ", data[[idx, 2
                    ]]]
            ]
            ,
            {idx, 1, Length[data], 1}
        ];
    ];

(* offset will always start from 0 *)

item[offset_] :=
    SQLExecute[conn, StringTemplate["SELECT * FROM mytable LIMIT 1 OFFSET ``"
        ][offset - 1]];

itemNumberIs69 = SQLExecute[conn, "SELECT * FROM mytable WHERE id = 69"
    ];

printer[number_] :=
    Print[StringTemplate["item`` :"][number], item[number], "\n"];

printer[69];

Print["itemNumberIs69: ", itemNumberIs69, "\n"]

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

(* 
selectedDataCompiled = Select[allData, isPrimeCompiled[#[[1]]]&];

selectedData = Select[allData, PrimeQ[#[[1]]]&]; *)

Print["The database has been created.\n"]

Print["Size of the .db file: ", N[FileByteCount[FileNameJoin[{dbDir, 
    "mydatabase.db"}]]] / Power[1024, 2], " MB\n"]

Print["Updating the database took: ", dbUpdateTime, " seconds\n"]

CloseSQLConnection[conn]
