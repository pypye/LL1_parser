# LL1 Parser
- The Final "Compiler" project by Duc Tran Van, Duy Duong Duc, Anh Le Tuan.
# Installation
- Install the required packages by the following command:
```cmd
pip install -r requirements.txt
```
# Input
- The input file was stored in `./input` directory
- Starting file is `main.py`.
```py
if __name__ == "__main__":
    file = "in"
    generate_token(file)
    ast = LL1_parser(file)
    ast = pretty_print_ast(file, ast)
    ast = bracket_print(file, ast)
```
# Output
- The output was stored in `./output/{input_file_name}` directory.
  - out_ast_bracket.vcps: Display abstract syntax tree as bracket sequence.
  ```
  ( ( int i ; ) ( int j ; ) ( int gcd ( \( ( ( int a ) ( , ( int b ) ) ) \) ) ( { ( if \( ( b ( == 0 ) ) \) ( { ( return a ; ) } ) ( else ( return ( gcd ( \( ( b ( , ( a ( - ( ( \( ( a ( / b ) ) \) ) ( * b ) ) ) ) ) ) \) ) ) ; ) ) ) } ) ) ( void main ( \( \) ) ( { ( ( ( i ( = ( getInt ( \( \) ) ) ) ) ; ) ( ( ( j ( = ( getInt ( \( \) ) ) ) ) ; ) ( ( putIntLn ( \( ( gcd ( \( ( i ( , j ) ) \) ) ) \) ) ) ; ) ) ) } ) ) ) 
  ```
  - out_ast_full.vcps: Display abstract syntax tree as treelib view.
  ```
  <program>
  ├── <var-decl>
  │   ├── <type>
  │   │   └── int
  │   ├── <init-declarator-list>
  │   │   ├── <init-declarator>
  │   │   │   ├── <declarator>
  │   │   │   │   ├── <identifier>
  │   │   │   │   │   └── i
  │   │   │   │   └── <declarator-t>
  │   │   │   │       └── EPSILON
  │   │   │   └── <init-declarator-t>
  │   │   │       └── EPSILON
  │   │   └── <init-declarator-list-t>
  │   │       └── EPSILON
  │   └── ;
  ...
  ```
  - out_ast_reduced.vcps: Display abstract syntax tree with treelib view but reduce some node for easier view.
  ```
  <program>
  ├── <var-decl>
  │   ├── int
  │   ├── i
  │   └── ;
  ├── <var-decl>
  │   ├── int
  │   ├── j
  │   └── ;
  ├── <func-decl>
  │   ├── int
  │   ├── gcd
  │   ├── <para-list>
  │   │   ├── (
  │   │   ├── <proper-para-list>
  │   │   │   ├── <para-decl>
  │   │   │   │   ├── int
  │   │   │   │   └── a
  │   │   │   └── <proper-para-list-t>
  │   │   │       ├── ,
  │   │   │       └── <para-decl>
  │   │   │           ├── int
  │   │   │           └── b
  │   │   └── )
  ...
  ```
