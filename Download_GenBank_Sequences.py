from Bio import Entrez
from Bio import SeqIO

# Email address (required for using NCBI Entrez)
Entrez.email = "email@email.com"

# Define the list of accession numbers (Each sequence accession number must be enclosed in quotation marks [""] and separated by a comma and a space)
accession_numbers = ["NC_038235", "NC_001781"...
]
    
# Download and save the sequences in FASTA format
for accession in accession_numbers:
    handle = Entrez.efetch(db="nucleotide", id=accession, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()
    
    # Save the sequence in FASTA format
    output_file = f"{accession}.fasta"
    SeqIO.write(record, output_file, "fasta")
    print(f"The sequence {accession} has been downloaded and saved in '{output_file}' in FASTA format.")
