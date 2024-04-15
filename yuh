import os
def atomfreq_from_file(filename):
    atom_counts = {}

    with open(filename, 'r') as file:
        for line in file:
            if line.startswith("ATOM"):
                element = line[76:78].strip()
                if element in atom_counts:
                    atom_counts[element] += 1
                else:
                    atom_counts[element] = 1

    for element, count in sorted(atom_counts.items(), key=lambda x: x[0]):
        print(f"{element}: {count}")

def main():
    pdbtool_path = os.getenv('PDBTOOL_PATH')
    if pdbtool_path:
        atomfreq_from_file(pdbtool_path)
    else:
        print("Error: Environment variable PDBTOOL_PATH is not set.")
        print("Please set the PDBTOOL_PATH environment variable to the path of pdbtool.pdb.")

if __name__ == "__main__":
    main()
