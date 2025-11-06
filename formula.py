"""
This module contains the parse_formula function that converts
a chemical formula into a list of [symbol, quantity] pairs.

For example:
    parse_formula("C6H12O6") → [["C", 6], ["H", 12], ["O", 6]]

If the formula contains parentheses, such as "Mg(OH)2",
the function correctly multiplies the quantities within parentheses.
"""

class FormulaError(ValueError):
    """Custom error class for invalid chemical formulas."""
    pass


def parse_formula(formula):
    """Convert a chemical formula string into a compound list of [symbol, quantity] pairs."""
    import re

    def parse_recursive(formula, index):
        elements = []
        while index < len(formula):
            if formula[index] == '(':
                group, index = parse_recursive(formula, index + 1)
                mult_match = re.match(r"\d+", formula[index:])
                mult = int(mult_match.group()) if mult_match else 1
                index += len(mult_match.group()) if mult_match else 0
                for sym, qty in group:
                    elements.append([sym, qty * mult])
            elif formula[index] == ')':
                return elements, index + 1
            else:
                match = re.match(r"([A-Z][a-z]?)(\d*)", formula[index:])
                if not match:
                    raise FormulaError(f"Invalid symbol at index {index}")
                sym = match.group(1)
                qty = int(match.group(2)) if match.group(2) else 1
                elements.append([sym, qty])
                index += len(match.group(0))
        return elements, index

    parsed, end = parse_recursive(formula, 0)
    if end != len(formula):
        raise FormulaError("Extra data after valid formula")
    # Combine duplicates
    combined = {}
    for sym, qty in parsed:
        combined[sym] = combined.get(sym, 0) + qty
    return [[sym, combined[sym]] for sym in sorted(combined)]
