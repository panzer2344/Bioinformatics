

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
	specCpy = spectrum.copy()
	
	for amino in peptide:
		if amino in specCpy:
			specCpy.remove(amino)
		else:
			return False
	
	return True


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
	
	#0 97 97 99 101 103 196 198 198 200 202 295 297 299 299 301 394 396 398 400 400 497
	#0 71 97 99 101 101 113 114 129 131 163 186 202 202 211 227 228 230 230 234 260 287 299 301 324 329 331 331 359 365 374 388 400 413 430 430 445 460 462 464 487 501 510 514 517 531 558 561 561 576 593 611 615 616 630 632 673 675 689 690 694 712 729 744 744 747 774 788 791 795 804 818 841 843 845 860 875 875 892 905 917 931 940 946 974 974 976 981 1004 1006 1018 1045 1071 1075 1075 1077 1078 1094 1103 1103 1119 1142 1174 1176 1191 1192 1204 1204 1206 1208 1234 1305

if __name__ == "__main__":
	main()
	
	