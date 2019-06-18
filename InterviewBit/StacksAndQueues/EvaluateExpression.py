"""
Evaluate Expression
===================
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Examples:

["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

from __future__ import print_function
import operator


OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


def eval_rpn(seq):
    st = []
    for tok in seq:
        if tok in '+-*/':
            b, a = st.pop(), st.pop()
            st.append(OPS[tok](a, b))
        else:
            st.append(int(tok))
    return st.pop()


for seq in (
    ["2", "1", "+", "3", "*"],
    ["4", "13", "5", "/", "+"]
):
    print(seq, eval_rpn(seq))
