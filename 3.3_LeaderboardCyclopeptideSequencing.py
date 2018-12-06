import functools as ft

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


		
def linear_scoring(peptide, spectrum):

	if not peptide:
		return 0

	pep_spectrum = linear_spectrum(peptide)
	specCpy = spectrum.copy()
	score = 0
	
	for mass in pep_spectrum:
		if mass in specCpy:
			specCpy.remove(mass)
			score += 1

	return score
		


def score_cmp(first, second, spectrum):
	return linear_scoring(second, spectrum) - linear_scoring(first, spectrum)
	
	

def cmp_to_key(cmp, spectrum):
	class K:
		def __init__(self, obj, *args):
			self.obj = obj
		def __lt__(self, other):
			return cmp(self.obj, other.obj, spectrum) < 0
		def __gt__(self, other):
			return cmp(self.obj, other.obj, spectrum) > 0
		def __eq__(self, other):
			return cmp(self.obj, other.obj, spectrum) == 0
		def __le__(self, other):
			return cmp(self.obj, other.obj, spectrum) <= 0
		def __ge__(self, other):
			return cmp(self.obj, other.obj, spectrum) >= 0
		def __ne__(self, other):
			return cmp(self.obj, other.obj, spectrum) != 0
	return K	
	
	
		
def trim(leaderboard, spectrum, n):
	
	sorted_leaderboard = sorted(leaderboard, key=cmp_to_key(score_cmp, spectrum))
	trimmed_s_l = sorted_leaderboard[:n]
	
	for pep in sorted_leaderboard[n:]:
		if linear_scoring(pep, spectrum) == linear_scoring(trimmed_s_l[-1], spectrum):
			trimmed_s_l.append(pep)
		else:
			break
			
	return trimmed_s_l
		
		
	
def leaderboard_cyclopeptide_sequencing(spectrum, n):
	
	leaderboard = []
	leaderboard = expand(leaderboard)
	leader_peptide = []
	
	while leaderboard:	
		need_delete = []
		
		for peptide in leaderboard:
			if mass(peptide) == parent_mass(spectrum):
				if linear_scoring(peptide, spectrum) > linear_scoring(leader_peptide, spectrum):
					leader_peptide = peptide

			elif mass(peptide) > parent_mass(spectrum):
				need_delete.append(peptide)
						
		for nd in need_delete:
			leaderboard.remove(nd)
			
		leaderboard = trim(leaderboard, spectrum, n)	
		
		if leaderboard:
			leaderboard = expand(leaderboard)
		
	return leader_peptide

def main():
	N = int(input())
	spectrum = [int(elem) for elem in input().split()]
	print_peptide(leaderboard_cyclopeptide_sequencing(spectrum, N))

if __name__ == "__main__":
	main()
