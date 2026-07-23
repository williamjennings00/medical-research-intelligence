from Bio import Entrez
from config.settings import settings
import xml.etree.ElementTree as ET

Entrez.email = settings.EMAIL

def fetch_gene(gene_name: str, organism: str = "Homo sapiens"):
    """
    Fetch basic gene metadata from NCBI Gene.

    Parameters
    ----------
    gene_name : str
        Gene symbol (e.g. TP53, BRCA1).
    organism : str
        Organism name.

    Returns
    -------
    dict | None
    """

    query = f"{gene_name}[Gene Name] AND {organism}[Organism]"

    # Search NCBI Gene
    with Entrez.esearch(db="gene", term=query) as handle:
        result = Entrez.read(handle)

    if not result["IdList"]:
        return None

    gene_id = result["IdList"][0]

    # Fetch gene record
    with Entrez.efetch(db="gene", id=gene_id, retmode="xml") as handle:
        records = Entrez.read(handle, validate=False)

    if not records:
        return None

    gene = records[0]

    gene_ref = gene["Entrezgene_gene"]["Gene-ref"]

    return {
        "gene_id": gene_id,
        "symbol": gene_ref.get("Gene-ref_locus", ""),
        "description": gene_ref.get("Gene-ref_desc", ""),
        "organism": organism,
    }


def search_pubmed(term, max_results=5):
    """
    Search PubMed and return article IDs.
    """

    handle = Entrez.esearch(
        db="pubmed",
        term=term,
        retmax=max_results
    )

    results = Entrez.read(handle)
    handle.close()

    return results["IdList"]


def fetch_details(pubmed_ids):
    """
    Fetch article information.
    """

    ids = ",".join(pubmed_ids)

    handle = Entrez.efetch(
        db="pubmed",
        id=ids,
        rettype="medline",
        retmode="text"
    )

    records = handle.read()
    handle.close()

    return records



