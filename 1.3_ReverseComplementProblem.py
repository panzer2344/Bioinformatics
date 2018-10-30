#Sample Input:
#text = "AAAACCCGGT"
#Sample Output:
#	ACCGGGTTTT


complements = ['A', 'G', 'C', 'T']

text = input()

text_len = len(text)

for i in range(0, text_len):
	for j in range(0, 4):
		if text[i] == complements[j]:
			text = text[:i] + complements[3 - j] + text[i+1:]
			break;
			


print(text[::-1])