#Prologue (indented comments)
  #Title: pdbtool
  #Authors: Adnan Prantoi, Iman Meawad, Taiji Hashimoto, Jayden Leung
  #Roles: J.L. (Parts 1 and 2), I.M. (Parts 3 and 4), T.H. (Parts 5 and 6), A.P. (parts 7 and 8)
  #Date of Creation: 03/29/24
  #Usage (command-usage): Commands 'help', 'atomfreq', 'resfreq', and 'quit' can be typed as they are
    #reslength <res_name> <chain_id> <res_seq_number>
    #tempcheck <decimal>
    #occupancy <decimal>
  #Accepted Input (files): Only files containing the word 'ATOM' in the first index are accepted, since that's how the file is read when looking for specific information
  #Command Descriptions (Input-Output): 
    #help-list all valid commands including itself
    #atomfreq-number of atoms for each element (Ex: C: 3201)
    #resfreq-displays the number of each residue in the file (Ex: ARG: 306)
    #reslength-displaysthe length of a residue if chain id and sequence number is given
    #tempcheck-displaysthe number of atoms that have a temperature factor at, above, or below a given value in terms of a fraction and percent
    #occupancy-displays the frequency of atoms at, above, or below a given value (factor)
    #quit-outputs a departing message (goodbye) then program ends
import sys
import math

def read_pdb(file_path):
    """
    Reads a PDB file and returns a list of atoms with their detailed properties.
    Each atom's properties include element type, residue name, chain ID, sequence number,
    coordinates (x, y, z), temperature factor, and occupancy.
    """
    atoms = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith("ATOM"):
                    parts = line.split()
                    atom = {
                        'element': parts[11].strip(),
                        'residue_name': parts[3].strip(),
                        'chain_id': parts[4].strip(),
                        'res_seq_num': int(parts[5]),
                        'x': float(parts[6]),
                        'y': float(parts[7]),
                        'z': float(parts[8]),
                        'temp_factor': float(parts[10]),
                        'occupancy': float(parts[9])
                    }
                    atoms.append(atom)
        return atoms
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' not found.")
        sys.exit(1)

def atom_frequencies(atoms):
    """
    Displays the frequency of each atom type sorted alphabetically.
    This function helps in understanding the composition of the molecule.
    """
    freq = {}
    for atom in atoms:
        element = atom['element']
        freq[element] = freq.get(element, 0) + 1
    for element in sorted(freq):
        print(f"{element}: {freq[element]}")

def residue_frequencies(atoms):
    """
    Displays the frequency of each residue type sorted alphabetically.
    Useful for understanding the composition of residues in the protein structure.
    """
    freq = {}
    for atom in atoms:
        residue = atom['residue_name']
        freq[residue] = freq.get(residue, 0) + 1
    for residue in sorted(freq):
        print(f"{residue}: {freq[residue]}")

def max_distance(atoms, res_name, chain_id, res_seq_num):
    """
    Calculates and returns the maximum distance between any two atoms within a specified residue.
    If the specified residue does not exist, returns None.
    """
    relevant_atoms = [atom for atom in atoms if atom['residue_name'] == res_name and atom['chain_id'] == chain_id and atom['res_seq_num'] == res_seq_num]
    if not relevant_atoms:
        return None
    max_dist = 0
    for i in range(len(relevant_atoms)):
        for j in range(i + 1, len(relevant_atoms)):
            atom1, atom2 = relevant_atoms[i], relevant_atoms[j]
            dist = math.sqrt((atom1['x'] - atom2['x'])**2 + (atom1['y'] - atom2['y'])**2 + (atom1['z'] - atom2['z'])**2)
            max_dist = max(max_dist, dist)
    return max_dist

def temperature_check(atoms, threshold):
    """
    Displays statistics of temperature factors below, at, and above a given threshold.
    Temperature factors indicate the degree of atomic motion due to thermal vibration.
    """
    below = sum(1 for atom in atoms if atom['temp_factor'] < threshold)
    at = sum(1 for atom in atoms if atom['temp_factor'] == threshold)
    above = sum(1 for atom in atoms if atom['temp_factor'] > threshold)
    total = len(atoms)
    print(f"Temperature factor below {threshold:.2f}: {below} / {total} ({below / total * 100:.1f}%)")
    print(f"Temperature factor at {threshold:.2f}: {at} / {total} ({at / total * 100:.1f}%)")
    print(f"Temperature factor above {threshold:.2f}: {above} / {total} ({above / total * 100:.1f}%)")

def occupancy_frequency(atoms, threshold):
    """
    Displays statistics of atom occupancy below, at, and above a given threshold.
    Occupancy values indicate the proportion of time an atom is present in a particular position in the structure.
    """
    below = sum(1 for atom in atoms if atom['occupancy'] < threshold)
    at = sum(1 for atom in atoms if atom['occupancy'] == threshold)
    above = sum(1 for atom in atoms if atom['occupancy'] > threshold)
    total = len(atoms)
    print(f"Occupancy below {threshold:.2f}: {below} / {total} ({below / total * 100:.1f}%)")
    print(f"Occupancy at {threshold:.2f}: {at} / {total} ({at / total * 100:.1f}%)")
    print(f"Occupancy above {threshold:.2f}: {above} / {total} ({above / total * 100:.1f}%)")

def main():
    """
    Main function that initializes the program, loads the PDB file, and handles user commands in a loop.
    Commands include atom and residue frequency analysis, residue length measurement, temperature and occupancy checks, and exiting the program.
    """
    if len(sys.argv) != 2:
        print("Usage: python pdbtool.py <pdb_file>")
        sys.exit(1)
    
    pdb_file = sys.argv[1]
    atoms = read_pdb(pdb_file)
    
    print("Welcome to the pdb program.")
    print("To begin, try typing 'help' for the list of valid commands.")
    print(f"{len(atoms)} atoms recorded.\n")

    while True:
        command = input("Enter a command: ").split()
        if not command:
            continue
        cmd = command[0]
        if cmd == "quit":
            print("Goodbye!")
            break
        elif cmd == "help":
            print("Available commands:")
            print("  help        - Show this help message")
            print("  atomfreq    - Display frequency of each atom type")
            print("  resfreq     - Display frequency of each residue")
            print("  reslength   - Calculate the length of a specified residue")
            print("  tempcheck   - Display temperature factor statistics")
            print("  occupancy   - Display occupancy statistics")
            print("  quit        - Exit the program")
        elif cmd == "atomfreq":
            atom_frequencies(atoms)
        elif cmd == "resfreq":
            residue_frequencies(atoms)
        elif cmd == "reslength" and len(command) == 4:
            res_name, chain_id, res_seq_num = command[1], command[2], int(command[3])
            dist = max_distance(atoms, res_name, chain_id, res_seq_num)
            if dist is not None:
                print(f"{res_name} with sequence number {res_seq_num} in chain {chain_id} has length {dist:.2f} angstroms.")
            else:
                print("No residue present.")
        elif cmd == "tempcheck" and len(command) == 2:
            threshold = float(command[1])
            temperature_check(atoms, threshold)
        elif cmd == "occupancy" and len(command) == 2:
            threshold = float(command[1])
            occupancy_frequency(atoms, threshold)
        else:
            print("Invalid command or incorrect number of arguments. Type 'help' for assistance.")

if __name__ == "__main__":
    main()
