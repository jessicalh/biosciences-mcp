# Biosciences MCP Server - Windows Setup Guide

## Working Configuration (October 2025)

This document describes the **working setup** for running the Biosciences MCP Server (Biopython toolkit) on Windows with Claude Desktop.

## Prerequisites

- **Python 3.8+** (tested with Python 3.14)
- **Claude Desktop** installed
- **Git** for version control

## Installation Steps

### 1. Clone the Repository

```bash
cd C:\projects\mcp
gh repo clone jessicalh/biosciences-mcp
cd biosciences-mcp
```

### 2. Install Python Dependencies

```bash
pip install fastmcp biopython
```

**Dependencies**:
- `fastmcp>=0.3.0` - MCP server framework
- `biopython>=1.85` - Bioinformatics toolkit

### 3. Configure Claude Desktop

Edit `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "biosciences": {
      "command": "python",
      "args": [
        "C:\\projects\\mcp\\biosciences-mcp\\server\\main.py"
      ]
    }
  }
}
```

**Key Points**:
- Uses **Python directly**
- Entry point is `server/main.py`
- Paths use double backslashes in JSON

### 4. Restart Claude Desktop

Close Claude Desktop completely and reopen it.

### 5. Test the Server

In Claude Desktop, ask:
```
What biosciences tools do you have?
```

You should see a list of 12 bioinformatics tools.

**Example commands**:
```
What's the reverse complement of ATCGATCG?
Calculate the GC content of this DNA sequence: GGCCAATTGGCC
Analyze this protein sequence: MKTIIALSYIFCLVFADYKDDDDK
```

## Available Tools

The Biosciences MCP server provides 12 tools:

### DNA/RNA Analysis
1. **reverse_complement** - Get reverse complement of DNA/RNA
2. **transcribe** - Transcribe DNA to RNA
3. **translate** - Translate nucleotide sequence to protein
4. **gc_content** - Calculate GC content percentage
5. **molecular_weight** - Calculate molecular weight
6. **find_orfs** - Identify Open Reading Frames
7. **find_motif** - Find pattern occurrences

### Protein Analysis
8. **protein_analysis** - Comprehensive protein characterization (MW, pI, instability, secondary structure)

### Sequence Alignment & Search
9. **pairwise_alignment** - Align two sequences (global/local)
10. **ncbi_blast_search** - Search NCBI databases
11. **calculate_sequence_distance** - Calculate sequence similarity

### Format Conversion
12. **convert_sequence_format** - Convert between sequence formats (FASTA, GenBank, EMBL)

## Troubleshooting

### Error: "No module named 'fastmcp'" or "No module named 'Bio'"

**Solution**: Install the dependencies:
```bash
pip install fastmcp biopython
```

### BLAST searches fail

**Solution**: Ensure you have internet connectivity. NCBI BLAST requires network access.

### Tools not showing in Claude Desktop

**Solution**:
1. Check Claude Desktop logs for errors
2. Verify the path in `claude_desktop_config.json` is correct
3. Ensure you restarted Claude Desktop after config changes

## Project Structure

```
biosciences-mcp/
├── server/
│   ├── __init__.py
│   └── main.py                 # Entry point
├── requirements.txt            # Python dependencies
├── manifest.json              # MCP server manifest
└── WINDOWS_SETUP.md          # This file
```

## How It Works

The server is built using:
- **FastMCP**: Provides the MCP protocol implementation
- **Biopython**: Provides bioinformatics algorithms and tools

The server exposes Biopython functionality through the Model Context Protocol, allowing Claude to perform sequence analysis, protein characterization, and other bioinformatics tasks.

## Notes

- **Alpha version**: This is an alpha release tested locally
- **Internet required**: BLAST searches require internet connectivity
- **Sequence formats**: DNA (ATCG), RNA (AUCG), Protein (standard amino acids)
- **Performance**: Most operations are fast (<1 second), BLAST can take minutes

## Example Workflows

### Basic Sequence Analysis
```
"What's the GC content of GGCCAATTGGCC?"
"Get the reverse complement of ATCGATCG"
"Transcribe and translate ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
```

### Protein Analysis
```
"Analyze this protein: MKTIIALSYIFCLVFADYKDDDDK"
"What's the molecular weight and pI of ACDEFGHIKLMNPQRSTVWY?"
```

### Advanced Analysis
```
"Find all ATG codons in ATGCCGATGATGTTTATG"
"Find ORFs longer than 100bp in this sequence: [your sequence]"
"Align these sequences: ACGTACGT and ACGTCGT"
```

## Version History

- **October 30, 2025**: Initial Windows setup documentation
- Successfully tested with Python 3.14 on Windows 11
- Alpha version (0.1.0-alpha)

## License

MIT License - see LICENSE file for details
