

#genome = "GATATATGCATATACTT"
#pattern = "ATAT"

print("input pattern: ")
pattern = input();

print("input genome: ")
genome = input();

pattern_len = len(pattern)
genome_len = len(genome)

count = 0

#print("\n")
for i in range(0, genome_len - pattern_len + 1):
	if genome[i:i + pattern_len] == pattern:
		count += 1

print(count)