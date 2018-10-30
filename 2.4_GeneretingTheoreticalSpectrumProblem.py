Masses = {
	'A' : 71, 'R' : 156, 'N' : 114, 'D' : 115, 'C' : 103, 'E' : 129, 'Q' : 128, 'G' : 57, 'H' : 137, 
	'I' : 113, 'L' : 113, 'K' : 128, 'M' : 131, 'F' : 147, 'P' : 97, 'S' : 87, 'T' : 101, 'W' : 186, 
	'Y' : 163, 'V' : 99 
}

def add_mass(_subpeptide, _spMasses):
	spMass = 0
	for amin in _subpeptide:
		spMass += Masses.get(amin)
	_spMasses += [spMass]

peptide = input()
peptide_len = len(peptide)

spMasses = [0]

for i in range(1, peptide_len):
	for j in range(0, peptide_len):
		subpeptide = ""
		tail = i if i <= peptide_len - j else peptide_len - j
		stump = i - tail
		subpeptide += peptide[j:j+tail]
		subpeptide += peptide[0:stump]
		add_mass(subpeptide, spMasses)
spMasses.sort()
add_mass(peptide, spMasses)
for mass in spMasses:
	print(mass, end=" ")