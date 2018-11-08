Masses = {
	'A' : 71, 'R' : 156, 'N' : 114, 'D' : 115, 'C' : 103, 'E' : 129, 'Q' : 128, 'G' : 57, 'H' : 137, 
	'I' : 113, 'L' : 113, 'K' : 128, 'M' : 131, 'F' : 147, 'P' : 97, 'S' : 87, 'T' : 101, 'W' : 186, 
	'Y' : 163, 'V' : 99 
}
SortedMasses = list(set(sorted(int(value) for (key, value) in Masses.items())))
    
def countingPeptidesWithGivenMass(given):
	masses = [0 for i in range(0, given + 1)]
	masses[0] = 1
	for i in range(0, given + 1):
		for j in range(0, len(SortedMasses)):
			if i >= SortedMasses[j]:
				masses[i] += masses[i - SortedMasses[j]]
	return masses[given]
	
def main():
	given = int(input())
	print(countingPeptidesWithGivenMass(given))

if __name__ == "__main__":
	main()