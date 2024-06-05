![logo](https://github.com/WilliamFernandoC-P/General/blob/main/Images/Python_Scripts.png)
This repository contains several Python scripts for use in bioinformatics tasks and projects, such as DNA/RNA sequence management.

* [Download_GenBank_Sequences.py](https://github.com/WilliamFernandoC-P/Python_Scripts/blob/main/Download_GenBank_Sequences.py) is a Python script that uses the Biopython library to fetch nucleotide sequences from the NCBI database (GenBank) using a list of accession numbers. For each accession number, the script retrieves the corresponding GenBank record, saves the sequence in FASTA format to a local file named after the accession number. This allows for the automated download and conversion of nucleotide sequences from GenBank to FASTA format.
* [Extract_specific_region_from_alignment.py](https://github.com/WilliamFernandoC-P/Python_Scripts/blob/main/Extract_specific_region_from_alignment.py) This Python script uses the Biopython library to process a multiple sequence alignment in FASTA format. The script performs the following tasks:
  * Load the Alignment: Reads the aligned sequences from a file in .fasta format.
  * Define Region of Interest: Specifies the start and end positions of the region to be extracted from the alignment.
  * Extract Sub-alignment: Creates a new alignment containing only the specified region of each sequence.
  * Save Sub-alignment: Writes the extracted sub-alignment to a new FASTA file named aligned_protein_G.fasta.
  * This allows for focusing on and saving a specific region of interest from a multiple sequence alignment.
  







