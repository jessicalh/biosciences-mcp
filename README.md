# Biosciences Toolkit MCP Server

A comprehensive bioinformatics MCP (Model Context Protocol) server that provides powerful sequence analysis, protein characterization, and molecular biology tools directly to Claude Desktop.

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

### Method 1: MCPB Bundle (Recommended)

1. Download the `.mcpb` file from the releases page
2. Open Claude Desktop
3. Navigate to Settings > Extensions
4. Click "Install Extension..." and select the `.mcpb` file
5. Restart Claude Desktop

### Method 2: Manual Configuration

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure Claude Desktop by editing `claude_desktop_config.json`:

   **Using uv (recommended):**
   ```json
   {
     "mcpServers": {
       "biosciences": {
         "command": "uv",
         "args": [
           "run",
           "--with", "fastmcp",
           "--with", "biopython",
           "fastmcp", "run",
           "/path/to/biosciences-mcp/server/main.py"
         ]
       }
     }
   }
   ```

   **Using Python directly:**
   ```json
   {
     "mcpServers": {
       "biosciences": {
         "command": "python",
         "args": ["/path/to/biosciences-mcp/server/main.py"]
       }
     }
   }
   ```

4. Restart Claude Desktop

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

## Building the MCPB Bundle

To create your own `.mcpb` bundle:

1. Install the MCPB CLI:
   ```bash
   npm install -g @anthropic-ai/mcpb
   ```

2. Navigate to this directory:
   ```bash
   cd biosciences-mcp
   ```

3. Pack the bundle:
   ```bash
   mcpb pack
   ```

This will create `biosciences-toolkit.mcpb` that can be shared and installed.

## Requirements

- Python 3.8 or higher
- Claude Desktop 0.10.0 or higher
- Biopython 1.85 or higher
- FastMCP 0.3.0 or higher

## Dependencies

The server uses the following Python libraries:
- **FastMCP**: MCP server framework
- **Biopython**: Core bioinformatics toolkit

## Troubleshooting

### Server not appearing in Claude Desktop
1. Check that Claude Desktop has been restarted
2. Verify the path in `claude_desktop_config.json` is correct
3. Ensure Python and dependencies are properly installed

### Tool execution errors
1. Verify sequence format (DNA should contain only ATCG, RNA: AUCG, Protein: standard amino acids)
2. Check that sequences are valid for the operation (e.g., no stop codons for translation)
3. For BLAST searches, ensure you have internet connectivity

### Permission errors
- On Windows, ensure the Python script has execute permissions
- On Unix systems, you may need to make the script executable: `chmod +x server/main.py`

## Contributing

Contributions are welcome! Some ideas for enhancements:
- Add support for multiple sequence alignment
- Integrate more genomics databases
- Add phylogenetic tree building
- Support for structural biology tools
- Integration with visualization libraries

## License

MIT License - see LICENSE file for details

## Acknowledgments

Built with:
- [Biopython](https://biopython.org/) - The foundation of bioinformatics in Python
- [FastMCP](https://github.com/jlowin/fastmcp) - Making MCP servers fast and simple
- [Model Context Protocol](https://modelcontextprotocol.io/) - Anthropic's protocol for AI-tool integration

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check the documentation at the MCP website
- Review Biopython documentation for sequence analysis details
