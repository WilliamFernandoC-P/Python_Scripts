from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment

# Load the alignment
alignment = AlignIO.read("aligned_sequences.fasta", "fasta")

# Define the start and end positions of the region 
start_pos = 100  # Adjust as necessary
end_pos = 300    # Adjust as necessary

# Extract the region of interest
sub_alignment = MultipleSeqAlignment([record[:, start_pos:end_pos] for record in alignment])

# Save the sub-alignment to a file
with open("aligned_protein_G.fasta", "w") as output_handle:
    AlignIO.write(sub_alignment, output_handle, "fasta")