# Lexical Scanner
- The Mid-term "Compiler" project by Duc Tran Van, Duy Duong Duc, Anh Le Tuan.
# Installation
- Install the required packages by the following command:
```cmd
pip install -r requirements.txt
```
# Input
- The input file was stored in `./input` directory
- Starting file is `main.py`.
```py
def generate_token(file):
    # Some hidden code

generate_token("{input_file_name}")
```
- Put `{input_file_name}.vc` file in `./input` directory and put file name in `generate_token` function.
- Run the `main.py` file.
# Output
- The output was stored in `./output/{input_file_name}` directory.
- `graph.dat` file:
    - Contains info about automata-graph.
    - Categories are `ALPHABET`, `STATE`, `INITIAL_STATE`, `ACCEPTING_STATES`, and `TRANSITIONS`.
    - Each element will be included consequently under the categories.
    - Each category ends with a blank line.
    - Example file:
        ```py
        ALPHABET
        space
        boolean
        arithmetic_1
        ...

        STATE
        0
        1
        2
        ...

        INITIAL_STATE
        0

        ACCEPTING_STATES
        1 SPACE
        2 BOOLEANLITERAL
        3 ARITHMETIC
        ...

        TRANSITIONS
        0 space 1
        0 boolean 2
        0 arithmetic_1 3
        ...
        ```
- `table.dat` file:
    - Contains info about automata-graph by display into a table.
    - The first row is the alphabet.
    - The first column is the state.
    - Each cell is a next_state which display the transition `state -> alphabet -> next_state`.
    - Example file:
        ```py
        +----------------------------------------------------------------------------------------------------------------------------------------------------------+
        |state|space|boolean|arithmetic_1|keyword|digit|relational|dot|equality|assignment|eof|separator|character|arithmetic_2|double_quote|other|exponent|logical|
        +-----+-----+-------+------------+-------+-----+----------+---+--------+----------+---+---------+---------+------------+------------+-----+--------+-------+
        |  0  |  1  |   2   |      3     |   4   |  5  |     6    | 7 |    8   |     9    | 10|    11   |    12   |      3     |     13     |     |   12   |   14  |
        +-----+-----+-------+------------+-------+-----+----------+---+--------+----------+---+---------+---------+------------+------------+-----+--------+-------+
        |  1  |  1  |       |            |       |     |          |   |        |          |   |         |         |            |            |     |        |       |
        +-----+-----+-------+------------+-------+-----+----------+---+--------+----------+---+---------+---------+------------+------------+-----+--------+-------+
        |  5  |     |       |            |       |  5  |          | 33|        |          |   |         |         |            |            |     |   34   |       |
        +-----+-----+-------+------------+-------+-----+----------+---+--------+----------+---+---------+---------+------------+------------+-----+--------+-------+
        |  7  |     |       |            |       |  29 |          |   |        |          |   |         |         |            |            |     |        |       |
        +-----+-----+-------+------------+-------+-----+----------+---+--------+----------+---+---------+---------+------------+------------+-----+--------+-------+
        ...
        ```
- `{input_file_name}.vctok` file:
    - Contains info about the token.
    - Each line contains a token.
    - Example file:
        ```py
        void
        main
        (
        )
        {
        int
        n
        ```
- `{input_file_name}.verbose.vctok` file:
    - Contains info about the token with detailed information.
    - Each line contains a token with `kind`, `spelling`, and `position`.
    - Example file:
        ```py
        Kind = 4 [KEYWORD], spelling = "void", position = 3(1)..3(4)
        Kind = 12 [IDENTIFIER], spelling = "main", position = 3(6)..3(9)
        Kind = 11 [SEPARATOR], spelling = "(", position = 3(10)..3(10)
        Kind = 11 [SEPARATOR], spelling = ")", position = 3(11)..3(11)
        Kind = 11 [SEPARATOR], spelling = "{", position = 3(13)..3(13)
        ```
