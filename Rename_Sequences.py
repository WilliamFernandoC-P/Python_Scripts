# Import necessary libraries
from docx import Document  # To work with DOCX files
import re  # To work with regular expressions

# Function to read the content of a FASTA file and return it as a list of lines
def read_fasta(file_path):
    with open(file_path, 'r') as file:
        fasta_content = file.readlines()
    return fasta_content

# Function to read a DOCX file and extract the mapping of identifiers to genotypes
def read_docx(file_path):
    document = Document(file_path)
    mapping = {}
    for table in document.tables:  # Iterate over all tables in the DOCX file
        for row in table.rows:  # Iterate over all rows in each table
            identifier = row.cells[0].text.strip()  # Extract the identifier (first column)
            genotype = row.cells[2].text.strip()  # Extract the genotype (third column)
            if identifier and genotype:
                # Store both the base identifier (without ".1" suffix) and the full identifier in the mapping
                identifier_base = identifier.split('.')[0]
                mapping[identifier_base] = genotype
                mapping[identifier] = genotype
    return mapping

# Function to modify identifier lines in the FASTA content based on the mapping
def modify_fasta(fasta_content, mapping):
    modified_fasta = []
    for line in fasta_content:
        if line.startswith('>'):  # Look for lines starting with '>', which are identifiers in FASTA
            # Extract the identifier using a regular expression
            match = re.match(r">(.*?)\s", line)
            if match:
                identifier_full = match.group(1)  # Full identifier
                identifier_base = identifier_full.split('.')[0]  # Base identifier
                if identifier_full in mapping:
                    # Use the full identifier if it is in the mapping
                    new_identifier = f">{identifier_full}_{mapping[identifier_full]}\n"
                elif identifier_base in mapping:
                    # Use the base identifier if it is in the mapping
                    new_identifier = f">{identifier_base}_{mapping[identifier_base]}\n"
                else:
                    # If no mapping is found, add a "NOT_FOUND" notice
                    new_identifier = f">{identifier_full}_NOT_FOUND\n"
                line = new_identifier
        modified_fasta.append(line)  # Add the line (modified or not) to the new FASTA content
    return modified_fasta

# Function to save the modified FASTA content to a new file
def save_fasta(file_path, modified_fasta):
    with open(file_path, 'w') as file:
        file.writelines(modified_fasta)

# Specify the paths for the input and output files
fasta_file_path = 'RSV-B_GenBank_Sequences.FASTA'
docx_file_path = 'Reference RSV-AB Genotypes.docx'

# Read the input files
fasta_content = read_fasta(fasta_file_path)
mapping = read_docx(docx_file_path)

# Modify the FASTA file content
modified_fasta = modify_fasta(fasta_content, mapping)

# Save the modified FASTA file
save_fasta(f'Modified_{fasta_file_path}', modified_fasta)

# Print a message indicating that the process was successful
print("The FASTA file has been successfully modified and saved.")
