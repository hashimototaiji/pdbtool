def atomfreq_from_file(6lu7.pdb):
    atom_counts = {} 
    with open('6lu7.pdb', 'r') as file:
        for line in file:
            atoms_in_line = line.strip().split()
            for atom in atoms_in_line:
                if atom in atom_counts:
                    atom_counts[atom] += 1
                else:
                    atom_counts[atom] = 1

    for element, count in sorted(atom_counts.items()):
        print(f"{element}: {count}")
with open("6lu7.pdb", "r") as file:                        
 residue_counts = {}             
for line in file:
        if line.startswith("ATOM"):
residue_name = line[17:20].strip().upper()
            residue_counts[residue_name] = residue_counts.get(residue_name, 0) + 1
for residue, count in sorted(residue_counts.items()):
    print(f"{residue}: {count}")
