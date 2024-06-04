from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# Load the nucleotide alignment
aligned_nucleotides = list(SeqIO.parse("aligned_nucleotide_sequences.fasta", "fasta"))

# Translate each nucleotide sequence to amino acids
aligned_proteins = []
for record in aligned_nucleotides:
    translated_seq = record.seq.translate(to_stop=True)
    aligned_proteins.append(SeqRecord(translated_seq, id=record.id, description=""))

# Save the aligned amino acid sequences to a file
with open("aligned_protein_sequences.fasta", "w") as output_handle:
    SeqIO.write(aligned_proteins, output_handle, "fasta")