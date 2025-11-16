# Syntax Analyzer (Predictive Parser)

This project implements a top-down predictive parser for a given context-free grammar (CFG) using the provided predictive parsing table. It traces input strings over the alphabet {a, +, -, *, /, (, )} ending with $, determining if they are valid expressions (e.g., arithmetic with operator precedence).

## Grammar Overview
- Non-terminals: E (expression), Q (add/sub), T (term), R (mul/div), F (factor).
- Productions (after left-recursion removal): E → TQ | Q → +TQ | -TQ | ε | T → FR | R → *FR | /FR | ε | F → (E) | a.
- Parsing is LL(1) using the predictive table for expansions based on lookahead.

## Requirements
- Python 3.x.
- No external libraries needed.

## How to Run
1. Save the code as `prog1.py`.
2. Run in terminal: `python prog1.py`.
3. Enter an input string ending with `$` (e.g., `a+a$`).
4. Output: Stack flow after each step, plus "String is accepted/ valid." or "String is not accepted/ Invalid."

## Testing
Test with the required inputs (all should accept):
- `(a+a)*a$`
- `a*(a/a)$`
- `a(a+a)$`

Example output for `(a+a)$`:
