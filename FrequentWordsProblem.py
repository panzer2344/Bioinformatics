#text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
#k = 4
#CATG GCAT

text = input()
k = int(input())
kMers = []
max_frequence = -1

text_len = len(text)

for i in range(0, text_len - k + 1):
	
	frequense = 1
	tmp = text[i: i + k]
	
	for j in range(i + 1, text_len - k + 1):
		if text[j: j + k] == tmp:
			frequense += 1	
	
	if frequense == max_frequence:
		kMers += [tmp];
	
	if frequense > max_frequence:
		max_frequence = frequense
		kMers = [tmp];


for kMer in kMers:	
	print(kMer, end=" ")