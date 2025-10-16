#!/usr/bin/env python3
"""
Biosciences MCP Server
A comprehensive bioinformatics toolkit for Claude Desktop
"""

from fastmcp import FastMCP
from typing import Optional, List, Dict
import json

# Initialize MCP server
mcp = FastMCP("Biosciences Toolkit")

# =============================================================================
# DNA/RNA Sequence Analysis Tools
# =============================================================================

@mcp.tool()
def reverse_complement(sequence: str) -> str:
    """
    Returns the reverse complement of a DNA or RNA sequence.

    Args:
        sequence: DNA or RNA sequence string

    Returns:
        Reverse complement sequence
    """
    try:
        from Bio.Seq import Seq
        seq = Seq(sequence.upper())
        return str(seq.reverse_complement())
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def transcribe(sequence: str) -> str:
    """
    Transcribes a DNA sequence to RNA (replaces T with U).

    Args:
        sequence: DNA sequence string

    Returns:
        RNA sequence
    """
    try:
        from Bio.Seq import Seq
        seq = Seq(sequence.upper())
        return str(seq.transcribe())
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def translate(sequence: str, table: str = "Standard") -> str:
    """
    Translates a DNA or RNA sequence to protein sequence.

    Args:
        sequence: DNA or RNA sequence string
        table: Genetic code table name (default: "Standard")

    Returns:
        Protein sequence
    """
    try:
        from Bio.Seq import Seq
        seq = Seq(sequence.upper())
        return str(seq.translate(table=table))
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def gc_content(sequence: str) -> float:
    """
    Calculates the GC content (percentage) of a DNA/RNA sequence.

    Args:
        sequence: DNA or RNA sequence string

    Returns:
        GC content as percentage (0-100)
    """
    try:
        from Bio.SeqUtils import gc_fraction
        return gc_fraction(sequence.upper()) * 100
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def molecular_weight(sequence: str, seq_type: str = "DNA") -> float:
    """
    Calculates molecular weight of a sequence.

    Args:
        sequence: Sequence string
        seq_type: Type of sequence - "DNA", "RNA", or "protein"

    Returns:
        Molecular weight in Daltons
    """
    try:
        from Bio.SeqUtils import molecular_weight as mw
        from Bio.Seq import Seq

        seq = Seq(sequence.upper())
        if seq_type.upper() == "DNA":
            return mw(seq, seq_type="DNA")
        elif seq_type.upper() == "RNA":
            return mw(seq, seq_type="RNA")
        else:
            return mw(seq, seq_type="protein")
    except Exception as e:
        return f"Error: {str(e)}"


# =============================================================================
# Protein Analysis Tools
# =============================================================================

@mcp.tool()
def protein_analysis(sequence: str) -> Dict:
    """
    Comprehensive protein sequence analysis including molecular weight,
    aromaticity, instability index, isoelectric point, and secondary structure.

    Args:
        sequence: Protein sequence string

    Returns:
        Dictionary with various protein properties
    """
    try:
        from Bio.SeqUtils.ProtParam import ProteinAnalysis

        protein = ProteinAnalysis(sequence.upper())

        return {
            "molecular_weight": round(protein.molecular_weight(), 2),
            "aromaticity": round(protein.aromaticity(), 4),
            "instability_index": round(protein.instability_index(), 2),
            "isoelectric_point": round(protein.isoelectric_point(), 2),
            "gravy": round(protein.gravy(), 4),
            "secondary_structure_fraction": {
                "helix": round(protein.secondary_structure_fraction()[0], 4),
                "turn": round(protein.secondary_structure_fraction()[1], 4),
                "sheet": round(protein.secondary_structure_fraction()[2], 4)
            },
            "amino_acid_percent": {k: round(v*100, 2) for k, v in protein.get_amino_acids_percent().items()}
        }
    except Exception as e:
        return {"error": str(e)}


# =============================================================================
# Sequence Format Conversion Tools
# =============================================================================

@mcp.tool()
def convert_sequence_format(sequence_data: str, input_format: str, output_format: str) -> str:
    """
    Converts between different sequence file formats (FASTA, GenBank, EMBL, etc.).

    Args:
        sequence_data: Sequence data in the input format
        input_format: Input format (fasta, genbank, embl, etc.)
        output_format: Output format (fasta, genbank, embl, etc.)

    Returns:
        Converted sequence data
    """
    try:
        from Bio import SeqIO
        from io import StringIO

        # Parse input
        input_handle = StringIO(sequence_data)
        records = list(SeqIO.parse(input_handle, input_format.lower()))

        # Convert to output
        output_handle = StringIO()
        SeqIO.write(records, output_handle, output_format.lower())

        return output_handle.getvalue()
    except Exception as e:
        return f"Error: {str(e)}"


# =============================================================================
# Sequence Search and Pattern Matching
# =============================================================================

@mcp.tool()
def find_motif(sequence: str, motif: str) -> List[int]:
    """
    Finds all occurrences of a motif in a sequence.

    Args:
        sequence: DNA, RNA, or protein sequence
        motif: Motif pattern to search for

    Returns:
        List of positions where motif is found (1-indexed)
    """
    try:
        sequence = sequence.upper()
        motif = motif.upper()
        positions = []

        for i in range(len(sequence) - len(motif) + 1):
            if sequence[i:i+len(motif)] == motif:
                positions.append(i + 1)  # 1-indexed

        return positions
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def find_orfs(sequence: str, min_length: int = 100) -> List[Dict]:
    """
    Finds Open Reading Frames (ORFs) in a DNA sequence.

    Args:
        sequence: DNA sequence
        min_length: Minimum ORF length in nucleotides (default: 100)

    Returns:
        List of ORFs with position, strand, and sequence information
    """
    try:
        from Bio import Seq

        seq = Seq.Seq(sequence.upper())
        orfs = []

        # Check all 6 frames (3 forward, 3 reverse)
        for strand, seq_strand in [(+1, seq), (-1, seq.reverse_complement())]:
            for frame in range(3):
                trans = str(seq_strand[frame:].translate())
                trans_len = len(trans)
                aa_start = 0

                while aa_start < trans_len:
                    aa_end = trans.find("*", aa_start)
                    if aa_end == -1:
                        aa_end = trans_len

                    if aa_end - aa_start >= min_length // 3:
                        if strand == 1:
                            start = frame + aa_start * 3
                            end = frame + aa_end * 3 + 3
                        else:
                            start = len(seq) - frame - aa_end * 3 - 3
                            end = len(seq) - frame - aa_start * 3

                        orfs.append({
                            "start": start + 1,  # 1-indexed
                            "end": end,
                            "strand": "+" if strand == 1 else "-",
                            "frame": frame + 1,
                            "length": (aa_end - aa_start) * 3,
                            "protein": trans[aa_start:aa_end]
                        })

                    aa_start = aa_end + 1

        return orfs
    except Exception as e:
        return {"error": str(e)}


# =============================================================================
# Pairwise Sequence Alignment
# =============================================================================

@mcp.tool()
def pairwise_alignment(seq1: str, seq2: str, alignment_type: str = "global") -> Dict:
    """
    Performs pairwise sequence alignment using Needleman-Wunsch (global)
    or Smith-Waterman (local) algorithm.

    Args:
        seq1: First sequence
        seq2: Second sequence
        alignment_type: "global" or "local" (default: "global")

    Returns:
        Dictionary with alignment score and aligned sequences
    """
    try:
        from Bio import pairwise2
        from Bio.Seq import Seq

        s1 = Seq(seq1.upper())
        s2 = Seq(seq2.upper())

        if alignment_type.lower() == "global":
            alignments = pairwise2.align.globalxx(s1, s2)
        else:
            alignments = pairwise2.align.localxx(s1, s2)

        if alignments:
            best = alignments[0]
            return {
                "score": best[2],
                "aligned_seq1": best[0],
                "aligned_seq2": best[1],
                "start": best[3],
                "end": best[4]
            }
        else:
            return {"error": "No alignment found"}
    except Exception as e:
        return {"error": str(e)}


# =============================================================================
# BLAST-like Sequence Search (using NCBI BLAST)
# =============================================================================

@mcp.tool()
def ncbi_blast_search(sequence: str, database: str = "nt", program: str = "blastn") -> str:
    """
    Performs NCBI BLAST search for a sequence.

    Args:
        sequence: Query sequence
        database: BLAST database (nt, nr, etc.)
        program: BLAST program (blastn, blastp, blastx, etc.)

    Returns:
        BLAST results summary
    """
    try:
        from Bio.Blast import NCBIWWW, NCBIXML
        from io import StringIO

        # Perform BLAST search
        result_handle = NCBIWWW.qblast(program, database, sequence)
        blast_record = NCBIXML.read(result_handle)

        results = []
        for alignment in blast_record.alignments[:5]:  # Top 5 hits
            for hsp in alignment.hsps[:1]:  # Best HSP per alignment
                results.append({
                    "title": alignment.title,
                    "length": alignment.length,
                    "e_value": hsp.expect,
                    "score": hsp.score,
                    "identities": f"{hsp.identities}/{hsp.align_length}"
                })

        return json.dumps(results, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


# =============================================================================
# Phylogenetics and Evolution
# =============================================================================

@mcp.tool()
def calculate_sequence_distance(seq1: str, seq2: str) -> float:
    """
    Calculates Hamming distance between two sequences of equal length.

    Args:
        seq1: First sequence
        seq2: Second sequence

    Returns:
        Hamming distance (proportion of differing positions)
    """
    try:
        if len(seq1) != len(seq2):
            return "Error: Sequences must be of equal length"

        differences = sum(c1 != c2 for c1, c2 in zip(seq1.upper(), seq2.upper()))
        return round(differences / len(seq1), 4)
    except Exception as e:
        return f"Error: {str(e)}"


# =============================================================================
# Main entry point
# =============================================================================

if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
