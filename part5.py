import sys
import math

# Function to calculate Euclidean distance between two 3D points
def calculate_distance(atom1, atom2):
    x1, y1, z1 = atom1
    x2, y2, z2 = atom2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

# Function to read PDB file and extract atom coordinates
def read_pdb_file(file_name):
    atom_coordinates = {}
    with open(file_name, 'r') as pdb_file:
        for line in pdb_file:
            if line.startswith('ATOM'):
                atom_name = line[12:16].strip()
                x = float(line[30:38])
                y = float(line[38:46])
                z = float(line[46:54])
                chain_id = line[21]
                residue_seq_num = int(line[22:26])
                if (atom_name, chain_id, residue_seq_num) not in atom_coordinates:
                    atom_coordinates[(atom_name, chain_id, residue_seq_num)] = []
                atom_coordinates[(atom_name, chain_id, residue_seq_num)].append((x, y, z))
    return atom_coordinates

# Function to calculate maximum distance within a residue
def calculate_residue_length(pdb_file, res_name, chain_id, res_seq_num):
    atom_coordinates = read_pdb_file(pdb_file)
    if (res_name, chain_id, res_seq_num) not in atom_coordinates:
        print("No residue present.")
        return
    atoms = atom_coordinates[(res_name, chain_id, res_seq_num)]
    max_distance = 0
    for i in range(len(atoms)):
        for j in range(i+1, len(atoms)):
            distance = calculate_distance(atoms[i], atoms[j])
            if distance > max_distance:
                max_distance = distance
    print(f"{res_name} with sequence number {res_seq_num} in chain {chain_id} has length {max_distance:.2f} angstroms.")

# Main function to handle user input
def main():
    if len(sys.argv) != 4:
        print("Usage: pdbtool.py <pdb_file>")
        sys.exit(1)
    
    pdb_file = sys.argv[1]
    print("Welcome to the pdb program.")
    print("To begin, try typing 'help' for the list of valid commands.")
    
    while True:
        command = input("Enter a command: ").split()
        if not command:
            continue
        if command[0] == 'reslength':
            if len(command) != 4:
                print("Usage: reslength <res_name> <chain_id> <res_seq_num>")
                print("For details about the reslength command, use the 'help' command.")
                continue
            res_name = command[1].upper()
            chain_id = command[2].upper()
            try:
                res_seq_num = int(command[3])
            except ValueError:
                print("Usage: reslength <res_name> <chain_id> <res_seq_num>")
                print("For details about the reslength command, use the 'help' command.")
                continue
            calculate_residue_length(pdb_file, res_name, chain_id, res_seq_num)
        elif command[0] == 'help':
            print("This program calculates the maximum distance between atoms within a specified residue.")
            print("Usage: reslength <res_name> <chain_id> <res_seq_num>")
        else:
            print("Invalid command. Type 'help' for assistance.")

if __name__ == "__main__":
    main()
