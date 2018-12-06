

masses = {
	'A' : 71, 'R' : 156, 'N' : 114, 'D' : 115, 'C' : 103, 'E' : 129, 'Q' : 128, 'G' : 57, 'H' : 137, 
	'I' : 113, 'L' : 113, 'K' : 128, 'M' : 131, 'F' : 147, 'P' : 97, 'S' : 87, 'T' : 101, 'W' : 186, 
	'Y' : 163, 'V' : 99 
}


masses_dict = sorted(set(masses.values()))



def add_mass(_subpeptide, _spMasses):
	spMass = 0
	for amin in _subpeptide:
		spMass += amin
	_spMasses += [spMass]


def cyclospectrum(peptide):	
	peptide_len = len(peptide)

	spMasses = [0]

	for i in range(1, peptide_len):
		for j in range(0, peptide_len):
			subpeptide = []
			
			tail = i if i <= peptide_len - j else peptide_len - j
			stump = i - tail
			
			subpeptide += peptide[j:j+tail]
			subpeptide += peptide[0:stump]
			
			add_mass(subpeptide, spMasses)
	spMasses.sort()
	add_mass(peptide, spMasses)
	
	return spMasses


def linear_spectrum(peptide):
	
	spMasses = [0]

	for i in range(1, len(peptide)):
		for j in range(0, len(peptide) - i + 1):
			add_mass(peptide[j:j+i], spMasses)
	spMasses.sort()
	add_mass(peptide, spMasses)

	return spMasses




def expand(peptides):
	
	result = []
	
	if not peptides:
			for mass in masses_dict:
				result.append( [mass] )
	else:
		for peptide in peptides:
			for mass in masses_dict:
				new_pep = peptide[:]
				new_pep.append(mass)
				result.append(new_pep)
	
	return result
	
	

def is_consistent(peptide, spectrum):

	pepSpec = linear_spectrum(peptide)
	
	specCpy = spectrum.copy()
	
	for amino in pepSpec:
		if amino in specCpy:
			specCpy.remove(amino)
		else:
			return False
	
	if mass(peptide) in spectrum:
		return True
	else:
		return False



def mass(peptide):
	result = 0
	
	for amino in peptide:
		result += amino
		
	return result


	
def parent_mass(spectrum):
	return spectrum[ len(spectrum) - 1 ]


	
def print_peptide(peptide):
	for i in range(len(peptide)):
		print(peptide[i], end = "-" if i < len(peptide) - 1 else " ")

	
	
def cyclopeptide_sequencing(spectrum):
	
	peptides = []
	peptides = expand(peptides)
	
	while peptides:	
		need_delete = []
		
		for peptide in peptides:
			if mass(peptide) == parent_mass(spectrum):
				if cyclospectrum(peptide) == spectrum:
					print_peptide(peptide)
									
				need_delete.append(peptide)

			elif not is_consistent(peptide, spectrum):
				need_delete.append(peptide)
						
		for nd in need_delete:
			peptides.remove(nd)
			
		if peptides:
			peptides = expand(peptides)
		

def main():
	spectrum = [int(elem) for elem in input().split()]
	cyclopeptide_sequencing(spectrum)
	

if __name__ == "__main__":
	main()
	
	
