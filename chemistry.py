# chemistry.py
# Molar mass calculator: computes molar mass from a chemical formula
# and the number of moles for a given sample mass.
# Exceeds requirements: known-molecule name lookup and total proton count.

# Imports the parser and its error type for chemical formulas.
from formula import parse_formula, FormulaError


# ------------------------------------------------
# Constant Section
# ------------------------------------------------

# Index position for the element name in the periodic table's inner list.
NAME_INDEX = 0

# Index position for the atomic mass (grams/mole) in the periodic table's inner list.
ATOMIC_MASS_INDEX = 1

# Index position for the atomic number (proton count) in the periodic table's inner list.
ATOMIC_NUMBER_INDEX = 2

# Index position for symbol in a [symbol, quantity] pair returned by parse_formula.
SYMBOL_INDEX = 0

# Index position for quantity in a [symbol, quantity] pair returned by parse_formula.
QUANTITY_INDEX = 1


# ----------------------------------------------------
# Periodic Table
# ----------------------------------------------------
# Returns a dictionary mapping each element symbol to:
#   [element name, atomic mass (g/mol), atomic number]
def make_periodic_table():
    """
    Return the periodic table as {symbol: [name, atomic_mass, atomic_number]}.
    Atomic masses are standard values appropriate for general chemistry work.
    """
    periodic_table_dict = {
        # 1–10
        "H":  ["Hydrogen",        1.00794,     1],
        "He": ["Helium",          4.002602,    2],
        "Li": ["Lithium",         6.941,       3],
        "Be": ["Beryllium",       9.012182,    4],
        "B":  ["Boron",          10.811,       5],
        "C":  ["Carbon",         12.0107,      6],
        "N":  ["Nitrogen",       14.0067,      7],
        "O":  ["Oxygen",         15.9994,      8],
        "F":  ["Fluorine",       18.9984032,   9],
        "Ne": ["Neon",           20.1797,     10],

        # 11–20
        "Na": ["Sodium",         22.98976928, 11],
        "Mg": ["Magnesium",      24.305,      12],
        "Al": ["Aluminum",       26.9815386,  13],
        "Si": ["Silicon",        28.0855,     14],
        "P":  ["Phosphorus",     30.973762,   15],
        "S":  ["Sulfur",         32.065,      16],
        "Cl": ["Chlorine",       35.453,      17],
        "Ar": ["Argon",          39.948,      18],
        "K":  ["Potassium",      39.0983,     19],
        "Ca": ["Calcium",        40.078,      20],

        # 21–30
        "Sc": ["Scandium",       44.955912,   21],
        "Ti": ["Titanium",       47.867,      22],
        "V":  ["Vanadium",       50.9415,     23],
        "Cr": ["Chromium",       51.9961,     24],
        "Mn": ["Manganese",      54.938045,   25],
        "Fe": ["Iron",           55.845,      26],
        "Co": ["Cobalt",         58.933195,   27],
        "Ni": ["Nickel",         58.6934,     28],
        "Cu": ["Copper",         63.546,      29],
        "Zn": ["Zinc",           65.409,      30],

        # 31–36
        "Ga": ["Gallium",        69.723,      31],
        "Ge": ["Germanium",      72.64,       32],
        "As": ["Arsenic",        74.9216,     33],
        "Se": ["Selenium",       78.96,       34],
        "Br": ["Bromine",        79.904,      35],
        "Kr": ["Krypton",        83.798,      36],

        # 37–46
        "Rb": ["Rubidium",       85.4678,     37],
        "Sr": ["Strontium",      87.62,       38],
        "Y":  ["Yttrium",        88.90585,    39],
        "Zr": ["Zirconium",      91.224,      40],
        "Nb": ["Niobium",        92.90638,    41],
        "Mo": ["Molybdenum",     95.96,       42],
        "Tc": ["Technetium",     98,          43],
        "Ru": ["Ruthenium",     101.07,       44],
        "Rh": ["Rhodium",       102.9055,     45],
        "Pd": ["Palladium",     106.42,       46],

        # 47–56
        "Ag": ["Silver",        107.8682,     47],
        "Cd": ["Cadmium",       112.411,      48],
        "In": ["Indium",        114.818,      49],
        "Sn": ["Tin",           118.71,       50],
        "Sb": ["Antimony",      121.76,       51],
        "Te": ["Tellurium",     127.6,        52],
        "I":  ["Iodine",        126.90447,    53],
        "Xe": ["Xenon",         131.293,      54],
        "Cs": ["Cesium",        132.9054519,  55],
        "Ba": ["Barium",        137.327,      56],

        # Lanthanides 57–71
        "La": ["Lanthanum",     138.90547,    57],
        "Ce": ["Cerium",        140.116,      58],
        "Pr": ["Praseodymium",  140.90765,    59],
        "Nd": ["Neodymium",     144.242,      60],
        "Pm": ["Promethium",    145,          61],
        "Sm": ["Samarium",      150.36,       62],
        "Eu": ["Europium",      151.964,      63],
        "Gd": ["Gadolinium",    157.25,       64],
        "Tb": ["Terbium",       158.92535,    65],
        "Dy": ["Dysprosium",    162.5,        66],
        "Ho": ["Holmium",       164.93032,    67],
        "Er": ["Erbium",        167.259,      68],
        "Tm": ["Thulium",       168.93421,    69],
        "Yb": ["Ytterbium",     173.04,       70],
        "Lu": ["Lutetium",      174.967,      71],

        # 72–80
        "Hf": ["Hafnium",       178.49,       72],
        "Ta": ["Tantalum",      180.94788,    73],
        "W":  ["Tungsten",      183.84,       74],
        "Re": ["Rhenium",       186.207,      75],
        "Os": ["Osmium",        190.23,       76],
        "Ir": ["Iridium",       192.217,      77],
        "Pt": ["Platinum",      195.084,      78],
        "Au": ["Gold",          196.966569,   79],
        "Hg": ["Mercury",       200.59,       80],

        # 81–86
        "Tl": ["Thallium",      204.3833,     81],
        "Pb": ["Lead",          207.2,        82],
        "Bi": ["Bismuth",       208.9804,     83],
        "Po": ["Polonium",      209,          84],
        "At": ["Astatine",      210,          85],
        "Rn": ["Radon",         222,          86],

        # 87–88
        "Fr": ["Francium",      223,          87],
        "Ra": ["Radium",        226,          88],

        # Actinides 89–103
        "Ac": ["Actinium",      227,          89],
        "Th": ["Thorium",       232.03806,    90],
        "Pa": ["Protactinium",  231.03588,    91],
        "U":  ["Uranium",       238.02891,    92],
        "Np": ["Neptunium",     237,          93],
        "Pu": ["Plutonium",     244,          94],
        "Am": ["Americium",     243,          95],
        "Cm": ["Curium",        247,          96],
        "Bk": ["Berkelium",     247,          97],
        "Cf": ["Californium",   251,          98],
        "Es": ["Einsteinium",   252,          99],
        "Fm": ["Fermium",       257,         100],
        "Md": ["Mendelevium",   258,         101],
        "No": ["Nobelium",      259,         102],
        "Lr": ["Lawrencium",    262,         103],

        # 104–118
        "Rf": ["Rutherfordium", 267,         104],
        "Db": ["Dubnium",       270,         105],
        "Sg": ["Seaborgium",    271,         106],
        "Bh": ["Bohrium",       270,         107],
        "Hs": ["Hassium",       277,         108],
        "Mt": ["Meitnerium",    276,         109],
        "Ds": ["Darmstadtium",  281,         110],
        "Rg": ["Roentgenium",   280,         111],
        "Cn": ["Copernicium",   285,         112],
        "Nh": ["Nihonium",      286,         113],
        "Fl": ["Flerovium",     289,         114],
        "Mc": ["Moscovium",     289,         115],
        "Lv": ["Livermorium",   293,         116],
        "Ts": ["Tennessine",    294,         117],
        "Og": ["Oganesson",     294,         118],
    }
    return periodic_table_dict


# ------------------------------------------------------
# Molar Mass Computation
# ------------------------------------------------------
# Computes and returns the total molar mass for a parsed chemical formula.
def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """
    Compute and return the total molar mass for a parsed chemical formula.

    Parameters:
        symbol_quantity_list: list of [symbol, quantity] pairs from parse_formula
        periodic_table_dict: dict mapping symbols to [name, atomic_mass, atomic_number]
    Returns:
        Float total molar mass in grams per mole
    """
    # Initializes the running total for molar mass.
    total_mass = 0.0

    # Iterates through each [symbol, quantity] pair.
    for element in symbol_quantity_list:
        # Extracts the chemical symbol and atom count.
        symbol = element[SYMBOL_INDEX]
        quantity = element[QUANTITY_INDEX]

        # Looks up [name, atomic_mass, atomic_number] for this symbol.
        element_data = periodic_table_dict[symbol]
        atomic_mass = element_data[ATOMIC_MASS_INDEX]

        # Accumulates this element’s mass contribution.
        total_mass += atomic_mass * quantity

    # Returns total molar mass (grams per mole).
    return total_mass


# ------------------------------------------------------
# Proton Count (Exceeds Requirements)
# ------------------------------------------------------
# Computes and returns the total number of protons in the molecule.
def sum_protons(symbol_quantity_list, periodic_table_dict):
    """
    Compute and return the total number of protons across the molecule.

    Parameters:
        symbol_quantity_list: list of [symbol, quantity] pairs from parse_formula
        periodic_table_dict: dict mapping symbols to [name, atomic_mass, atomic_number]
    Returns:
        Integer total proton count
    """
    # Initializes the proton counter.
    total = 0

    # Iterates through each [symbol, quantity] pair.
    for symbol, qty in symbol_quantity_list:
        # Retrieves the atomic number (protons) for the element.
        Z = periodic_table_dict[symbol][ATOMIC_NUMBER_INDEX]

        # Adds protons for all atoms of this element.
        total += Z * qty

    # Returns the molecule's total proton count.
    return total


# ------------------------------------------------------
# Known Molecules (Exceeds Requirements)
# ------------------------------------------------------
# Returns a dictionary mapping formulas to human-readable names.
def get_known_molecules():
    """
    Return {formula_string: human_readable_name}.
    """
    return {
        "Al(OH)3": "aluminum hydroxide",
        "Al2O3": "aluminum oxide",
        "CH3OH": "methanol",
        "C2H6O": "ethanol",
        "C2H5OH": "ethanol",
        "C3H8O": "isopropyl alcohol",
        "C3H8": "propane",
        "C4H10": "butane",
        "C6H6": "benzene",
        "C6H14": "hexane",
        "C8H18": "octane",
        "CH3(CH2)6CH3": "octane",
        "C13H18O2": "ibuprofen",
        "C13H16N2O2": "melatonin",
        "Fe2O3": "iron(III) oxide",
        "FeS2": "iron pyrite",
        "H2O": "water",
        "Mg(C2H3O2)2": "magnesium acetate",
        "NaCl": "sodium chloride",
        "NH3": "ammonia",
        "H2SO4": "sulfuric acid",
        "HNO3": "nitric acid",
        "CO2": "carbon dioxide",
        "NaHCO3": "sodium bicarbonate",
    }


# Looks up and returns a name for a formula if known; otherwise returns "unknown compound".
def get_formula_name(formula, known_molecules_dict):
    """
    Return the human-readable name for the formula if present; otherwise 'unknown compound'.
    """
    return known_molecules_dict.get(formula, "unknown compound")


# -------------------------------------------------------
# Program Entry
# -------------------------------------------------------
# Coordinates user input, parsing, computation, and output.
def main():
    """
    Orchestrates user input, parsing, computation, and output for the calculator.
    """
    try:
        # Reads the chemical formula string from standard input.
        formula = input("Enter the molecular formula of the sample: ").strip()

        # Reads the sample mass in grams and converts to float.
        mass_str = input("Enter the mass in grams of the sample: ").strip()
        sample_mass = float(mass_str)

        # Builds the periodic table dictionary.
        periodic_table_dict = make_periodic_table()

        # Parses the formula into a list of [symbol, quantity] pairs.
        symbol_quantity_list = parse_formula(formula)

        # Computes the molar mass (grams per mole).
        molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table_dict)

        # Computes the number of moles (sample_mass / molar_mass).
        number_of_moles = sample_mass / molar_mass

        # Loads known molecules and resolves a human-readable name if available.
        known_molecules_dict = get_known_molecules()
        compound_name = get_formula_name(formula, known_molecules_dict)

        # Computes total number of protons across the molecule.
        total_protons = sum_protons(symbol_quantity_list, periodic_table_dict)

        # Outputs required results with the specified formatting.
        print(f"{molar_mass:.5f} grams/mole")
        print(f"{number_of_moles:.5f} moles")

        # Outputs exceed-requirements results.
        print(f"Name: {compound_name}")
        print(f"Total protons: {total_protons}")

    except FormulaError as ex:
        # Reports invalid formula syntax caught by parse_formula.
        print(f"Error: invalid formula ({ex})")

    except ValueError:
        # Reports a non-numeric mass input or numeric conversion failure.
        print("Error: mass must be a valid number.")

    except KeyError as ex:
        # Reports an element symbol not present in the periodic table dictionary.
        missing = str(ex).strip("'")
        print(f"Error: unknown element symbol in formula: {missing}")


# Executes main() only when this file is run directly.
if __name__ == "__main__":
    main()
