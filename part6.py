import sys

def read_pdb_file(filename):
    # This function reads the PDB file and extracts temperature factors.
    atoms = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith("ATOM") or line.startswith("HETATM"):
                    temp_factor = float(line[60:66].strip())  # Assuming temp factor is in this column
                    atoms.append(temp_factor)
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        sys.exit(1)
    return atoms

def tempcheck(temp_factors, threshold):
    below = len([t for t in temp_factors if t < threshold])
    at = len([t for t in temp_factors if t == threshold])
    above = len([t for t in temp_factors if t > threshold])
    total = len(temp_factors)
    print(f"Temperature factor below {threshold:.2f}: {below} / {total} ({below/total*100:.1f}%)")
    print(f"Temperature factor at {threshold:.2f}: {at} / {total} ({at/total*100:.1f}%)")
    print(f"Temperature factor above {threshold:.2f}: {above} / {total} ({above/total*100:.1f}%)")

def main():
    if len(sys.argv) != 2:
        print("Usage: pdbtool.py <pdb_file>")
        sys.exit(1)

    filename = sys.argv[1]
    atoms = read_pdb_file(filename)
    print(f"Welcome to the pdb program.\nTo begin, try typing 'help' for the list of valid commands.\n{len(atoms)} atoms recorded.")

    while True:
        try:
            command = input("Enter a command: ").strip().split()
            if command[0] == 'tempcheck':
                if len(command) == 2:
                    try:
                        decimal = float(command[1])
                        if 0.00 <= decimal <= 100.00:
                            tempcheck(atoms, decimal)
                        else:
                            raise ValueError
                    except ValueError:
                        print("Usage: tempcheck <decimal>\nFor details about the tempcheck command, use the 'help' command.")
                else:
                    print("Incorrect number of arguments to tempcheck" if len(command) > 2 else "Missing argument to tempcheck")
            else:
                print(f"Unknown command: {command[0]}")
        except KeyboardInterrupt:
            print("\nExiting the program.")
            break

if __name__ == "__main__":
    main()
