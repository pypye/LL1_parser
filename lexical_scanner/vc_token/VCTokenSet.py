IDENTIFIER="((character|exponent)((character|exponent)|digit)*"
KEYWORD="keyword"
ARITHMETIC="arithmetic_1|arithmetic_2"
RELATIONAL="relational"
LOGICAL="logical"
EQUALITY="equality"
ASSIGNMENT="assignment"
SEPARATOR="separator"
INTLITERAL="digit(digit)*"

__FRACTION__ = "(dot)(digit)+"
__EXPONENT__ = "(exponent)(arithmetic_1)?(digit)+"
FLOATLITERAL=f"((digit)*({__FRACTION__})({__EXPONENT__})?)" \
             f"|((digit)+(dot))"\
             f"|((digit)+(dot)?({__EXPONENT__}))"

BOOLEANLITERAL="boolean"
STRINGLITERAL=f"(double_quote)(character|exponent|digit|space|separator|arithmetic_1|arithmetic_2|relational|logical|equality|assignment|separator|dot|other)*(double_quote)"

SPACE="space(space)*"
EOF="eof"