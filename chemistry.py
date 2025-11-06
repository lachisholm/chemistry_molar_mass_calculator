# chemistry.py
# Module file for the molar mass calculator assignment
#This program calculates the molar mass of a chemical compound
# and determines the number of moles in a given sample mass.

# Imports the parse_formula function from formula.py for chemical formulat parsing
from formula import parse_formula

#------------------------------------------------
#    Constant Section
#------------------------------------------------

# Defines the index position for the element name in the periodic table's inner list
NAME_INDEX = 0

# Defines the index position for the atomic mass in the periodic table's inner list
SYMBOL_INDEX = 1

#----------------------------------------------------
# Function: make_periodic_table
#----------------------------------------------------

#------------------------------------------------------
# Function: make_periodic_table
#-------------------------------------------------------
#Returns the periodic table as a dictionary
def make_periodic_table():
    """
    Return the periodic table as a dictionary mapping symbols to [name, atomic_mass].
    """
    # Initializes the periodic table with the minimal set of elements
    # required for the assignment’s sample inputs and initial tests.
    # Elements included for now:
    #   H  (Hydrogen)         1.00794
    #   C  (Carbon)          12.0107
    #   O  (Oxygen)          15.9994
    #   Al (Aluminum)        26.9815386
    #   Mg (Magnesium)       24.305
    periodic_table_dict = {
        # symbol: [name, atomic_mass]
        "H":  ["Hydrogen", 1.00794],
        "C":  ["Carbon",   12.0107],
        "O":  ["Oxygen",   15.9994],
        "Al": ["Aluminum", 26.9815386],
        "Mg": ["Magnesium", 24.305],
    }

    # Returns the periodic table dictionary used for mass lookups.
    return periodic_table_dict

        
        #------------------------------------------------------
        # Function: compute-molar-mass
        #-------------------------------------------------------
        
        # Computes and returns the total moar mass for a parsed chemical formula
        #The molar mass is the sum of the atomic masses of all atoms in the formula
        # This function will use the periodic table dictionary for mass lookups
       # Initializes the running total for molar mass.
    total_mass = 0.0

    # Iterates through each [symbol, quantity] pair returned from parse_formula().
    for element in symbol_quantity_list:

        # Extracts the symbol (e.g., "H") and quantity (e.g., 2) from the list.
        symbol = element[SYMBOL_INDEX]
        quantity = element[QUANTITY_INDEX]

        # Retrieves the corresponding [name, atomic_mass] list from the periodic table.
        element_data = periodic_table_dict[symbol]

        # Extracts the atomic mass value from the element_data list.
        atomic_mass = element_data[ATOMIC_MASS_INDEX]

        # Calculates the contribution of this element to the molecule’s total molar mass.
        element_mass = atomic_mass * quantity

        # Adds this element’s mass contribution to the running total.
        total_mass += element_mass

    # Returns the complete molar mass for the compound (grams per mole).
    return total_mass


            
            #-------------------------------------------------------
            # Function: main
            #-------------------------------------------------------
            # Serves as the entry point of the program
            # This function will coordinate user input, parsing, computation, and output.
            # The program flow will be as follows:
            # 1. Prompt the user for a molecular formula and sample mass
            # 2. Build the periodic table vai make_periodic_table()
            # 3. Parse the molecular formula using parse_formula()
            # 4. Compute the molar mass using compute_molar_mass()
            # 5. Calculate the number of moles by dividing sample mass by molar mass.
            # 6. Display both the molar mass and number of moles
            
def main():
        """
        Orchestrates user input, parsing, computation, and output for the calculator.
        """
        # Prompts the user for a molecular formula string (e.g., "C6H6" or "Al(OH)3").
        formula = input("Enter the molecular formula of the sample: ").strip()

        # Prompts the user for the sample mass in grams and converts it to float.
        # Raises ValueError if the input cannot be converted.
        mass_str = input("Enter the mass in grams of the sample: ").strip()
        sample_mass = float(mass_str)

        # Builds the periodic table dictionary used for atomic mass lookups.
        periodic_table_dict = make_periodic_table()

        # Parses the formula into a list of [symbol, quantity] pairs using parse_formula().
        # Raises FormulaError if the formula is syntactically invalid.
        symbol_quantity_list = parse_formula(formula)

        # Computes the molar mass (grams per mole) for the parsed compound.
        molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table_dict)

        # Computes the number of moles in the sample (sample_mass divided by molar_mass).
        number_of_moles = sample_mass / molar_mass

        # Prints the molar mass with five digits after the decimal point to match examples.
        print(f"{molar_mass:.5f} grams/mole")

        # Prints the number of moles with five digits after the decimal point to match examples.
        print(f"{number_of_moles:.5f} moles")

                
                # --------------------------------------------------------
                # Program Entry Point
                # --------------------------------------------------------
                # Executes main() only when this file is run directly,
                #not when it is imported as a module
if __name__=="__main__":
                    main()