

masses = {
	'A' : 71, 'R' : 156, 'N' : 114, 'D' : 115, 'C' : 103, 'E' : 129, 'Q' : 128, 'G' : 57, 'H' : 137, 
	'I' : 113, 'L' : 113, 'K' : 128, 'M' : 131, 'F' : 147, 'P' : 97, 'S' : 87, 'T' : 101, 'W' : 186, 
	'Y' : 163, 'V' : 99 
}

#masses_dict = sorted(masses.values())
masses_dict = sorted(set(masses.values()))

#massesForCS = dict((v,k) for k,v in masses.items())


def add_mass(_subpeptide, _spMasses):
	spMass = 0
	for amin in _subpeptide:
		spMass += amin
		#print(amin)
		#spMass += masses.get(amin)
	_spMasses += [spMass]


def cyclospectrum(peptide):	
	peptide_len = len(peptide)

	spMasses = [0]

	for i in range(1, peptide_len):
		for j in range(0, peptide_len):
			#subpeptide = ""
			
			subpeptide = []
			
			tail = i if i <= peptide_len - j else peptide_len - j
			stump = i - tail
			
			#subpeptide += peptide[j:j+tail]
			#subpeptide += peptide[0:stump]
			
			subpeptide += peptide[j:j+tail]
			subpeptide += peptide[0:stump]
			
			add_mass(subpeptide, spMasses)
	spMasses.sort()
	add_mass(peptide, spMasses)
	
	return spMasses



def expand(peptides):

	#print("hi")

	#if [0] in peptides:
	#	del peptides[0]
	
	#peptides.remove[0]
	
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
				#print(new_pep)
	
	return result
	#return result
			

#def cyclospectrum(peptide):
	#spectrum = []
	#for amino in peptide:
		

def is_consistent(peptide, spectrum):
	
	#pepSpec = cyclospectrum(peptide)
	
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
	#print(peptides)
	
	while peptides:
		
		need_delete = []
		
		for peptide in peptides:
			
			#print("peptide = ", peptide, " pep_mass = ", mass(peptide), " parent_mass = ", parent_mass(spectrum))
		
			if mass(peptide) == parent_mass(spectrum):
				#print()
				#print(cyclospectrum(peptide))
				#print(spectrum)
				#print()
				if cyclospectrum(peptide) == spectrum:
					#print(peptide)
					print_peptide(peptide)
					#print(peptide)
				#peptides.remove(peptide)
				#print("mass of peptide ", peptide, "equal to spectrum parent_mass")
				need_delete.append(peptide)

			elif not is_consistent(peptide, spectrum):
				#peptides.remove(peptide)
				#print(peptide, "isnt consistent")
				need_delete.append(peptide)
						
		for nd in need_delete:
			#print("need_delete = ", nd)#, end=" ")
			peptides.remove(nd)
		#print()
		#print(peptides)
		#print(not peptides)
		
		if peptides:
			peptides = expand(peptides)
			#print(peptides)
		

def main():
	
	#input(spectrum_list)
	#spectrum_str = input().split()#spectrum_list.split()
	#spectrum = [int(elem) for elem in spectrum_str]
	spectrum = [int(elem) for elem in input().split()]
	#print(spectrum)
	
	cyclopeptide_sequencing(spectrum)
	
	
	#cyclopeptide_sequencing([0, 113, 128, 186, 241, 299, 314, 427])
	#cyclopeptide_sequencing([0, 97, 97, 99, 101, 103, 196, 198, 198, 200, 202, 295, 297, 299, 299, 301, 394, 396, 398, 400, 400, 497])
	#0 97 97 99 101 103 196 198 198 200 202 295 297 299 299 301 394 396 398 400 400 497
	#print(masses_dict)
	
	#print(is_consistent([97, 97, 103], [0, 97, 97,99,101,103,196,198,198,200,202]))
	#print(is_consistent([101, 102], [0, 97, 97,99,101,103,196,198,198,200,202]))
	#print(cyclospectrum([113, 129, 128, 114]))
	

if __name__ == "__main__":
	main()
	
	