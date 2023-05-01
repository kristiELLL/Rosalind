sample = "AAAACCCGGT"
complement = ""

for i in sample:
    if i == "A":
        complement += "T"
    elif i == "C":
        complement += "G"
    elif i == "T":
        complement += "A"
    elif i == "G":
        complement += "C"

reverse = complement[::-1]
print(reverse)
