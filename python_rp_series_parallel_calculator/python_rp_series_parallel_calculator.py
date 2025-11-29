#===================================================
# SERIES AND PARALLEL RESISTOR CALCULATOR
# ---------------------------------------------------
#
# This program calculates the total resistance of a set of resistors
# connected in series or in parallel, allowing flexible input of values
# and offering robust error handling.
#
# Program: python_rp_series_parallel_calculator.py
# Author : Juan Carlos with Natsuki assistance
# Date   : Nov 28, 2025
#===================================================

import sys # For sys.exit()

def display_welcome_message():
    """Displays a welcome message and a brief explanation of the tool."""
    print("=" * 60)
    print("SERIES AND PARALLEL RESISTOR CALCULATOR".center(60))
    print("=" * 60)
    print("\nWelcome. This tool calculates the total resistance of a set of resistors")
    print("connected in series or in parallel. Designed to facilitate electronics")
    print("calculations precisely and robustly.")
    print("\n")
    print("Visual example of connections:")
    print("--------------------------------------------------")
    print("  Series: ---[R1]---[R2]---[R3]---")
    print(" ")
    print("             +----[R1]----+")
    print("             |            |")
    print("  Parallel:  +----[R2]----+")
    print("             |            |")
    print("             +----[R3]----+")
    print("--------------------------------------------------")
    print("\n")

def get_number_of_resistors():
    """Prompts for and validates the number of resistors."""
    while True:
        try:
            num_resistors = int(input("How many resistors do you want to enter?: "))
            if num_resistors <= 0:
                print("Error: Please enter a positive number of resistors.")
            else:
                return num_resistors
        except ValueError:
            print("Error: Invalid input. Please enter an integer.")

def get_calculation_mode():
    """Prompts for and validates the calculation mode (series 's' or parallel 'p')."""
    while True:
        mode = input("Are the resistors in series (s) or parallel (p)?: ").lower()
        if mode in ['s', 'p']:
            return mode
        else:
            print("Error: Invalid input. Please enter 's' for series or 'p' for parallel.")

def parse_resistor_value(resistor_input_str):
    """
    Parses the resistor input string, handling suffixes like 'k' and 'M'.
    Returns the value in Ohms (float).
    """
    try:
        # Try to convert directly to float
        value = float(resistor_input_str)
    except ValueError:
        # If direct conversion fails, try with suffixes
        resistor_input_str = resistor_input_str.lower().strip()
        if resistor_input_str.endswith('k'):
            value = float(resistor_input_str[:-1]) * 1e3
        elif resistor_input_str.endswith('m'):
            value = float(resistor_input_str[:-1]) * 1e6
        else:
            raise ValueError("Invalid resistor format. Use Ohms, k (kilo) or M (mega).")
    return value


def get_resistor_value(resistor_index):
    """Prompts for and validates the value of a resistor."""
    while True:
        raw_input = input(f"Enter the value for resistor {resistor_index} in Ohms (e.g.: 100, 1k, 2.2M): ")
        try:
            value_ohms = parse_resistor_value(raw_input)
            if value_ohms <= 0:
                print("Error: The resistor value must be positive.")
            else:
                return value_ohms
        except ValueError as e:
            print(f"Error in value: {e}. Please try again.")

def calculate_series_resistance(resistor_values):
    """Calculates the total resistance in series."""
    return sum(resistor_values)

def calculate_parallel_resistance(resistor_values):
    """Calculates the total resistance in parallel."""
    sum_inverses = 0.0
    for r in resistor_values:
        if r == 0: # Avoid division by zero
            raise ValueError("Resistors in parallel cannot be zero for inverse calculation.")
        sum_inverses += 1 / r
    return 1 / sum_inverses

def format_total_resistance(total_resistance_ohms):
    """Formats the total resistance to the most appropriate unit (Ohms, kΩ, MΩ)."""
    if total_resistance_ohms >= 1e6:
        return f"{total_resistance_ohms / 1e6:.2f} MΩ"
    elif total_resistance_ohms >= 1e3:
        return f"{total_resistance_ohms / 1e3:.2f} kΩ"
    else:
        return f"{total_resistance_ohms:.2f} Ω"

def main():
    """Main function that orchestrates the program."""
    display_welcome_message()

    while True:
        num_resistors = get_number_of_resistors()
        calculation_mode = get_calculation_mode()

        resistor_values_ohms = []
        for i in range(1, num_resistors + 1):
            value = get_resistor_value(i)
            resistor_values_ohms.append(value)

        total_resistance = 0.0
        try:
            if calculation_mode == 's':
                total_resistance = calculate_series_resistance(resistor_values_ohms)
                print(f"\nCalculating {num_resistors} resistors in SERIES.")
            else: # calculation_mode == 'p'
                total_resistance = calculate_parallel_resistance(resistor_values_ohms)
                print(f"\nCalculating {num_resistors} resistors in PARALLEL.")

            print(f"Total Resistance = {format_total_resistance(total_resistance)}")
        except ValueError as e:
            print(f"Error in calculation: {e}. Please review the entered values.")


        continue_choice = input("\nDo you want to perform another calculation? (y/n): ").lower()
        if continue_choice != 'y':
            print("Thank you for using the calculator. See you soon!")
            sys.exit(0) # Exit the program

if __name__ == "__main__":
    main()
