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


def generate_next_peptide(_current_peptide, _replacedPos = -1):
	_peptide = _current_peptide
	replacedPos = len(_peptide) - 1
	
	if _replacedPos != -1:
		replacedPos = _replacedPos 
	
	if _peptide[replacedPos] == 'W':
		_peptide = _peptide[:replacedPos] + 'G' + _peptide[replacedPos + 1:]
		if replacedPos - 1 >= 0:
			_peptide = generate_next_peptide(_peptide, replacedPos - 1)
		else:
			return -1
	else:
		_peptide = _peptide[:replacedPos] + acids[acids.index(_peptide[replacedPos]) + 1] + _peptide[replacedPos + 1:]
	return _peptide
	
def calculate_mass(_current_peptide):
	mass = 0
	for pos in range(len(_current_peptide)):
		mass += SortedMasses.get(_current_peptide[pos])
	return mass

def main():
	for mass in Masses:
		print(mass, end=" ")
	print("\n" + str(acids_count))	
	
	for smass in SortedMasses:
		print(smass)
	print("\n")

	print("min_len = " + str(min_len))
	print("max_len = " + str(max_len))
	
	
	countEquilPeptides = 0
	for peptide_len in range(min_len, max_len + 1):
		print(peptide_len)
		current_peptide = 'G' * peptide_len
		if calculate_mass(current_peptide) == given:
			countequilpeptides += 1
		while True:
			current_peptide = generate_next_peptide(current_peptide)
			if current_peptide == -1:
				break
			else:
				if calculate_mass(current_peptide) == given:
					countequilpeptides += 1
					
	print(countEquilPeptides)
	
if __name__ == "__main__":
	main()