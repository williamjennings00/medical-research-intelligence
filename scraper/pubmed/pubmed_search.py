from Bio import Entrez
from config.settings import settings

Entrez.email = settings.EMAIL

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



