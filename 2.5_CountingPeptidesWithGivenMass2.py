Masses = {
	'A' : 71, 'R' : 156, 'N' : 114, 'D' : 115, 'C' : 103, 'E' : 129, 'Q' : 128, 'G' : 57, 'H' : 137, 
	'I' : 113, 'L' : 113, 'K' : 128, 'M' : 131, 'F' : 147, 'P' : 97, 'S' : 87, 'T' : 101, 'W' : 186, 
	'Y' : 163, 'V' : 99 
}

#acids = ['A','R','N','D','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V']
acids = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'L', 'N', 'D', 'K', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
acids_count = len(acids)

SortedMasses = dict( (key, value) for (value, key) in sorted((value, key) for (key, value) in Masses.items()))

#given = int(input())
given = 1024
max_len = int(given / 57.0)
min_len = int(given / 186.0)

def calculate_mass(_current_peptide):
	mass = 0
	for pos in range(len(_current_peptide)):
		mass += SortedMasses.get(_current_peptide[pos])
	return mass
	
