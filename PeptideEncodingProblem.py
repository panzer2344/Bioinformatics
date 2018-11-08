RNAdict = {
	'AAA' : 'K', 'AAC' : 'N', 'AAG' : 'K', 'AAU' : 'N', 'ACA' : 'T', 
	'ACC' : 'T', 'ACG' : 'T', 'ACU' : 'T', 'AGA' : 'R', 'AGC' : 'S', 'AGG' : 'R',
	'AGU' : 'S', 'AUA' : 'I', 'AUC' : 'I', 'AUG' : 'M', 'AUU' : 'I', 'CAA' : 'Q',
	'CAC' : 'H', 'CAG' : 'Q', 'CAU' : 'H', 'CCA' : 'P', 'CCC' : 'P', 'CCG' : 'P',
	'CCU' : 'P', 'CGA' : 'R', 'CGC' : 'R', 'CGG' : 'R', 'CGU' : 'R', 'CUA' : 'L',
	'CUC' : 'L', 'CUG' : 'L', 'CUU' : 'L', 'GAA' : 'E', 'GAC' : 'D', 'GAG' : 'E',
	'GAU' : 'D', 'GCA' : 'A', 'GCC' : 'A', 'GCG' : 'A', 'GCU' : 'A', 'GGA' : 'G',
	'GGC' : 'G', 'GGG' : 'G', 'GGU' : 'G', 'GUA' : 'V', 'GUC' : 'V', 'GUG' : 'V',
	'GUU' : 'V', 'UAA' : '', 'UAC' : 'Y', 'UAG' : '', 'UAU' : 'Y', 'UCA' : 'S', 
	'UCC' : 'S', 'UCG' : 'S', 'UCU' : 'S', 'UGA' : '', 'UGC' : 'C', 'UGG' : 'W', 
	'UGU' : 'C', 'UUA' : 'L', 'UUC' : 'F', 'UUG' : 'L', 'UUU' : 'F'
}

def main():
	result = []
	text = input()
	peptide = input()
	#text = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
	#peptide = "MA"
	peptide_len = len(peptide)
	pptd_len_inText = peptide_len * 3
	text_len = len(text)
	
	for i in range(0, text_len - pptd_len_inText + 1):
		pattern = text[i:i + pptd_len_inText]
		reversePattern = reverese_complement(pattern, pptd_len_inText)
		
		tripletsOriginal = []
		for i in range(0, pptd_len_inText, 3):
			tripletsOriginal += [pattern[i:i+3]]
		
		tripletsReverse = []
		for i in range(0, pptd_len_inText, 3):
			tripletsReverse += [reversePattern[i:i+3]]
		
		translPep = translation(tripletsOriginal)
		translRrsPep = translation(tripletsReverse)
		if translPep == peptide or translRrsPep == peptide:
			result += [pattern]
	#result.sort()
	for res in result:
		print(res)
	
	
def reverese_complement(_text, _text_len):
	reverse = _text
	complements = ['A', 'G', 'C', 'T']
	for i in range(0, _text_len):
		for j in range(0, 4):
			if reverse[i] == complements[j]:
				reverse = reverse[:i] + complements[3 - j] + reverse[i+1:]
				break
	return reverse[::-1]

def translation(triplets):
	result = ""
	for triplet in triplets:
		triplet = triplet.replace('T', 'U')
		rna = RNAdict.get(triplet)
		if rna == None:
			return None
		else:
			result += rna
	return result
	
		
		
if __name__ == "__main__":
		main()