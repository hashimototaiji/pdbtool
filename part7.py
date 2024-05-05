# Part 7: Calculating frequency based on occupancy
def occupancy_frequency(atom_records, threshold):
    below_count = sum(1 for atom in atom_records if atom['occupancy'] < threshold)
    at_count = sum(1 for atom in atom_records if atom['occupancy'] == threshold)
    above_count = sum(1 for atom in atom_records if atom['occupancy'] > threshold)
    total_count = len(atom_records)
    return below_count, at_count, above_count, total_count

# Part 8: Quitting the program
elif command.lower() == 'quit':
    print("Quitting the program. Goodbye!")
    break
