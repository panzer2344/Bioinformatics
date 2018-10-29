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
	#text = input()
	#peptide = input()
	text = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
	peptide = "MA"
	peptide_len = len(peptide)
	text_len = len(text)
	
	for i in range(0, text_len):
		pattern = text[i: i + 6]
		leftTriplet = pattern[:]

	
	
def reverese_complement(_text, _text_len):
	complements = ['A', 'G', 'C', 'T']
	for i in range(0, _text_len):
		for j in range(0, 4):
			if _text[i] == complements[j]:
				_text = _text[:i] + complements[3 - j] + _text[i+1:]
				break
	#resultString = _text[::-1].replace('T', 'U')
	return _text[::-1]#resultString
	
	
if __name__ == "__main__":
		main()
	
	