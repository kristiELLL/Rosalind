"""

This code calculates the GC-content for a set of DNA strings in FASTA format,
and returns the ID and GC-content of the strings.

The code uses the Biopython library, so you first need to install biopython with pip. 

"""


from Bio import SeqIO

# Open the fasta file and loop through its sequences
fasta_file = "rosalind_gc.txt"

rosalind_list = []

for record in SeqIO.parse(fasta_file, "fasta"):
    seq_id = record.id
    seq = str(record.seq)
    #print(f"Sequence ID: {seq_id}")
    #print(f"Sequence: {seq}")
    rosalind_list.append(seq_id)
    rosalind_list.append(seq)

#print(rosalind_list)

rosalind_dict = {}

for i in range(0, len(rosalind_list), 2):
    key = rosalind_list[i]
    value = rosalind_list[i+1]
    rosalind_dict[key] = value

print(rosalind_dict)


def CG_percentage(i):
    length= len(i)
    sum_C = i.count("C")
    sum_G = i.count("G")
    sum_CG= sum_C + sum_G
    percentage = (sum_CG * 100) / length
    formatted_result = "{:.6f}".format(percentage)
    print(formatted_result)

for key, value in rosalind_dict.items():
    print(f"{key}")
    # Apply CG_percentage to the current value
    CG_percentage(value)
