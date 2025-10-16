# Biosciences Toolkit MCP Server

**Alpha version - tested locally only**

A bioinformatics MCP (Model Context Protocol) server built with FastMCP and Biopython. Provides sequence analysis and molecular biology tools for Claude Desktop.

## Features

### DNA/RNA Analysis
- **Reverse Complement**: Generate reverse complement of DNA/RNA sequences
- **Transcription**: Convert DNA to RNA sequences
- **Translation**: Translate nucleotide sequences to proteins
- **GC Content**: Calculate GC percentage
- **Molecular Weight**: Calculate molecular weight of sequences
- **Find ORFs**: Identify Open Reading Frames in DNA sequences
- **Motif Finding**: Search for specific patterns in sequences

### Protein Analysis
- **Comprehensive Protein Analysis**: Get molecular weight, isoelectric point, instability index, aromaticity, GRAVY score
- **Secondary Structure Prediction**: Estimate helix, turn, and sheet fractions
- **Amino Acid Composition**: Detailed breakdown of amino acid percentages

### Sequence Alignment & Search
- **Pairwise Alignment**: Global (Needleman-Wunsch) or local (Smith-Waterman) alignment
- **NCBI BLAST Search**: Search sequences against NCBI databases
- **Sequence Distance**: Calculate Hamming distance between sequences

### Format Conversion
- **Multi-format Support**: Convert between FASTA, GenBank, EMBL, and other formats

## Installation

1. Download the `.mcpb` file from the [releases page](https://github.com/jessicalh/biosciences-mcp/releases)
2. Open Claude Desktop
3. Navigate to Settings > Extensions
4. Click "Install Extension..." and select the `.mcpb` file
5. Restart Claude Desktop

## Usage Examples

Once installed, you can ask Claude to perform bioinformatics tasks naturally:

### Sequence Analysis
```
"What's the reverse complement of ATCGATCG?"
"Calculate the GC content of this DNA sequence: GGCCAATTGGCC"
"Transcribe and translate this DNA sequence: ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
```

### Protein Analysis
```
"Analyze this protein sequence: MKTIIALSYIFCLVFADYKDDDDK"
"What's the molecular weight and isoelectric point of this peptide: ACDEFGHIKLMNPQRSTVWY"
```

### Advanced Features
```
"Find all ATG start codons in this sequence: ATGCCGATGATGTTTATG"
"Find all ORFs longer than 100bp in this DNA sequence: [your sequence]"
"Align these two sequences: ACGTACGT and ACGTCGT"
"Search this sequence in NCBI: ATCGATCGATCG"
```

## Available Tools

| Tool | Description |
|------|-------------|
| `reverse_complement` | Get reverse complement of DNA/RNA |
| `transcribe` | Transcribe DNA to RNA |
| `translate` | Translate nucleotide sequence to protein |
| `gc_content` | Calculate GC content percentage |
| `molecular_weight` | Calculate molecular weight |
| `protein_analysis` | Comprehensive protein characterization |
| `convert_sequence_format` | Convert between sequence formats |
| `find_motif` | Find pattern occurrences |
| `find_orfs` | Identify Open Reading Frames |
| `pairwise_alignment` | Align two sequences |
| `ncbi_blast_search` | Search NCBI databases |
| `calculate_sequence_distance` | Calculate sequence similarity |

## Requirements

- Python 3.8 or higher
- Claude Desktop 0.10.0 or higher
- Biopython 1.85 or higher
- FastMCP 0.3.0 or higher

## Dependencies

- **FastMCP** (>=0.3.0): MCP server framework
- **Biopython** (>=1.85): Sequence analysis and bioinformatics toolkit

## Troubleshooting

- Ensure Claude Desktop has been restarted after installation
- For BLAST searches, internet connectivity is required
- Sequence format requirements: DNA (ATCG), RNA (AUCG), Protein (standard amino acids)

## Status

This is an alpha version tested locally. Use at your own risk.

## License

MIT License - see LICENSE file for details

## Built With

- [Biopython](https://biopython.org/)
- [FastMCP](https://github.com/jlowin/fastmcp)
- [Model Context Protocol](https://modelcontextprotocol.io/)
