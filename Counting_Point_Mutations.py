"""
Given two strings s and t. The Hamming distance between s and t,
result is the number of corresponding symbols that differ in s and t.
"""

string1 = "GAGCCTACTAACGGGAT"
string2 = "CATCGTAATGACGGCCT"
mismatch_count = 0

# Compare the strings symbol by symbol
for i in range(min(len(string1), len(string2))):
    if string1[i] != string2[i]:
        mismatch_count += 1

# Add any remaining symbols in longer string to the count
mismatch_count += abs(len(string1) - len(string2))

print(mismatch_count)
